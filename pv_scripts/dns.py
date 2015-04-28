try: paraview.simple
except: from paraview.simple import *

def svbSetup(geometryLevel=1):
  numCells = 0
  numPolys = 0 
  numPoints = 0
  numFiles=geometryLevel
  name = '/scratch/01336/carson/intelTACC/dns/u_yz_'+str(numFiles*128)+'.xmf'
  dns_xmf = XDMFReader( FileName=name )

  dns_xmf.Sets = []
  dns_xmf.Grids = ['Grid_2']
  dns_xmf.PointArrays = ['RTData']

  RenderView1 = GetRenderView()
  #RenderView1.CenterOfRotation = [1.5, 3839.0, 5119.0]

  #DataRepresentation1 = Show()
  #DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #DataRepresentation1.Slice = 5119
  #DataRepresentation1.SelectionPointFieldDataArrayName = 'RTData'
  #DataRepresentation1.ScalarOpacityUnitDistance = 20.713499280232124
  #DataRepresentation1.Representation = 'Outline'
  #DataRepresentation1.ScaleFactor = 1023.8000000000001

  RenderView1.CameraPosition = [3288.9337054286098, 3838.9999999999995, 29621.745437756035]
  RenderView1.CameraViewUp = [0.0, 1.0, 0.0]
  RenderView1.CameraFocalPoint = [1.4999999999999774, 3838.9999999999995, 5119.0]
  RenderView1.CameraClippingRange = [14378.327142273009, 37802.84573819896]
  RenderView1.CameraParallelScale = 6398.600178945392

  #contourPoints = [.8,.95,1.05,1.15]
  contourPoints = [.8]
  #contourColors = [[.01,.12,.22],[.3,.39,.55],[.5,.24,.8],[.83,.57,.42]]
  contourColors = [[.01,.17,.29],[.34,.53,.70],[.56,.7,.77],[.46,.24,.08],[1,.8,.46],[1,.89,.72]]
  for j in range(0,len(contourPoints)):
    SetActiveSource(dns_xmf)
    print "adding contour " + str(contourPoints[j]) + " color " + str(contourColors[j])
    Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'RTData']
    Contour1.Isosurfaces = [contourPoints[j]]

    cDataRepresentation2 = Show()
    cDataRepresentation2.ScaleFactor = 968.4097045898438
    #cDataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
    #DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
    cDataRepresentation2.DiffuseColor = contourColors[j]
    numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
    numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
    numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()
  ResetCamera()
  cam = GetActiveCamera()
  cam.Elevation(65)
  cam.Azimuth(-20)

  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))


def svbRender():
  Render()
