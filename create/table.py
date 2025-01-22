import arcpy
import gc
import os
#variables********************************************************************************
fc = "FieldChecks"
selectLayer = "CLU"
NameInput = arcpy.GetParameterAsText(0)
CoDi={'Aitkin':'001','Anoka':'003','Becker':'005','Beltrami':'007',
        'Benton':'009','Big Stone':'011','Blue Earth':'013','Brown':'015',
        'Carlton':'017','Carver':'019','Cass':'021','Chippewa':'023',
        'Chisago':'025','Clay':'027','Clearwater':'029','Cook':'031',
        'Cottonwood':'033','Crow Wing':'035','Dakota':'037','Dodge':'039',
        'Douglas':'041','Faribault':'043','Fillmore':'045','Freeborn':'047',
        'Goodhue':'049','Grant':'051','Hennepin':'053','Houston':'055',
        'Hubbard':'057','Isanti':'059','Itasca':'061','Jackson':'063',
        'Kanabec':'065','Kandiyohi':'067','Kittson':'069','Koochiching':'071',
        'Lac Qui Parle':'073','Lake':'075','Lake of the Woods':'077','Le Sueur':'079',
        'Lincoln':'081','Lyon':'083','Mahnomen':'087','Marshall':'089',
        'Martin':'091','McLeod':'085','Meeker':'093','Mille Lacs':'095',
        'Morrison':'097','Mower':'099','Murray':'101','Nicollet':'103',
        'Nobles':'105','Norman':'107','Olmsted':'109','Otter Tail':'111',
        'Pennington':'113','Pine':'115','Pipestone':'117','Polk':'119','Pope':'121',
        'Ramsey':'123','Red Lake':'125','Redwood':'127','Renville':'129',
        'Rice':'131','Rock':'133','Roseau':'135','Scott':'139',
        'Sherburne':'141','Sibley':'143','St. Louis':'137','Stearns':'145',
        'Steele':'147','Stevens':'149','Swift':'151','Todd':'153',
        'Traverse':'155','Wabasha':'157','Wadena':'159','Waseca':'161',
        'Washington':'163','Watonwan':'165','Wilkin':'167','Winona':'169',
        'Wright':'171','Yellow Medicine':'173',
        }

#*****************************************************************************************
def clear_all():
    """Clear selection for all features"""
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    mp = aprx.activeMap
    try:
        mp.clearSelection()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
#*********************************************************************************************
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view=selectLayer,
    selection_type="CLEAR_SELECTION",
    where_clause="",
    )
with arcpy.da.SearchCursor(fc,['County','Tract','Field'])as cursor:
    for row in cursor:
        cty =row[0]
        tract = row[1]
        field = row[2]
        fips = CoDi[cty]
        arcpy.management.SelectLayerByAttribute(
        in_layer_or_view=selectLayer,
        selection_type="ADD_TO_SELECTION",
        where_clause=f"county_code = '{fips}' And tract_number = '{tract}'And clu_number ='{field}'",
        )
   
#add layer
DefaultPath = "\Default.gdb"
fullPath = os.path.join(DefaultPath, NameInput)  
arcpy.conversion.ExportFeatures(in_features="CLU",out_features= NameInput)

# Call Functions ***********************************************************************************
clear_all()
gc.collect()
