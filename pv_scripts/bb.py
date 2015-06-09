try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()
import os

LoadPlugin("/home/01249/gda/plugins/wrf-4.1-mav/libWRFReader.so", False, globals())
print "Happy"

