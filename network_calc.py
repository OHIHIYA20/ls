# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'network_calc.ui'
#
# Created: Thu Dec 18 19:26:01 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NetworkCalcDialog(object):
    def setupUi(self, NetworkCalcDialog):
        NetworkCalcDialog.setObjectName(_fromUtf8("NetworkCalcDialog"))
        NetworkCalcDialog.resize(638, 542)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NetworkCalcDialog.sizePolicy().hasHeightForWidth())
        NetworkCalcDialog.setSizePolicy(sizePolicy)
        NetworkCalcDialog.setMinimumSize(QtCore.QSize(638, 542))
        NetworkCalcDialog.setMaximumSize(QtCore.QSize(638, 542))
        NetworkCalcDialog.setWindowTitle(_fromUtf8("Network Adjustment"))
        NetworkCalcDialog.setAccessibleName(_fromUtf8(""))
        NetworkCalcDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.PointsGroup = QtGui.QGroupBox(NetworkCalcDialog)
        self.PointsGroup.setGeometry(QtCore.QRect(10, 10, 401, 311))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsGroup.sizePolicy().hasHeightForWidth())
        self.PointsGroup.setSizePolicy(sizePolicy)
        self.PointsGroup.setObjectName(_fromUtf8("PointsGroup"))
        self.AddFixButton = QtGui.QPushButton(self.PointsGroup)
        self.AddFixButton.setGeometry(QtCore.QRect(160, 50, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddFixButton.sizePolicy().hasHeightForWidth())
        self.AddFixButton.setSizePolicy(sizePolicy)
        self.AddFixButton.setObjectName(_fromUtf8("AddFixButton"))
        self.AddAdjButton = QtGui.QPushButton(self.PointsGroup)
        self.AddAdjButton.setGeometry(QtCore.QRect(160, 200, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddAdjButton.sizePolicy().hasHeightForWidth())
        self.AddAdjButton.setSizePolicy(sizePolicy)
        self.AddAdjButton.setObjectName(_fromUtf8("AddAdjButton"))
        self.RemoveFixButton = QtGui.QPushButton(self.PointsGroup)
        self.RemoveFixButton.setGeometry(QtCore.QRect(160, 90, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveFixButton.sizePolicy().hasHeightForWidth())
        self.RemoveFixButton.setSizePolicy(sizePolicy)
        self.RemoveFixButton.setObjectName(_fromUtf8("RemoveFixButton"))
        self.PointsLabel = QtGui.QLabel(self.PointsGroup)
        self.PointsLabel.setGeometry(QtCore.QRect(10, 20, 121, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsLabel.sizePolicy().hasHeightForWidth())
        self.PointsLabel.setSizePolicy(sizePolicy)
        self.PointsLabel.setObjectName(_fromUtf8("PointsLabel"))
        self.FixLabel = QtGui.QLabel(self.PointsGroup)
        self.FixLabel.setGeometry(QtCore.QRect(260, 20, 121, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FixLabel.sizePolicy().hasHeightForWidth())
        self.FixLabel.setSizePolicy(sizePolicy)
        self.FixLabel.setObjectName(_fromUtf8("FixLabel"))
        self.RemoveAdjButton = QtGui.QPushButton(self.PointsGroup)
        self.RemoveAdjButton.setGeometry(QtCore.QRect(160, 240, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveAdjButton.sizePolicy().hasHeightForWidth())
        self.RemoveAdjButton.setSizePolicy(sizePolicy)
        self.RemoveAdjButton.setObjectName(_fromUtf8("RemoveAdjButton"))
        self.AdjustedLabel = QtGui.QLabel(self.PointsGroup)
        self.AdjustedLabel.setGeometry(QtCore.QRect(260, 170, 141, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AdjustedLabel.sizePolicy().hasHeightForWidth())
        self.AdjustedLabel.setSizePolicy(sizePolicy)
        self.AdjustedLabel.setObjectName(_fromUtf8("AdjustedLabel"))
        self.PointsList = QtGui.QListWidget(self.PointsGroup)
        self.PointsList.setGeometry(QtCore.QRect(10, 40, 131, 261))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsList.sizePolicy().hasHeightForWidth())
        self.PointsList.setSizePolicy(sizePolicy)
        self.PointsList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.PointsList.setObjectName(_fromUtf8("PointsList"))
        self.FixList = QtGui.QListWidget(self.PointsGroup)
        self.FixList.setGeometry(QtCore.QRect(260, 40, 131, 111))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FixList.sizePolicy().hasHeightForWidth())
        self.FixList.setSizePolicy(sizePolicy)
        self.FixList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.FixList.setObjectName(_fromUtf8("FixList"))
        self.AdjustedList = QtGui.QListWidget(self.PointsGroup)
        self.AdjustedList.setGeometry(QtCore.QRect(260, 190, 131, 111))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AdjustedList.sizePolicy().hasHeightForWidth())
        self.AdjustedList.setSizePolicy(sizePolicy)
        self.AdjustedList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.AdjustedList.setObjectName(_fromUtf8("AdjustedList"))
        self.ResetButton = QtGui.QPushButton(NetworkCalcDialog)
        self.ResetButton.setGeometry(QtCore.QRect(440, 510, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        self.ResetButton.setObjectName(_fromUtf8("ResetButton"))
        self.CloseButton = QtGui.QPushButton(NetworkCalcDialog)
        self.CloseButton.setGeometry(QtCore.QRect(540, 510, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.ResultGroup = QtGui.QGroupBox(NetworkCalcDialog)
        self.ResultGroup.setGeometry(QtCore.QRect(10, 330, 621, 161))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultGroup.sizePolicy().hasHeightForWidth())
        self.ResultGroup.setSizePolicy(sizePolicy)
        self.ResultGroup.setObjectName(_fromUtf8("ResultGroup"))
        self.ResultTextBrowser = QtGui.QTextBrowser(self.ResultGroup)
        self.ResultTextBrowser.setGeometry(QtCore.QRect(10, 20, 601, 131))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultTextBrowser.sizePolicy().hasHeightForWidth())
        self.ResultTextBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(11)
        self.ResultTextBrowser.setFont(font)
        self.ResultTextBrowser.setObjectName(_fromUtf8("ResultTextBrowser"))
        self.HelpButton = QtGui.QPushButton(NetworkCalcDialog)
        self.HelpButton.setGeometry(QtCore.QRect(20, 510, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpButton.sizePolicy().hasHeightForWidth())
        self.HelpButton.setSizePolicy(sizePolicy)
        self.HelpButton.setObjectName(_fromUtf8("HelpButton"))
        self.CalcButton = QtGui.QPushButton(NetworkCalcDialog)
        self.CalcButton.setGeometry(QtCore.QRect(340, 510, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalcButton.sizePolicy().hasHeightForWidth())
        self.CalcButton.setSizePolicy(sizePolicy)
        self.CalcButton.setObjectName(_fromUtf8("CalcButton"))
        self.ParametersGroup = QtGui.QGroupBox(NetworkCalcDialog)
        self.ParametersGroup.setGeometry(QtCore.QRect(420, 10, 201, 311))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ParametersGroup.sizePolicy().hasHeightForWidth())
        self.ParametersGroup.setSizePolicy(sizePolicy)
        self.ParametersGroup.setObjectName(_fromUtf8("ParametersGroup"))
        self.ConfidenceComboBox = QtGui.QComboBox(self.ParametersGroup)
        self.ConfidenceComboBox.setGeometry(QtCore.QRect(30, 270, 81, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConfidenceComboBox.sizePolicy().hasHeightForWidth())
        self.ConfidenceComboBox.setSizePolicy(sizePolicy)
        self.ConfidenceComboBox.setObjectName(_fromUtf8("ConfidenceComboBox"))
        self.ConfidenceComboBox.addItem(_fromUtf8(""))
        self.ConfidenceComboBox.addItem(_fromUtf8(""))
        self.ConfidenceLabel = QtGui.QLabel(self.ParametersGroup)
        self.ConfidenceLabel.setGeometry(QtCore.QRect(10, 250, 151, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConfidenceLabel.sizePolicy().hasHeightForWidth())
        self.ConfidenceLabel.setSizePolicy(sizePolicy)
        self.ConfidenceLabel.setObjectName(_fromUtf8("ConfidenceLabel"))
        self.DistDevMMComboBox = QtGui.QComboBox(self.ParametersGroup)
        self.DistDevMMComboBox.setGeometry(QtCore.QRect(30, 180, 81, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DistDevMMComboBox.sizePolicy().hasHeightForWidth())
        self.DistDevMMComboBox.setSizePolicy(sizePolicy)
        self.DistDevMMComboBox.setObjectName(_fromUtf8("DistDevMMComboBox"))
        self.DistDevMMComboBox.addItem(_fromUtf8(""))
        self.DistDevMMComboBox.addItem(_fromUtf8(""))
        self.DistDevMMComboBox.addItem(_fromUtf8(""))
        self.DistDevMMComboBox.addItem(_fromUtf8(""))
        self.DistDevLabel = QtGui.QLabel(self.ParametersGroup)
        self.DistDevLabel.setGeometry(QtCore.QRect(10, 160, 191, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DistDevLabel.sizePolicy().hasHeightForWidth())
        self.DistDevLabel.setSizePolicy(sizePolicy)
        self.DistDevLabel.setObjectName(_fromUtf8("DistDevLabel"))
        self.DistDevMMKMComboBox = QtGui.QComboBox(self.ParametersGroup)
        self.DistDevMMKMComboBox.setGeometry(QtCore.QRect(30, 210, 81, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DistDevMMKMComboBox.sizePolicy().hasHeightForWidth())
        self.DistDevMMKMComboBox.setSizePolicy(sizePolicy)
        self.DistDevMMKMComboBox.setObjectName(_fromUtf8("DistDevMMKMComboBox"))
        self.DistDevMMKMComboBox.addItem(_fromUtf8(""))
        self.DistDevMMKMComboBox.addItem(_fromUtf8(""))
        self.DistDevMMKMComboBox.addItem(_fromUtf8(""))
        self.DistDevMMKMComboBox.addItem(_fromUtf8(""))
        self.DistDevMMLabel = QtGui.QLabel(self.ParametersGroup)
        self.DistDevMMLabel.setGeometry(QtCore.QRect(120, 190, 61, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DistDevMMLabel.sizePolicy().hasHeightForWidth())
        self.DistDevMMLabel.setSizePolicy(sizePolicy)
        self.DistDevMMLabel.setObjectName(_fromUtf8("DistDevMMLabel"))
        self.DistDevMMKMLabel = QtGui.QLabel(self.ParametersGroup)
        self.DistDevMMKMLabel.setGeometry(QtCore.QRect(120, 220, 61, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DistDevMMKMLabel.sizePolicy().hasHeightForWidth())
        self.DistDevMMKMLabel.setSizePolicy(sizePolicy)
        self.DistDevMMKMLabel.setObjectName(_fromUtf8("DistDevMMKMLabel"))
        self.AngleDevComboBox = QtGui.QComboBox(self.ParametersGroup)
        self.AngleDevComboBox.setGeometry(QtCore.QRect(30, 120, 81, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AngleDevComboBox.sizePolicy().hasHeightForWidth())
        self.AngleDevComboBox.setSizePolicy(sizePolicy)
        self.AngleDevComboBox.setObjectName(_fromUtf8("AngleDevComboBox"))
        self.AngleDevComboBox.addItem(_fromUtf8(""))
        self.AngleDevComboBox.addItem(_fromUtf8(""))
        self.AngleDevComboBox.addItem(_fromUtf8(""))
        self.AngleDevComboBox.addItem(_fromUtf8(""))
        self.ZenitDevLabel = QtGui.QLabel(self.ParametersGroup)
        self.ZenitDevLabel.setGeometry(QtCore.QRect(10, 100, 181, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZenitDevLabel.sizePolicy().hasHeightForWidth())
        self.ZenitDevLabel.setSizePolicy(sizePolicy)
        self.ZenitDevLabel.setObjectName(_fromUtf8("ZenitDevLabel"))
        self.DistDevMMLabel_2 = QtGui.QLabel(self.ParametersGroup)
        self.DistDevMMLabel_2.setGeometry(QtCore.QRect(120, 120, 61, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DistDevMMLabel_2.sizePolicy().hasHeightForWidth())
        self.DistDevMMLabel_2.setSizePolicy(sizePolicy)
        self.DistDevMMLabel_2.setObjectName(_fromUtf8("DistDevMMLabel_2"))
        self.DimensionComboBox = QtGui.QComboBox(self.ParametersGroup)
        self.DimensionComboBox.setGeometry(QtCore.QRect(30, 60, 81, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DimensionComboBox.sizePolicy().hasHeightForWidth())
        self.DimensionComboBox.setSizePolicy(sizePolicy)
        self.DimensionComboBox.setObjectName(_fromUtf8("DimensionComboBox"))
        self.DimensionComboBox.addItem(_fromUtf8(""))
        self.DimensionComboBox.addItem(_fromUtf8(""))
        self.DimensionComboBox.addItem(_fromUtf8(""))
        self.ZenitDevLabel_2 = QtGui.QLabel(self.ParametersGroup)
        self.ZenitDevLabel_2.setGeometry(QtCore.QRect(10, 40, 181, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZenitDevLabel_2.sizePolicy().hasHeightForWidth())
        self.ZenitDevLabel_2.setSizePolicy(sizePolicy)
        self.ZenitDevLabel_2.setObjectName(_fromUtf8("ZenitDevLabel_2"))

        self.retranslateUi(NetworkCalcDialog)
        QtCore.QMetaObject.connectSlotsByName(NetworkCalcDialog)
        NetworkCalcDialog.setTabOrder(self.PointsList, self.AddFixButton)
        NetworkCalcDialog.setTabOrder(self.AddFixButton, self.RemoveFixButton)
        NetworkCalcDialog.setTabOrder(self.RemoveFixButton, self.AddAdjButton)
        NetworkCalcDialog.setTabOrder(self.AddAdjButton, self.RemoveAdjButton)
        NetworkCalcDialog.setTabOrder(self.RemoveAdjButton, self.FixList)
        NetworkCalcDialog.setTabOrder(self.FixList, self.AdjustedList)
        NetworkCalcDialog.setTabOrder(self.AdjustedList, self.DimensionComboBox)
        NetworkCalcDialog.setTabOrder(self.DimensionComboBox, self.AngleDevComboBox)
        NetworkCalcDialog.setTabOrder(self.AngleDevComboBox, self.DistDevMMComboBox)
        NetworkCalcDialog.setTabOrder(self.DistDevMMComboBox, self.DistDevMMKMComboBox)
        NetworkCalcDialog.setTabOrder(self.DistDevMMKMComboBox, self.ConfidenceComboBox)
        NetworkCalcDialog.setTabOrder(self.ConfidenceComboBox, self.ResultTextBrowser)
        NetworkCalcDialog.setTabOrder(self.ResultTextBrowser, self.HelpButton)
        NetworkCalcDialog.setTabOrder(self.HelpButton, self.CalcButton)
        NetworkCalcDialog.setTabOrder(self.CalcButton, self.ResetButton)
        NetworkCalcDialog.setTabOrder(self.ResetButton, self.CloseButton)

    def retranslateUi(self, NetworkCalcDialog):
        self.PointsGroup.setTitle(QtGui.QApplication.translate("NetworkCalcDialog", "Points", None, QtGui.QApplication.UnicodeUTF8))
        self.AddFixButton.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Add >", None, QtGui.QApplication.UnicodeUTF8))
        self.AddAdjButton.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Add >", None, QtGui.QApplication.UnicodeUTF8))
        self.RemoveFixButton.setText(QtGui.QApplication.translate("NetworkCalcDialog", "< Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.PointsLabel.setText(QtGui.QApplication.translate("NetworkCalcDialog", "List of Points", None, QtGui.QApplication.UnicodeUTF8))
        self.FixLabel.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Fix Points", None, QtGui.QApplication.UnicodeUTF8))
        self.RemoveAdjButton.setText(QtGui.QApplication.translate("NetworkCalcDialog", "< Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.AdjustedLabel.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Adjusted Points", None, QtGui.QApplication.UnicodeUTF8))
        self.ResetButton.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.CloseButton.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.ResultGroup.setTitle(QtGui.QApplication.translate("NetworkCalcDialog", "Result of Calculations", None, QtGui.QApplication.UnicodeUTF8))
        self.HelpButton.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.CalcButton.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.ParametersGroup.setTitle(QtGui.QApplication.translate("NetworkCalcDialog", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.ConfidenceComboBox.setItemText(0, QtGui.QApplication.translate("NetworkCalcDialog", "0.95", None, QtGui.QApplication.UnicodeUTF8))
        self.ConfidenceComboBox.setItemText(1, QtGui.QApplication.translate("NetworkCalcDialog", "0.997", None, QtGui.QApplication.UnicodeUTF8))
        self.ConfidenceLabel.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Confidence Level", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMComboBox.setItemText(0, QtGui.QApplication.translate("NetworkCalcDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMComboBox.setItemText(1, QtGui.QApplication.translate("NetworkCalcDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMComboBox.setItemText(2, QtGui.QApplication.translate("NetworkCalcDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMComboBox.setItemText(3, QtGui.QApplication.translate("NetworkCalcDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevLabel.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Distance standard deviation", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMKMComboBox.setItemText(0, QtGui.QApplication.translate("NetworkCalcDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMKMComboBox.setItemText(1, QtGui.QApplication.translate("NetworkCalcDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMKMComboBox.setItemText(2, QtGui.QApplication.translate("NetworkCalcDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMKMComboBox.setItemText(3, QtGui.QApplication.translate("NetworkCalcDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMLabel.setText(QtGui.QApplication.translate("NetworkCalcDialog", "[mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMKMLabel.setText(QtGui.QApplication.translate("NetworkCalcDialog", "[mm/km]", None, QtGui.QApplication.UnicodeUTF8))
        self.AngleDevComboBox.setItemText(0, QtGui.QApplication.translate("NetworkCalcDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.AngleDevComboBox.setItemText(1, QtGui.QApplication.translate("NetworkCalcDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.AngleDevComboBox.setItemText(2, QtGui.QApplication.translate("NetworkCalcDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.AngleDevComboBox.setItemText(3, QtGui.QApplication.translate("NetworkCalcDialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.ZenitDevLabel.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Angle standard deviation", None, QtGui.QApplication.UnicodeUTF8))
        self.DistDevMMLabel_2.setText(QtGui.QApplication.translate("NetworkCalcDialog", "[cc]", None, QtGui.QApplication.UnicodeUTF8))
        self.DimensionComboBox.setItemText(0, QtGui.QApplication.translate("NetworkCalcDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.DimensionComboBox.setItemText(1, QtGui.QApplication.translate("NetworkCalcDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.DimensionComboBox.setItemText(2, QtGui.QApplication.translate("NetworkCalcDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.ZenitDevLabel_2.setText(QtGui.QApplication.translate("NetworkCalcDialog", "Dimension", None, QtGui.QApplication.UnicodeUTF8))

