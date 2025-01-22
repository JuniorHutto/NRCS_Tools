"""
Find CLU tract
input county and clu tract number
sort list (county, zip, real county) some counties are split in ClU data
clear selection
select with input
zoom to selection
changess
    -may need add selected layer if CLU is name someting else ex(mn_CLU)
    -moduels 

Frank Hutto Jan 25
"""
import arcpy
#Variables*****************************************************
cty_input =arcpy.GetParameterAsText(0)
tract_input =arcpy.GetParameterAsText(1) 
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
    """clear selection for all features"""
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    mp = aprx.activeMap
    mp.clearSelection() 
    return()  
#**************************************************************
def select_attribute(var1, var2):
    """SelectByAttribute"""
    arcpy.management.SelectLayerByAttribute(
        in_layer_or_view="CLU",
        selection_type="NEW_SELECTION",
        where_clause=f"county_code = '{var1}' And tract_number = '{var2}'",
        ) 
    return()
#**************************************************************
def zoom_to_feature(the_feature):
    """zoom to selected feature"""
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    mp = aprx.activeView 
    mp.camera.setExtent(mp.getLayerExtent(mp.map.listLayers(the_feature)[0]))
    return()
# calls funtions**************************************************************

if __name__ == "__main__":
    cty_zip, cty_name = sort_list(cty_list, cty_input) 
    clear_all()  
    select_attribute(cty_zip, tract_input) 
    zoom_to_feature("CLU")