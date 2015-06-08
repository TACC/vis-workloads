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
  reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')

  Slice1 = Slice( SliceType="Plane" )

  Slice1.SliceOffsetValues = [0.0]
  Slice1.SliceType = "Plane"

  # toggle the 3D widget visibility.
  active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')

  Slice1.SliceType.Origin = [1, 1023.5, 959]
  Slice1.SliceType.Normal = [1.0, 0.0, 0.0]

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
