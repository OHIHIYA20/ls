# -*- coding: utf-8 -*-
"""
.. module:: network_dialog
    :platform: Linux, Windows
    :synopsis: GUI for adjusment calculation

.. moduleauthor: Zoltan Siki <siki@agt.bme.hu>
"""
import platform
from PyQt4.QtGui import QDialog, QFont

from network_calc import Ui_NetworkCalcDialog
from surveying_util import *
from gama_interface import *
# debugging
from PyQt4.QtCore import pyqtRemoveInputHook
import pdb


class NetworkDialog(QDialog):
    """ Class for network calculation dialog
    """
    def __init__(self):
        """ Initialize dialog data and event handlers
        """
        super(NetworkDialog, self).__init__()
        self.ui = Ui_NetworkCalcDialog()
        self.ui.setupUi(self)
        if platform.system() == 'Linux':
            # change font
            self.ui.ResultTextBrowser.setFont(QFont("DejaVu Sans Mono", 9))
        self.points = []
        self.fix = []
        self.adj = []
        # event handling
        self.ui.CloseButton.clicked.connect(self.onCloseButton)
        self.ui.ResetButton.clicked.connect(self.onResetButton)
        self.ui.AddFixButton.clicked.connect(self.onAddFixButton)
        self.ui.AddAdjButton.clicked.connect(self.onAddAdjButton)
        self.ui.RemoveFixButton.clicked.connect(self.onRemoveFixButton)
        self.ui.RemoveAdjButton.clicked.connect(self.onRemoveAdjButton)
        self.ui.CalcButton.clicked.connect(self.onCalcButton)

    def showEvent(self, event):
        """ Set up initial state of dialog widgets

            :param event: NOT USED
        """
        self.reset()

    def reset(self):
        """ Reset dialog to initial state
        """
        self.points = get_measured()
        self.fix = []
        self.adj = []
        # clear lists
        self.ui.PointsList.clear()
        self.ui.FixList.clear()
        self.ui.AdjustedList.clear()
        self.ui.ResultTextBrowser.clear()
        i = 0
        if self.points is not None:
            for p in self.points:
                self.ui.PointsList.addItem(p[0])
                if p[1]:
                    item = self.ui.PointsList.item(i)
                    itemfont = item.font()
                    itemfont.setWeight(QFont.Bold)
                    item.setFont(itemfont)
                i += 1

    def onCloseButton(self):
        """ Close dialog after Close button pressed
        """
        self.accept()

    def onResetButton(self):
        """ Reset dialog to initial state after Reset button pressed
        """
        self.reset()

    def onAddFixButton(self):
        """ Move selected points to fix point list
        """
        selected = self.ui.PointsList.selectedItems()
        for item in selected:
            i = self.ui.PointsList.row(item)
            if self.points[i][1]:
                self.ui.FixList.addItem(self.ui.PointsList.takeItem(i))
                self.fix.append(self.points[i])
                del self.points[i]

    def onAddAdjButton(self):
        """ Move selected points to adjusted list
        """
        selected = self.ui.PointsList.selectedItems()
        for item in selected:
            i = self.ui.PointsList.row(item)
            self.ui.AdjustedList.addItem(self.ui.PointsList.takeItem(i))
            self.adj.append(self.points[i])
            del self.points[i]

    def onRemoveFixButton(self):
        """ Move back selected points from fixed list
        """
        selected = self.ui.FixList.selectedItems()
        for item in selected:
            i = self.ui.FixList.row(item)
            self.ui.PointsList.addItem(self.ui.FixList.takeItem(i))
            self.points.append(self.fix[i])
            del self.fix[i]

    def onRemoveAdjButton(self):
        """ Move back selected points from adjusted list
        """
        selected = self.ui.AdjustedList.selectedItems()
        for item in selected:
            i = self.ui.AdjustedList.row(item)
            self.ui.PointsList.addItem(self.ui.AdjustedList.takeItem(i))
            self.points.append(self.adj[i])
            del self.adj[i]

    def onCalcButton(self):
        """ Collect observations and adjust network
        """
        if len(self.adj):
            dimension = int(self.ui.DimensionComboBox.currentText())
            conf = float(self.ui.ConfidenceComboBox.currentText())
            stda = float(self.ui.AngleDevComboBox.currentText())
            stdd = float(self.ui.DistDevMMComboBox.currentText())
            stdd1 = float(self.ui.DistDevMMKMComboBox.currentText())
            g = GamaInterface(dimension, conf, stda, stdd, stdd1)
            # add points to adjustment
            fix_names = []
            adj_names = []
            for fp in self.fix:
                p = get_coord(fp[0])
                g.add_point(p, 'FIX')
                fix_names.append(fp[0])
            for fp in self.adj:
                p = get_coord(fp[0])
                if p is None:
                    p = Point(fp[0])
                g.add_point(p, 'ADJ')
                adj_names.append(fp[0])
            # add observations to adjustment
            fb_list = get_fblist()
            if fb_list is None:
                return None
            for fb in fb_list:
                lay = get_layer_by_name(fb)
                if lay is None:
                    continue
                st = None
                n_ori = 0    # number of orientation directions
                n_adj = 0    # number of adjusted targets
                for feat in lay.getFeatures():
                    pid = feat['point_id']
                    if feat['station'] == 'station':
                        if st is not None:
                            if (n_ori + n_adj == 0) or \
                                (st in fix_names and n_adj == 0):
                                # no adjusted point on known station, remove it
                                g.remove_last_observation(True)
                        st = None
                        n_ori = 0    # number of orientation directions
                        n_adj = 0    # number of adjusted targets
                        if pid in fix_names or pid in adj_names:
                            st = pid
                            o = PolarObservation(pid, feat['station'])
                            o.th = feat['th'] if type(feat['th']) is float else None
                            o.pc = feat['pc'] if type(feat['pc']) is str else None
                            g.add_observation(o)
                            # TODO empty station? without observation
                    else:
                        if st is not None and (pid in fix_names or pid in adj_names):
                            if dimension in [2, 3] and (type(feat['hz']) is float or \
                                type(feat['v']) is float and type(feat['sd']) is float) or \
                                dimension == 1 and type(feat['v']) is float and \
                                type(feat['sd']):
                                o = PolarObservation(pid, None)
                                o.hz = Angle(feat['hz'], 'GON') if type(feat['hz']) is float else None
                                o.v = Angle(feat['v'], 'GON') if type(feat['v']) is float else None
                                if type(feat['sd']) is float and \
                                    (st in adj_names or pid in adj_names):
                                    # add distance if one end is unknown
                                    o.d = Distance(feat['sd'], 'SD')
                                o.th = feat['th'] if type(feat['th']) is float else None
                                o.pc = feat['pc'] if type(feat['pc']) is str else None
                                if o.hz is not None or o.d is not None:
                                    # direction or distance given
                                    g.add_observation(o)
                                    if pid in fix_names:
                                        n_ori += 1
                                    if pid in adj_names:
                                        n_adj += 1
            t = g.adjust()
            if t is None:
                # adjustment failed
                self.ui.ResultTextBrowser.append('gama-local not installed or other runtime error')
            else:
                self.ui.ResultTextBrowser.append(t)
