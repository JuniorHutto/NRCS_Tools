"""
Frank Hutto
This script check to see if ACRES field if not it create one and calucates area in acres
"""
import arcpy
arcpy.ImportToolbox(r"@\Analysis Tools.tbx")

input_feature =arcpy.GetParameterAsText(0)
clip_feature = arcpy.GetParameterAsText(1)
out_feature= arcpy.GetParameterAsText(2)

def the_clip(input_feature,clip_feature,out_feature):
    arcpy.analysis.PairwiseClip(
        in_features=input_feature,
        clip_features=clip_feature,
        out_feature_class=out_feature,
        cluster_tolerance=None
    )
    return

def make_field(out_feature):
    """checks if field is present if not creates FEET   field"""
    fields =[field.name for field in arcpy.ListFields(out_feature)]
    if "ACRES" not in fields:
        arcpy.management.AddField(
            in_table=input_feature,
            field_name="ACRES",
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
def calc_geom(out_feature):
    """Calculates the area of a feature in acres"""
    arcpy.management.CalculateGeometryAttributes(
        in_features=out_feature,
        geometry_property="ACRES AREA_GEODESIC",
        length_unit="",
        area_unit="ACRES_US",
        coordinate_system='PROJCS["NAD_1983_UTM_Zone_15N",/GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-93.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
        coordinate_format="SAME_AS_INPUT"
    )
    return

the_clip(input_feature,clip_feature,out_feature)
make_field(out_feature)
calc_geom(out_feature)
