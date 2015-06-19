try: paraview.simple
except: from paraview.simple import *

global Slice1
global reader

def svbGetStagesSize():
  return 3;

def svbSetup(geometryLevel=1, stage=0):
  global Clip1
  global reader

  numCells = 0
  numPolys = 0 
  numPoints = 0
  
  #ppmt273_256_256_256_nrrd = NrrdReader( FileName='/scratch/01336/carson/data/RM/ppmt273_256_256_256.nrrd' )
  # reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')
  reader = XdmfReader( FileName='/work/00401/pnav/workloads/dns/u_0035_pv.xmf')

  Contour1 = Contour( PointMergeMethod="Uniform Binning" )

  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'ImageFile']
  #data range for smaller 32 is -.0299 to 1.268
  valRanges = [-0.03,1.26]
  valRange = valRanges[1]-valRanges[0]
  val = (float(stage)/float(svbGetStagesSize()))*valRange/2.0+valRanges[0]
  Contour1.Isosurfaces = [val]
  Contour1.ComputeNormals = 1

  # bounds are same as dimensions.
  clipRanges = [1,7679]
  clipRange = clipRanges[1]-clipRanges[0]
  val = (float(stage)/float(svbGetStagesSize()))*clipRange+clipRanges[0]
  Clip1 = Clip(ClipType="Plane")
  Clip1.ClipType.Origin = [1, val, 1]
  Clip1.ClipType.Normal = [0,1,0]
  #Slice1 = Slice( SliceType="Plane" )

  #Slice1.SliceOffsetValues = [0.0]
  #Slice1.SliceType = "Plane"

  #Slice1.SliceType.Origin = [1, 1023.5, 959]
  #Slice1.SliceType.Normal = [1.0, 0.0, 0.0]

  DataRepresentation2 = Show()
  DataRepresentation2.ScaleFactor = 25.5
  DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
  
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

  return {'azimuth':90, 'dolly':3.0}

def svbRender():
  Render()
