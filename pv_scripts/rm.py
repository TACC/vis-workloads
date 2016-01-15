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
  valRanges = [27,150]
  valRange = valRanges[1]-valRanges[0]
  val = (float(stage+.5)/float(svbGetStagesSize()))*valRange+valRanges[0]
 
  if (geometryLevel == 0):
    isovals = [val]
  else:
    val = 0
    isovals = drange(val,val+50.0,51.0/float(geometryLevel))
    isovals = isovals[:geometryLevel]
  print "isovals: " + str(isovals)

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
    #filename = rm_data_dir+ '/llnl__0270.hdr'
    st_reader = time.time()
    reader = XDMFReader(FileNames=[filename])
    #reader = NrrdReader(FileName=filename)
    reader.UpdatePipeline()
    et_reader = time.time()
    tt_reader = (et_reader-st_reader)

  print "reading file: " + filename
  # reader = NrrdReader( FileName=rm_data_dir+ '/rm_0273.nhdr' )
  # reader = XDMFReader(FileNames=[rm_data_dir + '/rm_0273.xmf'])
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
  Contour1.ComputeScalars = 0
  
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


  contour1Display = GetDisplayProperties(Contour1, view=renderView1)

  # set scalar coloring
  ColorBy(contour1Display, ('POINTS', 'Normals'))

  # rescale color and/or opacity maps used to include current data range
  contour1Display.RescaleTransferFunctionToDataRange(True)

  # get color transfer function/color map for 'Normals'
  normalsLUT = GetColorTransferFunction('Normals')
  normalsLUT.ScalarRangeInitialized = 1.0

  # get opacity transfer function/opacity map for 'Normals'
  normalsPWF = GetOpacityTransferFunction('Normals')
  normalsPWF.ScalarRangeInitialized = 1

  #change array component used for coloring
  normalsLUT.VectorMode = 'Component'

  # Properties modified on normalsPWF
  normalsPWF.Points = [-0.9999991059303284, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

  #change array component used for coloring
  normalsLUT.VectorComponent = 0

  normalsLUT.RGBPoints = [-0.9999991059303284, 0.058823529411764705, 0.0784313725490196, 0.2, -0.6878973245620728, 0.28627450980392155, 0.3803921568627451, 0.8235294117647058, 4.4702373369620574e-07, 0.865003, 0.865003, 0.865003, 1.0, 0.5568627450980392, 0.07450980392156863, 0.0392156862745098]

  #### saving camera placements for all active views

  # current camera placement for oSPRayRendered3DView1
  renderView1.CameraPosition = [-343.804513858627, 484.2377950087568, -331.00118857283326]
  renderView1.CameraFocalPoint = [127.50000000000018, 127.49999999999984, 112.4193172454835]
  renderView1.CameraViewUp = [0.4505229216329572, -0.39806930949541297, -0.799105701344415]
  renderView1.CameraParallelScale = 191.24810607783527



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
