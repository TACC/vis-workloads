try: paraview.simple
except: from paraview.simple import *

def svbSetup(geometryLevel=1):

  numCells = 0
  numPolys = 0 
  numPoints = 0
  
  if geometryLevel < 6:
    ppmt273_256_256_256_nrrd = NrrdReader( FileName='/scratch/01336/carson/data/RM/ppmt273_256_256_256.nrrd' )

    Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'ImageFile']
    Contour1.Isosurfaces = [27.0]
    Contour1.ComputeNormals = 0

    DataRepresentation2 = Show()
    DataRepresentation2.ScaleFactor = 25.5
    DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
  else:
    #ppmt273_nrrd = NrrdReader( FileName='/scratch/01336/carson/intelTACC/rm/ppmt273.nrrd' )
    def computeFileName(x):
      return {
      0:'/scratch/01336/carson/intelTACC/rm/rm_yz_256.xmf',
      1:'/scratch/01336/carson/intelTACC/rm/rm_yz_256.xmf',
      2:'/scratch/01336/carson/intelTACC/rm/rm_yz_512',
      3:'/scratch/01336/carson/intelTACC/rm/rm_yz_1024.xmf',
      4:'/scratch/01336/carson/intelTACC/rm/rm_yz_1280.xmf',
      5:'/scratch/01336/carson/intelTACC/rm/rm_yz_1792.xmf',
      6:'/scratch/01336/carson/intelTACC/rm/rm.xmf',
      }.get(x,6)
    fileName = computeFileName(geometryLevel)
    # name = '/scratch/01336/carson/intelTACC/rm/rm.xmf'
    rm_xmf = XDMFReader( FileName=fileName )

    # rm_xmf.Sets = []
    # rm_xmf.Grids = ['Grid_5']
    # rm_xmf.PointArrays = ['ImageFile']
    # Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    #Contour1.PointMergeMethod = "Uniform Binning"
    #Contour1.ContourBy = ['POINTS', 'RTData']
    #Contour1.Isosurfaces = [27.0]
    #Contour1.ComputeNormals = 0

    #DataRepresentation2 = Show()
    #DataRepresentation2.ScaleFactor = 25.5
    #DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'

    RenderView2 = GetRenderView()

    # DataRepresentation2 = Show()
    # DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
    # #DataRepresentation2.Slice = 959
    # DataRepresentation2.SelectionPointFieldDataArrayName = 'ImageFile'
    # #DataRepresentation2.ScalarOpacityUnitDistance = -4.241863336756942
    # DataRepresentation2.Representation = 'Outline'
    # DataRepresentation2.ScaleFactor = 204.70000000000002

    RenderView2.CameraClippingRange = [4733.166751461594, 9213.860962357088]

    Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'ImageFile']
    #Contour1.Isosurfaces = [115.0]

    Contour1.Isosurfaces = [27.0]
    if (geometryLevel == 7):
      Contour1.Isosurfaces = [27.0,33]
    if (geometryLevel == 8):
      Contour1.Isosurfaces = [27.0,33,56]
    if (geometryLevel == 9):
      Contour1.Isosurfaces = [22,27.0,33,56]
    if (geometryLevel == 10):
      Contour1.Isosurfaces = [18,22,27.0,33,56]

    DataRepresentation3 = Show()
    DataRepresentation3.ScaleFactor = 204.70000000000002
    DataRepresentation3.SelectionPointFieldDataArrayName = 'Normals'
    DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]

    #RenderView1 = GetRenderView()

  #DataRepresentation1 = Show()
  #DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #DataRepresentation1.Slice = 127
  #DataRepresentation1.SelectionPointFieldDataArrayName = 'ImageFile'
  #DataRepresentation1.ScalarOpacityUnitDistance = 1.7320508075688774
  #DataRepresentation1.Representation = 'Outline'
  #DataRepresentation1.ScaleFactor = 25.5

  #RenderView1.CameraPosition = [729.0865354184773, -292.7342127551322, -307.84659539241414]
  #RenderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
  #RenderView1.CameraClippingRange = [411.40476465105576, 1411.4925876279806]
  #RenderView1.CameraParallelScale = 220.83647796503186

  #DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #RenderView1.Background = [1.0,1.0,1.0]

  ResetCamera()
  cam = GetActiveCamera()
  cam.Roll(90)
  cam.Elevation(65)
  cam.Azimuth(-20)

  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))


  return {'azimuth':90, 'dolly':3.0}


def svbRender():
  Render()
