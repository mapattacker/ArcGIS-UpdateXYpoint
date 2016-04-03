import arcpy

#Verified to work for feature classes in file geodatabase and shapefiles.
#It does not work in ArcSDE Geodatabase unofortunately
#################### ENTER VARIABLES ################################
arcpy.env.workspace = arcpy.GetParameterAsText(0)    #Input geodatabase path where original feature class resides
original_FC = arcpy.GetParameterAsText(1)    #Input original feature class name
new_FC = arcpy.GetParameterAsText(2)     #Input path of new feature class (or just feature class name if it is in same geodatabase)
common_attribute = arcpy.GetParameterAsText(3)      #Input common field name for matching between original and new feature classes
#####################################################################


#Create list of XY geometry for each feature
Feature_XY = []
with arcpy.da.SearchCursor(new_FC, [common_attribute, "SHAPE@X", "SHAPE@Y"]) as cur:
    for row in cur:
        Feature_XY.append(row)


#Create SQL expression for defining features to update geometry in original feature class
Feature_List = []
with arcpy.da.SearchCursor(new_FC, [common_attribute]) as cur:
    for row in cur:
        Feature_List.append(row[0])

SQL = """{} IN (""".format(common_attribute) + str(Feature_List) + ")"
SQL_exp = SQL.replace("[","").replace("]","").replace("u","")
print str(SQL_exp) + "\n"


#In original feature class, update XY geometry identified by SQL expression
i = 0
with arcpy.da.Editor(arcpy.env.workspace) as edit:
    with arcpy.da.UpdateCursor(original_FC, [common_attribute, "SHAPE@X", "SHAPE@Y"], SQL_exp) as cur:
        for row in cur:
            print row
            if row[0] == Feature_XY[i][0]:  #if common_attribute is the same
                row[1] = Feature_XY[i][1]       #update geometry X
                row[2] = Feature_XY[i][2]       #update geometry Y
        	i += 1
        	cur.updateRow(row)

arcpy.AddMessage('Points shifted!')
print "points shifted!"
