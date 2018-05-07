from PIL import Image, ImageFilter
import sys
import os, gdal
import urllib, cStringIO

class imgConverter:

    def fileReadIn(file):

       file = cStringIO.StringIO(urllib.urlopen(URL).read())
       inFile = Image.open(file)

    def convertToGeoTiff():

       inFile = Image.open(file)
       gdalString = "gdal_translate " + str(inFile) + " " + "-of GTiff " + str(inFile) + ".tif"
       os.system(gdalString)
