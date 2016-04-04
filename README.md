## Update point feature class XY coordinates based on new feature class / shapefile

### Description
Sometimes, one might need to update the coordinates of a point feature class based on a new submission by another colleague. 

ESRI has an decent blog post on how to do this in the Field Calculator in ArcMap (https://blogs.esri.com/esri/supportcenter/2011/12/06/how-to-update-the-location-of-a-point-feature-and-its-xy-fields/). However, a major limitation is that the XY needs to be updated in the original feature class XY fields, then updated into the Shape field. A table join to transfer the XY from a new dataset does not work from ArcGIS v10 onwards.

##### In summary:

1) You have one point shapefile / feature class of a new XY coordinates. You want to update the original features in the feature class. They both have a common unique ID field.

2) Use the script will take update the XY geometries of the original feature class based on the new shapefile / feature class.

### Requirements
As this requires some ArcPy functions, ArcGIS needs to be already installed to work.

### Format
The original dataset must be a feature class stored in a file geodatabase. Unfortunately, I can't get it to work in an ArcSDE geodatabase yet. New dataset can be either a feature class or shapefile.

### ArcGIS Tool

I have also created an ArcGIS tool to perform the same function. Place the script and toolbox inside the Toolbox folder somewhere together and add the latter into ArcMap/Catalog ArcToolbox window.
