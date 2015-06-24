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

rm_data_dir =  path_vars["RMDATA_DIR"]
print "rm_data_dir:%s" %  rm_data_dir

global Contour1
global reader
global ospIso

def svbGetStagesSize():
  return 4;

def svbSetup(geometryLevel=1, stage=0):
  #global Contour1
  global ospIso
  global reader

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False};

  val = (float(stage)/float(svbGetStagesSize()))*255.0
  if (stage != 0):  
    #ResetCamera()
    #Contour1.Isosurfaces = [val]
    ospIso.IsosurfaceValue = val
    return returnVals;

  numCells = 0
  numPolys = 0 
  numPoints = 0
  print "h"
  print(rm_data_dir+"/rm_0273.nhdr")
  
  reader = NrrdReader( FileName=rm_data_dir+ '/ppmt273_256_256_256.nrrd' )
  # reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')

  lut = imageFileLUT = GetColorTransferFunction('ImageFile')

  ospIso = ospIsosurface(Input=reader)

  rep = Show()
  rep.ColorArrayName = ['POINTS','ImageFile']
  rep.LookupTable = lut
  imageFilePWF = GetOpacityTransferFunction('ImageFile')
  rep.SetRepresentationType('Volume')


  # Contour1 = Contour( PointMergeMethod="Uniform Binning" )
  # Contour1 = Contour(Input=reader)

  # Contour1.PointMergeMethod = "Uniform Binning"
  # Contour1.ContourBy = ['POINTS', 'ImageFile']
  # Contour1.Isosurfaces = [val]
  # # Contour1.Isosurfaces = [125.0]
  # Contour1.PointMergeMethod = 'Uniform Binning'
  # Contour1.ComputeNormals = 1

  # DataRepresentation2 = Show()
  # DataRepresentation2.ScaleFactor = 25.5
  # DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
  # DataRepresentation2.SetRepresentationType('Surface')
  
  ResetCamera()
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
