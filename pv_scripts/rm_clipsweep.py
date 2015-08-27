try: paraview.simple
except: from paraview.simple import *
import os
import time
#read in paths from the environment variables bash script generate by cmake
dir = os.path.dirname( os.path.dirname(os.path.abspath(__file__)))
pathsfile = os.path.join(dir,'paths.sh')
path_vars = dict()

with open(pathsfile) as f:
    print f
    next(f)
    for line in f:
        print line
        eq_index = line.find('=')
        var_name = line[:eq_index].strip()
        paths = line[eq_index + 1:].strip()
        path_vars[var_name] = paths

rm_data_dir =  path_vars["RMDATA_DIR"]
print "rm_data_dir:%s" %  rm_data_dir


valRanges = [0,2047]
valRange = valRanges[1]-valRanges[0]

#global Slice1
#global reader

def svbGetStagesSize():
  return 5;

def svbSetup(geometryLevel=1, stage=0):
  #global Clip1
  val = (float(stage+.5)/float(svbGetStagesSize()))*valRange+valRanges[0]
  clipVal = val
  print "clipVal: " + str(clipVal)
  global Clip1
  global reader

  numCells = 0
  numPolys = 0 
  numPoints = 0

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':0.0, 'tt_filter':0.0}; 
  contour_values = []
  for i in range(geometryLevel):
    cval = (i+1) *(255.0/(geometryLevel+1))
    contour_values.append(cval)

  #clipVal = (float(stage)/float(svbGetStagesSize()))*2045+1
  if (stage != 0):
    #ResetCamera()
    st_filter = time.time()
    Clip1.ClipType.Origin = [clipVal, 1023.5, 959]
    Clip1.UpdatePipeline()
    et_filter = time.time()
    tt_filter = (et_filter - st_filter)
    returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':0, 'tt_filter':tt_filter};
    return returnVals;


  #contour_values = [23,30,40,50,60,70,80,90,100,110]
  #contour_values = contour_values[:geometryLevel]
  #print "contour_values: " + str(contour_values)
  st_reader = time.time()
  if (geometryLevel == 0):
    reader = NrrdReader( FileName=rm_data_dir+ '/ppmt273_256_256_256.nrrd' )
  else:
    reader = XDMFReader(FileNames=[rm_data_dir + '/rm_0273.xmf'])
  #ppmt273_256_256_256_nrrd = NrrdReader( FileName='/scratch/01336/carson/data/RM/ppmt273_256_256_256.nrrd' )
  #reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')
  # reader = NrrdReader( FileName=rm_data_dir+ '/ppmt273_256_256_256.nrrd' )
  # reader = NrrdReader( FileName=rm_data_dir+ '/rm_0273.nhdr' )
  reader.UpdatePipeline()
  et_reader = time.time()
  tt_reader = (et_reader - st_reader)

  st_filter = time.time() 
  Contour1 = Contour(Input=reader)

  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'ImageFile']
  val = (float(stage)/float(svbGetStagesSize()))*255.0
  #Contour1.Isosurfaces = [125.0]
  Contour1.Isosurfaces = contour_values
  Contour1.ComputeNormals = 1
  Contour1.ComputeScalars = 1

  lut = imageFileLUT = GetColorTransferFunction('ImageFile')
  lut.RescaleTransferFunction(0,250)

  #clipVal = (float(stage)/float(svbGetStagesSize()))*2046+1
  Clip1 = Clip(ClipType="Plane")
  Clip1.ClipType.Origin = [clipVal, 1023.5, 959]
  Clip1.ClipType.Normal = [-1,0,0]
  #Slice1 = Slice( SliceType="Plane" )

  #Slice1.SliceOffsetValues = [0.0]
  #Slice1.SliceType = "Plane"

  #Slice1.SliceType.Origin = [1, 1023.5, 959]
  #Slice1.SliceType.Normal = [1.0, 0.0, 0.0]
  Contour1.UpdatePipeline()
  Clip1.UpdatePipeline()
  et_filter = time.time()
  tt_filter = (et_filter - st_filter)

  rep = Show()
  rep.LookupTable = lut
  imageFilePWF = GetOpacityTransferFunction('ImageFile')
  #DataRepresentation2.ScaleFactor = 25.5
  #rep.SelectionPointFieldDataArrayName = 'Normals'
  rep.ColorArrayName = ['POINTS','ImageFile']
  rep.SetRepresentationType('Surface')
  
  # ResetCamera()
  renderView1 = GetActiveView()
  renderView1.CameraPosition = [582.5678621725423, 464.5664327088711, 765.7235282760473]
  renderView1.CameraFocalPoint = [127.50000000000001, 127.50000000000006, 127.50000000000001]
  renderView1.CameraViewUp = [-0.08930979131282728, 0.9056097848422845, -0.4146018316090396]
  renderView1.CameraParallelScale = 220.83647796503186
  renderView1.Background = [1,1,1]
  ResetCamera()
  #cam = GetActiveCamera()
  #cam.Roll(90)
  #cam.Elevation(65)
  #cam.Azimuth(-20)

  #numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  #numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  #numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  #print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  #print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  #print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))
  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
  return returnVals

def svbRender():
  Render()
