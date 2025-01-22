"""
Frank Hutto Dec 2024
-Select feature and geometry type
-calculates acres or feet determined by geometery type
"""
import arcpy
#input varabile ********************************************************
input_feature = arcpy.GetParameterAsText(0)
geo_type = arcpy.GetParameterAsText(1)
#************************************************************************
def make_field(input_feature, geo_type):
    """checks if field is present if not creates FEET or ARCES field"""
    fields =[field.name for field in arcpy.ListFields(input_feature)]
    if "FEET" not in fields and "ACRES" not in fields:
        arcpy.management.AddField(
            in_table=input_feature,
            field_name = "ACRES" if geo_type == "Area" else "FEET",  
            field_type="DOUBLE",
            field_precision=12,
            field_scale=2,
            field_length=None,
            field_alias="",
            field_is_nullable="NULLABLE",
            field_is_required="NON_REQUIRED",
            field_domain=""
        )
    return
#*************************************************************************
def calc_geom(input_feature, geo_type):
    """Calculates the length of a feature in feet or area in acres"""
    arcpy.management.CalculateGeometryAttributes(
        in_features=input_feature,
        geometry_property= "ACRES AREA_GEODESIC" if geo_type == "Area" else "FEET LENGTH_GEODESIC",
        length_unit="" if geo_type == "Area" else "US Survey Feet",
        area_unit="ACRES_US" if geo_type == "Area" else "",
        coordinate_system='PROJCS["NAD_1983_UTM_Zone_15N", GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-93.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
        coordinate_format="SAME_AS_INPUT"
    )
    return
#**************************************************************************
make_field(input_feature, geo_type)
calc_geom(input_feature, geo_type)