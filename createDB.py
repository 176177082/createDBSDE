#!C:/Python27/ArcGIS10.2/python.exe
#-*- coding:utf-8 -*-
"""
#============================================
#
# Project: mmanagecelery
# Name: The file name is createDB
# Purpose: 
# Auther: Administrator
# Tel: 17372796660
#
#============================================
#
"""

import arcpy
import os
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf8')


def createDB(gdbpath,datatype):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    ymd=datetime.datetime.now().strftime(u"%Y%m%d%H")
    authorization_file=os.path.join(SCRIPT_DIR,u"server10.2.ecp")
    database_name=datatype+ymd
    arcpy.AddMessage(database_name)
    arcpy.CreateEnterpriseGeodatabase_management(database_platform=u"PostgreSQL", instance_name=u"localhost",
                                                 database_name=database_name, account_authentication=u"DATABASE_AUTH",
                                                 database_admin=u"postgres", database_admin_password=u"postgres123",
                                                 sde_schema=u"SDE_SCHEMA", gdb_admin_name=u"sde",
                                                 gdb_admin_password=u"sde", tablespace_name=u"#",
                                                 authorization_file=authorization_file)

    connsdepath=os.path.join(os.path.dirname(SCRIPT_DIR))
    connsde=datatype+ymd+u".sde"
    arcpy.AddMessage(connsde)
    conn = {}
    conn[u"out_folder_path"] = connsdepath
    conn[u"out_name"] = connsde
    conn[u"database_platform"] = u"PostgreSQL"
    conn[u"instance"] = u"localhost"
    conn[u"account_authentication"] = u"DATABASE_AUTH"
    conn[u"database"] = database_name
    conn[u"username"] = u"sde"
    conn[u"password"] = u"sde"
    conn[u"save_user_pass"] = u"SAVE_USERNAME"
    arcpy.CreateDatabaseConnection_management(**conn)

    arcpy.env.workspace = gdbpath
    sdepath=os.path.join(SCRIPT_DIR, connsde)
    for ds in arcpy.ListDatasets(feature_type='feature') + ['']:
        dspath=os.path.join(gdbpath,ds)
        arcpy.Copy_management(dspath,sdepath)

    return True


if __name__ == "__main__":
    createDB()