"""
Objective: Clip feature with boundary and calculate acres of each polygon.
Frank Hutto 2025-01-27
"""
import arcpy

input =arcpy.GetParameterAsText(0)
boundary = arcpy.GetParameterAsText(1)
out= arcpy.GetParameterAsText(2)

def the_clip(input,boundary,out):
    """Clips the input feature class by the boundary feature class"""
    arcpy.analysis.PairwiseClip(
        in_features=input,
        clip_features=boundary,
        out_feature_class=out,
        #cluster_tolerance=None
    )
    return

def make_field(out):
    """checks if field is present if not creates ARCE field"""
    fields =[field.name for field in arcpy.ListFields(out)]
    if "ACRES" not in fields:
        arcpy.management.AddField(
            in_table=out,
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

def calc_geom(out):
    """Calculates the area of a feature in acres"""
    arcpy.management.CalculateGeometryAttributes(
        in_features=out,
        geometry_property="ACRES AREA_GEODESIC",
        length_unit="",
        area_unit="ACRES_US",
        coordinate_system='PROJCS["NAD_1983_UTM_Zone_15N",/GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-93.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
        coordinate_format="SAME_AS_INPUT"
    )
    return

the_clip(input,boundary,out)
make_field(out)
calc_geom(out)
