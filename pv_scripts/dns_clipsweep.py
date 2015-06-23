try: paraview.simple
except: from paraview.simple import *
import os
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

data_dir =  path_vars["DNSDATA_DIR"]
print "data_dir:%s" %  data_dir

global Slice1
global reader

valRanges = [1,7679.0]
valRange = valRanges[1]-valRanges[0]

def svbGetStagesSize():
  return 10;

def svbSetup(geometryLevel=1, stage=0):
  val = (float(stage+.5)/float(svbGetStagesSize()))*float(valRange) + float(valRanges[0])
  clipVal = val
  global Clip1
  global reader

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False};

  #valRanges = [-0.03,1.26]
  #valRange = valRanges[1]-valRanges[0]
  #val = (float(stage)/float(svbGetStagesSize()))*valRange + valRanges[0]

  # bounds are same as dimensions.
  #clipRanges = [1,7679]
  #clipRange = clipRanges[1]-clipRanges[0]
  #clipVal = (float(stage)/float(svbGetStagesSize()))*clipRange+clipRanges[0]

  if (stage != 0):  
    ResetCamera()
    Clip1.ClipType.Origin = [clipVal, 1, 1]
    #Contour1.Isosurfaces = [val]
    return returnVals;

  numCells = 0
  numPolys = 0 
  numPoints = 0
  
  #ppmt273_256_256_256_nrrd = NrrdReader( FileName='/scratch/01336/carson/data/RM/ppmt273_256_256_256.nrrd' )
  # reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')
  # reader = XdmfReader( FileName='/work/00401/pnav/workloads/dns/u_0035_pv.xmf')
  reader = XDMFReader(FileNames=[data_dir + '/u_0032_pv.xmf'])
  reader.PointArrayStatus = ['dataset0']
  reader.GridStatus = ['Grid_2']

  Contour1 = Contour(Input=reader)

  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'dataset0']
  #data range for smaller 32 is -.0299 to 1.268
  #valRanges = [-0.03,1.26]
  #valRange = valRanges[1]-valRanges[0]
  #val = (float(stage)/float(svbGetStagesSize()))*valRange/2.0+valRanges[0]
  Contour1.Isosurfaces = [1.0]
  Contour1.ComputeNormals = 1


  Clip1 = Clip(ClipType="Plane")
  Clip1.ClipType.Origin = [1,clipVal, 1]
  Clip1.ClipType.Normal = [0,1,0]
  #Slice1 = Slice( SliceType="Plane" )

  #Slice1.SliceOffsetValues = [0.0]
  #Slice1.SliceType = "Plane"

  #Slice1.SliceType.Origin = [1, 1023.5, 959]
  #Slice1.SliceType.Normal = [1.0, 0.0, 0.0]

  DataRepresentation2 = Show()
  DataRepresentation2.ScaleFactor = 25.5
  DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
  DataRepresentation2.SetRepresentationType('Surface')
  
  ResetCamera()
  renderView1 = GetActiveView()
  renderView1.Background = [0.5529411764705883, 0.5529411764705883, 0.5529411764705883]
  renderView1.CameraPosition = [5630.224162601005, -6026.47810866812, 6733.205518587123]
  renderView1.CameraFocalPoint = [336.5950056411767, 3593.3184025734727, 534.8053287858077]
  renderView1.CameraViewUp = [-0.08525959200958713, 0.5060899960109523, 0.8582562076140161]
  renderView1.CameraParallelScale = 3948.7274848994075
  
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

  return returnVals

def svbRender():
  Render()
