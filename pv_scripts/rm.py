try: paraview.simple
except: from paraview.simple import *
import os
import time
#read in paths from the environment variables bash script generate by cmake
dir = os.path.dirname( os.path.dirname(os.path.abspath(__file__)))
pathsfile = os.path.join(dir,'paths.sh')
path_vars = dict()

with open(pathsfile) as f:
    #print f
    next(f)
    for line in f:
        #print line
        eq_index = line.find('=')
        var_name = line[:eq_index].strip()
        paths = line[eq_index + 1:].strip()
        path_vars[var_name] = paths


rm_data_dir =  path_vars["RMDATA_DIR"]
print "rm_data_dir:%s" %  rm_data_dir


def drange(start,stop,step):
  vals = []
  v = start
  while v < stop:
    vals.append(v)
    v+=step
  return vals


def svbGetStagesSize():
  return 1;

def svbSetup(geometryLevel=1, stage=0):

  global Contour1
  global reader
  
  numCells = 0
  numPolys = 0
  numPoints = 0

  returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':True, 'tt_reader':0, 'tt_filter':0};
  valRanges = [0,200]
  valRange = valRanges[1]-valRanges[0]
  val = (float(stage+.5)/float(svbGetStagesSize()))*valRange+valRanges[0]
 
  if (geometryLevel == 0):
    isovals = [val]
  else:
    isovals = drange(val,val+50.0,51.0/float(geometryLevel))
    isovals = isovals[:geometryLevel]
  print "isosweep vals: " + str(isovals)

  #print "h"
  #print(rm_data_dir+"/rm_0273.nhdr")
  filename = ""
  if (geometryLevel == 0):
    filename = rm_data_dir+ '/ppmt273_256_256_256.nrrd' 
    st_reader = time.time() 
    reader = NrrdReader( FileName=filename)
    reader.UpdatePipeline()
    et_reader = time.time()
    tt_reader = time.time()
  else:
    filename = rm_data_dir+ '/rm_0273.xmf'
    st_reader = time.time()
    reader = XDMFReader(FileNames=[filename])
    reader.UpdatePipeline()
    et_reader = time.time()
    tt_reader = (et_reader-st_reader)

  print "reading file: " + filename
  # reader = NrrdReader( FileName=rm_data_dir+ '/rm_0273.nhdr' )
  # reader = XDMFReader(FileNames=[rm_data_dir + '/rm_0202.xmf'])
  # reader = NrrdReader( FileName=rm_data_dir+ '/ppmt273_256_256_256.nrrd' )  
  # reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')

  st_filter = time.time()
  Contour1 = Contour(Input=reader)

  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'ImageFile']
  Contour1.Isosurfaces = isovals
  # Contour1.Isosurfaces = [125.0]
  Contour1.PointMergeMethod = 'Uniform Binning'
  Contour1.ComputeNormals = 1
  Contour1.ComputeScalars = 1
  
  #just checking if Update will work here
  Contour1.UpdatePipeline()
  et_filter = time.time()
  tt_filter = (et_filter-st_filter)
  lut = imageFileLUT = GetColorTransferFunction('ImageFile')
  lut.RescaleTransferFunction(0,250)
  rep = Show()
  rep.LookupTable = lut
  imageFilePWF = GetOpacityTransferFunction('ImageFile')
  rep.ColorArrayName = ['POINTS','ImageFile']
  rep.SetRepresentationType('Surface')
  
  renderView1 = GetActiveView()
  #displayProperties = GetDisplayProperties(Contour1, renderView1)
  #displayProperties.RescaleTransferFunctionToDataRange(True)

  renderView1.CameraPosition = [582.5678621725423, 464.5664327088711, 765.7235282760473]
  renderView1.CameraFocalPoint = [127.50000000000001, 127.50000000000006, 127.50000000000001]
  renderView1.CameraViewUp = [-0.08930979131282728, 0.9056097848422845, -0.4146018316090396]
  renderView1.CameraParallelScale = 220.83647796503186
  renderView1.Background = [1,1,1]
  ResetCamera()
  returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':True, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))
  return returnVals

def svbRender():
  Render()
