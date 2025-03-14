import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT")
mp = aprx.activeView

aprx.updateConnectionProperties(None, r'C:\NRCS_GEODB\geodb.gdb')




