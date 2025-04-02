import arcpy

# Set the path to your local Geodatabase file (.gdb) https://gis-states.sc.egov.usda.gov/server/rest/services/Hosted/mn_clu_a/FeatureServer
gdb_path = r"C:\NRCS_GEODB\geodb.gdb"

# Set the name of the feature class or table that corresponds to the broken FeatureServer layer
feature_class_name = "CLU"

# Set the name of the broken FeatureServer layer
fs_layer_name = "CLU"

# Disconnect from online data source
arcpy.FeatureServer.Disconnect(fs_layer_name)

# Create a new feature server with local Geodatabase as data source
https://gis-states.sc.egov.usda.gov/server/rest/services/Hosted/mn_clu_a/FeatureServer.Create(fs_layer_name, gdb_path, feature_class_name)




