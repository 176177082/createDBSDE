#!C:/Python27/ArcGIS10.2/python.exe
#-*- coding:utf-8 -*-
"""
#============================================
#
# Project: createDBSDE
# Name: The file name is main
# Purpose: 
# Auther: Administrator
# Tel: 17372796660
#
#============================================
#
"""

import sys
import arcpy
import datetime
from createDB import createDB

reload(sys)
sys.setdefaultencoding('utf8')


def main():
    rgspath=arcpy.GetParameterAsText(0)
    mapindexpath=arcpy.GetParameterAsText(0)
    ymdhms = datetime.datetime.now().strftime(u"%Y%m%d%H%M%S")
    createDB(rgspath,u"rgs",ymdhms)
    createDB(mapindexpath, u"mapindex", ymdhms)
    return True


if __name__ == "__main__":
    main()