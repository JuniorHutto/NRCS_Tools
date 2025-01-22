"""
Find CLU tract
-input county and clu tract number
-sort list (county, zip, real county) some counties are split in ClU data
-clear selection
-select with input
-zoom to selection
-export radio button check will export
-path selects geodatabase
Frank Hutto Jan 25
"""
import arcpy
import gc
#Variables*****************************************************
cty_input =arcpy.GetParameterAsText(0)
tract_input =arcpy.GetParameterAsText(1)
export_input =arcpy.GetParameter(2)
path_input =arcpy.GetParameterAsText(3)
cty_list =[('Aitkin', '001', 'Aitkin'),('Anoka', '003', 'Anoka'),('Becker', '005', 'Becker'),('Beltrami', '007', 'Beltrami'),
('Benton', '009', 'Benton'),('Big Stone', '011', 'Big Stone'),('Blue Earth', '013', 'Blue Earth'),('Brown', '015', 'Brown'),
('Carlton', '017', 'Carlton'),('Carver', '019', 'Carver'),('Cass', '021', 'Cass'),('Chippewa', '023', 'Chippewa'),
('Chisago', '025', 'Chisago'),('Clay', '027', 'Clay'),('Clearwater', '029', 'Clearwater'),('Cook', '031', 'Cook'),
('Cottonwood', '033', 'Cottonwood'),('Crow Wing', '035', 'Crow Wing'),('Dakota', '037', 'Dakota'),('Dodge', '039', 'Dodge'),
('Douglas', '041', 'Douglas'),('Faribault', '043', 'Faribault'),('Fillmore', '045', 'Fillmore'),('Freeborn', '047', 'Freeborn'),
('Goodhue', '049', 'Goodhue'),('Grant', '051', 'Grant'),('Hennepin', '053', 'Hennepin'),('Houston', '055', 'Houston'),('Hubbard', '057', 'Hubbard'),
('Isanti', '059', 'Isanti'),('Itasca', '061', 'Itasca'),('Jackson', '063', 'Jackson'),('Kanabec', '065', 'Kanabec'),('Kandiyohi', '067', 'Kandiyohi'),
('Kittson', '069', 'Kittson'),('Koochiching', '071', 'Koochiching'),('Lac Qui Parle', '073', 'Lac Qui Parle'),('Lake', '075', 'Lake'),
('Lake of the Woods', '077', 'Lake of the Woods'),('Le Sueur', '079', 'Le Sueur'),('Lincoln', '081', 'Lincoln'),('Lyon', '083', 'Lyon'),
('Mahnomen', '087', 'Mahnomen'),('Marshall', '089', 'Marshall'),('Martin', '091', 'Martin'),('McLeod', '085', 'McLeod'),('Meeker', '093', 'Meeker'),
('Mille Lacs', '095', 'Mille Lacs'),('Morrison', '097', 'Morrison'),('Mower', '099', 'Mower'),('Murray', '101', 'Murray'),
('Nicollet', '103', 'Nicollet'),('Nobles', '105', 'Nobles'),('Norman', '107', 'Norman'),('Olmsted', '109', 'Olmsted'),
('East Otter Tail', '111', 'Otter Tail'),('West Otter Tail', '112', 'Otter Tail'),('Pennington', '113', 'Pennington'),('Pine', '115', 'Pine'),
('Pipestone', '117', 'Pipestone'),('East Polk', '119', 'Polk'),('West Polk', '120', 'Polk'),('Pope', '121', 'Pope'),('Ramsey', '123', 'Ramsey'),
('Red Lake', '125', 'Red Lake'),('Redwood', '127', 'Redwood'),('Renville', '129', 'Renville'),('Rice', '131', 'Rice'),('Rock', '133', 'Rock'),
('Roseau', '135', 'Roseau'),('Scott', '139', 'Scott'),('Sherburne', '141', 'Sherburne'),('Sibley', '143', 'Sibley'),('North St. Louis', '137', 'St. Louis'),
('South St. Louis', '138', 'St. Louis'),('Stearns', '145', 'Stearns'),('Steele', '147', 'Steele'),('Stevens', '149', 'Stevens'),('Swift', '151', 'Swift'),
('Todd', '153', 'Todd'),('Traverse', '155', 'Traverse'),('Wabasha', '157', 'Wabasha'),('Wadena', '159', 'Wadena'),('Waseca', '161', 'Waseca'),
('Washington', '163', 'Washington'),('Watonwan', '165', 'Watonwan'),('Wilkin', '167', 'Wilkin'),('Winona', '169', 'Winona'),('Wright', '171', 'Wright'),
('Yellow Medicine', '173', 'Yellow Medicine'),
]
#**************************************************************
def sort_list(cty_list,cty_input):
    """sort the list"""
    for (field01, field02, field03) in cty_list:
        if field01 == cty_input:
            cty_zip = field02
            cty_name = field03
    return(cty_zip,cty_name)       
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
def select_attribute(var1, var2):
    """SelectByAttribute with split by space to select multiply CLU"""
    try:
        sp_var2 = var2.split()
        for var0 in sp_var2:
            arcpy.management.SelectLayerByAttribute(
            in_layer_or_view="CLU",
            selection_type="ADD_TO_SELECTION",
            where_clause=f"county_code = '{var1}' And tract_number = '{var0}'",
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
#***************************************************************
def export_select(the_path):
    """export the selected features to geodatabase"""
    try:
        arcpy.conversion.ExportFeatures(
            in_features="CLU",
            out_features=the_path,
            where_clause="",
            use_field_alias_as_name="NOT_USE_ALIAS",
            field_mapping='clu_identifier "clu_identifier" true true false 36 Text 0 0,First,#,CLU,clu_identifier,0,35;clu_number "clu_number" true true false 7 Text 0 0,First,#,CLU,clu_number,0,6;tract_number "tract_number" true true false 7 Text 0 0,First,#,CLU,tract_number,0,6;farm_number "farm_number" true true false 7 Text 0 0,First,#,CLU,farm_number,0,6;clu_classification_code "clu_classification_code" true true false 2 Text 0 0,First,#,CLU,clu_classification_code,0,1;clu_calculated_acreage "clu_calculated_acreage" true true false 0 Double 0 0,First,#,CLU,clu_calculated_acreage,-1,-1;highly_erodible_land_type_code "highly_erodible_land_type_code" true true false 4 Text 0 0,First,#,CLU,highly_erodible_land_type_code,0,3;state_code "state_code" true true false 2 Text 0 0,First,#,CLU,state_code,0,1;county_code "county_code" true true false 3 Text 0 0,First,#,CLU,county_code,0,2;data_source_site_identifier "data_source_site_identifier" true true false 0 Short 0 0,First,#,CLU,data_source_site_identifier,-1,-1;creation_date "creation_date" true true false 29 Date 0 0,First,#,CLU,creation_date,-1,-1;last_change_date "last_change_date" true true false 29 Date 0 0,First,#,CLU,last_change_date,-1,-1;data_source "data_source" true true false 20 Text 0 0,First,#,CLU,data_source,0,19;admin_state "admin_state" true true false 2 Text 0 0,First,#,CLU,admin_state,0,1;admin_county "admin_county" true true false 3 Text 0 0,First,#,CLU,admin_county,0,2;cropland_indicator_3cm "cropland_indicator_3CM" true true false 0 Short 0 0,First,#,CLU,cropland_indicator_3cm,-1,-1;sap_crp "sap_crp" true true false 0 Short 0 0,First,#,CLU,sap_crp,-1,-1;clu_status "clu_status" true true false 30 Text 0 0,First,#,CLU,clu_status,0,29;cdist_fips "cdist_fips" true true false 4 Text 0 0,First,#,CLU,cdist_fips,0,3;edit_reason "edit_reason" true true false 60 Text 0 0,First,#,CLU,edit_reason,0,59;clu_alt_id "clu_alt_id" true true false 38 Guid 0 0,First,#,CLU,clu_alt_id,-1,-1;last_chg_user_nm "last_chg_user_nm" true true false 50 Text 0 0,First,#,CLU,last_chg_user_nm,0,49;state_ansi_code "state_ansi_code" true true false 2 Text 0 0,First,#,CLU,state_ansi_code,0,1;county_ansi_code "county_ansi_code" true true false 3 Text 0 0,First,#,CLU,county_ansi_code,0,2;SHAPE__Length "SHAPE__Length" false true true 0 Double 0 0,First,#,CLU,SHAPE__Length,-1,-1;SHAPE__Area "SHAPE__Area" false true true 0 Double 0 0,First,#,CLU,SHAPE__Area,-1,-1;comments "comments" true true false 80 Text 0 0,First,#,CLU,comments,0,79',
            sort_field=None
        )
    except Exception as e:
        print(f"An error occurred: {str(e)}")
# funtions calls**************************************************************
cty_zip, cty_name = sort_list(cty_list, cty_input) 
clear_all()  
select_attribute(cty_zip, tract_input) 
zoom_to_feature("CLU")
if export_input==True:export_select(path_input)
gc.collect()
