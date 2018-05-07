from PIL import Image, ImageFilter
import sys
import os, gdal
import urllib, cStringIO


class imgConverter:

    def fileReadIn(file):
       file = cStringIO.StringIO(urllib.urlopen(URL).read()) 
       gdalString = "gdal_translate -of GTiff " + os.path.splitext(os.path.basename(file))[0] + os.path.splitext(os.path.basename(file))[1] + " " + os.path.splitext(os.path.basename(file))[0] + ".tif"

       os.system(gdalString)
