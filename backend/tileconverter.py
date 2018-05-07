import os, gdal
import sys
import urllib, cStringIO
         
class tileConverter: 
         
    def fileReadIn(file):
        file = cStringIO.StringIO(urllib.urlopen(URL).read())
        inFile = Image.open(file)
      
    def tileImage():
        tile_size_x = 60
        tile_size_y = 60 
    
        ds = gdal.Open(inFile)
        band = ds.GetRasterBand(1)
        xsize = band.XSize
        ysize = band.YSize
    
        for i in range(0, xsize, tile_size_x): 
           for j in range(0, ysize, tile_size_y):
               gdalString = "gdal_translate -of GTIFF -srcwin "+ str(i) + ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + str(inFile) + " " + str(outFile) + str(i) + "_" + str(j) + ".tif"
                os.system(gdalString)


