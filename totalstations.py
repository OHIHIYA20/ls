#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Total station file loader classes for Land Surveying Plug-in for QGIS
    GPL v2.0 license
    Copyright (C) 2014-  DgiKom Kft. http://digikom.hu
    .. moduleauthor::Zoltan Siki <siki@agt.bme.hu>
"""

import re
from base_classes import Angle

class TotalStation(object):
    """
        base class to load different total station data format
    """

    def __init__(self, fname, separator):
        """
            :param fname: input file name (string)
            :param separator: field separator in input (string/regexp???)
        """
        self.fname = fname
        self.separator = re.compile(separator)
        self.fp = None

    def open(self):
        """
            open data set
            return 0 on success -1 on failure
        """
        if self.fp is None:
            try:
                self.fp = open(self.fname, 'r')
            except IOError:
                self.fp = None
                return -1
        return 0

    def close(self):
        """
            close dataset
        """
        if not self.fp is None:
            try:
                self.fp.close()
            except IOError:
                self.fp = None
                pass

    def get_line(self):
        """
            read & split a single line
        """
        buf = self.fp.readline()
        if buf == '':
            # end of file
            return None
        return self.separator.split(buf.strip('\n'))

    def trim_left(self, s, ch):
        """
            strip left part of a string
            :param s: string to legt trim
            :param ch: character to trim
            :return left trimmed string
        """
        s = re.sub('^' + ch + '+', '', s)
        if len(s) == 0:
            s = ch
        return s

    def parse(self):
        """
            parse one line/logical unit of input, implemented in derives classes
        """
        pass

class LeicaGsi(TotalStation):
    """
        read leica GSI 8/16 data
    """
    
    def __init__(self, fname, separator=' '):
        super(LeicaGsi, self).__init__(fname, separator)

    def convert(self, val, unit):
        """
            convert angle to radian, distance to meter
            :param val: value to convert (float)
            :param unit: unit & decimals (int)
            :return converted value
        """
        res = None
        if unit == 0:
            # meter, 3 decomals
            res = val / 1000.0
        elif unit == 1:
            # feet, 3 decimals
            res = val / 1000.0 * 0.3048
        elif unit == 2:
            # gon
            res = Angle(val / 100000.0, 'GON').get_angle('GON')
        elif unit == 3:
            # DEG
            res = Angle(val / 10000.0, 'DEG').get_angle('GON')
        elif unit == 4:
            # DMS
            res = Angle(val / 100000.0, 'PDEG').get_angle('GON')
        elif unit == 5:
            # mil
            res = val / 6400.0 * math.pi * 2
        elif unit == 6:
            # meter, 4 decimals
            res = val / 10000.0
        elif unit == 7:
            # feet, 4 decimals
            res = val / 1000.0 * 0.3048
        elif unit == 8:
            # meter, 5 decimals
            res = val / 100000.0
        return res
            
    def parse_next(self):
        """
            parse single line from input
        """
        if self.fp is None:
            return None
        res = {'station': None}
        buf = self.get_line()
        if buf is None:
            return None
        if len(buf) == 0:
            return {}
        if buf[0][0] == '*':
            buf[0] = buf[0].strip('*')
        for i, val in enumerate(buf):
            item_code = val[0:2]
            if item_code == '11':
                res['point_id'] = self.trim_left(val[7:], '0')
            elif item_code == '21':
                # horizontal angle
                res['hz'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '22':
                # vertical angle
                res['v'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '31':
                # slope distance
                res['sd'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '32':
                # horizontal distance
                res['hd'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '33':
                # vertical distance
                res['vd'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '41':
                # new station
                pass
            elif item_code == '42':
                # station number
                res['point_id'] = self.trim_left(val[7:], '0')
                res['station'] = 'station'
            elif item_code == '43':
                # station height
                res['ih'] = self.convert(float(self.trim_left(val[7:], '0')), 0)
            elif item_code == '71':
                # code (first remark)
                res['code'] = self.trim_left(val[7:], '0')
            elif item_code == '81':
                # easting
                res['e'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '82':
                # northing
                res['n'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '83':
                # elevation
                res['z'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '84':
                # station easting
                res['station_e'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '85':
                # station northing
                res['station_n'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '86':
                # station elevation
                res['station_z'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '87':
                # reflector height
                res['th'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
            elif item_code == '88':
                # station height
                res['ih'] = self.convert(float(self.trim_left(val[7:], '0')), int(val[5]))
        return res

class JobAre(TotalStation):
    """
        Class to import JOB/ARE data from file
    """
    # TODO change parse_next to return a whole record

    def __init__(self, fname, separator='='):
        super(JobAre, self).__init__(fname, separator)
        self.angle_unit = 'PDEG'
        self.distance_unit = 'm'
        self.res = {'station': None}

    def parse_next(self):
        """
            parse single line from input
        """
        if self.fp is None:
            return None
        while True:
            buf = self.get_line()
            if buf is None:
                ret = self.res
                self.res = {}
                if len(ret) > 0:
                    return ret
                else:
                    return None
            if len(buf) < 2:
                continue
            item_code = buf[0].strip()
            if item_code == '2':
                ret = self.res
                self.res = {}
                # station point id
                self.res['point_id'] = buf[1].strip()
                self.res['station'] = 'station'
                if len(ret):
                    return ret
            elif item_code == '3':
                # instrument height
                self.res['ih'] = float(buf[1].strip())
            elif item_code == '4':
                # point code
                self.res['code'] = buf[1].strip()
            elif item_code == '5' or item_code == '62':
                ret = self.res
                self.res = {}
                # target point id
                self.res['point_id'] = buf[1].strip()
                if len(ret):
                    return ret
            elif item_code == '6':
                # target height
                self.res['th'] = float(buf[1].strip())
            elif item_code == '7' or item_code == '21':
                # horizontal angle
                self.res['hz'] = Angle(float(buf[1]), self.angle_unit).get_angle('GON')
            elif item_code == '8':
                # zenit angle
                self.res['v'] = Angle(float(buf[1]), self.angle_unit).get_angle('GON')
            elif item_code == '9':
                # slope distance
                self.res['sd'] = float(buf[1].strip())
            elif item_code == '10':
                # vertical distance
                self.res['vd'] = float(buf[1].strip())
            elif item_code == '11':
                # horizontal distance
                self.res['hd'] = float(buf[1].strip())
            elif item_code == '37':
                # northing
                self.res['n'] = float(buf[1].strip())
            elif item_code == '38':
                # easting
                self.res['e'] = float(buf[1].strip())
            elif item_code == '39':
                # elevation
                self.res['z'] = float(buf[1].strip())

class Sdr(TotalStation):
    """
        Class to import Sokkia field books
    """

    def __init__(self, fname, separator='='):
        super(Sdr, self).__init__(fname, separator)
        self.angle_unit = 'PDEG'
        self.distance_unit = 'm'
        self.coord_order = 'EN'
        self.angle_dir = 'CW'

    def parse_next(self):
        # TODO
        pass

if __name__ == "__main__":
    """
        unit test
    """
    ts = LeicaGsi('samples/kz120125_kzp.gsi', ' ')
    ts.open()
    while True:
        r = ts.parse_next()
        if r is None:
            break
        if len(r) > 0:
            print r
    ts.close()
    #ts = JobAre('test.job', '=')
    #ts.open()
    #while True:
    #    r = ts.parse_next()
    #    if r is None:
    #        break
    #    if len(r) > 0:
    #        print r
