"""

"""
import arcpy
import gc
#Variables*****************************************************
trs_input =arcpy.GetParameterAsText(0)
#**************************************************************
def clear_all():
    """Clear selection for all features"""
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    mp = aprx.activeMap
    try:
        mp.clearSelection()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
#**************************************************************
def select_attribute(var1):
    """SelectByAttribute with split by space to select multiply CLU"""
    try:
        var2 =int(var1)
        arcpy.management.SelectLayerByAttribute(
            in_layer_or_view="PLS Sections",
            selection_type="NEW_SELECTION",
            where_clause=f"twprngsec = {var2}",
            invert_where_clause=None
            )
    except Exception as e:
        print(f"Error setting extent: {e}")
    #********************************
def zoom_to_feature(the_feature):
    """Zoom in on a specific feature in ArcMap.:param the_feature: Name of the layer or feature class to zoom in on. """
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    mp = aprx.activeView
    if not mp.map.listLayers(the_feature):
        raise ValueError(f"Layer '{the_feature}' does not exist in the current project.")
    try:
        mp.camera.setExtent(mp.getLayerExtent(mp.map.listLayers(the_feature)[0]))
    except Exception as e:
        print(f"Error setting extent: {e}")

clear_all()  
select_attribute(trs_input) 
zoom_to_feature("PLS Sections")

gc.collect()
