"""Upload function"""
from qgis.core import QgsProject, QgsVectorFileWriter
import tempfile
import os
import geopandas as gpd

def upload(layer, targetschema, target_table, engine, mode):
    # get layer from QGIS Project
    lyr = layer

    # write as geojson in temporary folder
    with tempfile.TemporaryDirectory() as temp_dir:
        # create output path
        output_geojson_path = os.path.join(temp_dir, 'output_layer.geojson')
        
        error = QgsVectorFileWriter.writeAsVectorFormat(
                lyr,
                output_geojson_path,
                'utf-8',  # encoding
                lyr.crs(),  # coordinatesystem
                'GeoJSON'  # format
            )
            
        # upload geodataframe to postgis
        gdf = gpd.read_file(output_geojson_path)
        gdf = gdf.to_crs("EPSG:25832")
        gdf = gdf.rename_geometry('geom')
        gdf.to_postgis(target_table, con=engine, schema=targetschema, if_exists=mode, index=False)
