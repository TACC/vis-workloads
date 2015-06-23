try: paraview.simple
except: from paraview.simple import *
import os
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


global Slice1
global reader

def svbGetStagesSize():
  return 10;

def svbSetup(geometryLevel=1, stage=0):
  global Clip1
  global reader

  numCells = 0
  numPolys = 0 
  numPoints = 0

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False};


  clipVal = (float(stage)/float(svbGetStagesSize()))*2045+1
  if (stage != 0):  
    ResetCamera()
    Clip1.ClipType.Origin = [clipVal, 1023.5, 959]
    #Contour1.Isosurfaces = [val]
    return returnVals;
  
  #ppmt273_256_256_256_nrrd = NrrdReader( FileName='/scratch/01336/carson/data/RM/ppmt273_256_256_256.nrrd' )
  #reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')
  reader = NrrdReader( FileName=rm_data_dir+ '/ppmt273_256_256_256.nrrd' )

  Contour1 = Contour(Input=reader)

  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'ImageFile']
  val = (float(stage)/float(svbGetStagesSize()))*255.0
  Contour1.Isosurfaces = [125.0]
  Contour1.ComputeNormals = 1

  #clipVal = (float(stage)/float(svbGetStagesSize()))*2046+1
  Clip1 = Clip(ClipType="Plane")
  Clip1.ClipType.Origin = [clipVal, 1023.5, 959]
  Clip1.ClipType.Normal = [1,0,0]
  #Slice1 = Slice( SliceType="Plane" )

  #Slice1.SliceOffsetValues = [0.0]
  #Slice1.SliceType = "Plane"

  #Slice1.SliceType.Origin = [1, 1023.5, 959]
  #Slice1.SliceType.Normal = [1.0, 0.0, 0.0]

  DataRepresentation2 = Show()
  #DataRepresentation2.ScaleFactor = 25.5
  DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
  DataRepresentation2.SetRepresentationType('Surface')
  
  ResetCamera()
  if (stage == 0):
    cam = GetActiveCamera()
    cam.Roll(90)
    cam.Elevation(65)
    cam.Azimuth(-20)

  #numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  #numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  #numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  #print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  #print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  #print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))

  return returnVals

def svbRender():
  Render()
