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


global Contour1
global reader

def svbGetStagesSize():
  return 10;

def svbSetup(geometryLevel=1, stage=0):
  global Contour1
  global reader

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False};

  valRanges = [-0.03,1.26]
  valRange = valRanges[1]-valRanges[0]
  val = (float(stage)/float(svbGetStagesSize()))*valRange + valRanges[0]

  if (stage != 0):  
    ResetCamera()
    Contour1.Isosurfaces = [val]
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
  Contour1.Isosurfaces = [val]
  Contour1.ComputeNormals = 1

  DataRepresentation2 = Show()
  DataRepresentation2.ScaleFactor = 25.5
  DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
  DataRepresentation2.SetRepresentationType('Surface')
  #DataRepresentation2.ColorArrayName = ['POINTS', '']
  
  ResetCamera()
  cam = GetActiveCamera()
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
