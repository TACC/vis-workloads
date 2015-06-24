try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()
import os


bashCommand = "export LD_LIBRARY_PATH=/opt/apps/intel14/netcdf/4.2.1.1/lib:$LD_LIBRARY_PATH"

os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH'] + ':' + "/opt/apps/intel14/netcdf/4.2.1.1/lib"
os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH'] + ':' + "/home/01249/gda/plugins/gdal/lib"
os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH'] + ':' + "/home/01249/gda/plugins/proj-4.9.1/src/.libs"
os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH'] + ':' + "/home/01249/gda/pvospray/pv-4.1/lib/paraview-4.1"

os.system('xterm')

LoadPlugin("/home/01249/gda/plugins/wrf-4.1-mav/libWRFReader.so", False, globals())
print "Happy"

