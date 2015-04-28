try: paraview.simple
except: from paraview.simple import *

def svbSetup(geometryLevel=1):
  numCells = 0
  numPolys = 0 
  numPoints = 0
  paraview.simple._DisableFirstRenderCameraReset()

  a4RHV_ribbons_obj = WavefrontOBJReader( FileName='/work/01891/adb/molecule_benchmark/bacteriaphage_ribbons.obj' )

  RenderView1 = GetRenderView()
  RenderView1.CenterOfRotation = [77.85100555419922, 193.92295455932617, 40.27460050582886]

  DataRepresentation1 = Show()
  DataRepresentation1.ScaleFactor = 45.73679962158204
  DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]

  RenderView1.CameraPosition = [77.85100555419922, 193.92295455932617, 1045.196735251777]
  RenderView1.CameraFocalPoint = [77.85100555419922, 193.92295455932617, 40.27460050582886]
  RenderView1.CameraClippingRange = [888.7225317046486, 1153.617427140539]
  RenderView1.CameraParallelScale = 260.092987317333
  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  a4RHV_pdb = PDBReader( FileName='/work/01891/adb/molecule_benchmark/1VRI.pdb' )

  DataRepresentation6 = Show()
  DataRepresentation6.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  DataRepresentation6.SelectionPointFieldDataArrayName = 'rgb_colors'
  DataRepresentation6.ColorArrayName = ('POINT_DATA', 'rgb_colors')
  DataRepresentation6.MapScalars = 0
  DataRepresentation6.ScaleFactor = 8.8759998321533
  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  a3_rgb_colors_PVLookupTable = GetLookupTableForArray( "rgb_colors", 3, RGBPoints=[255.0, 0.23, 0.299, 0.754, 307.8122292025696, 0.865, 0.865, 0.865, 360.62445840513925, 0.706, 0.016, 0.15], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

  a3_rgb_colors_PiecewiseFunction = CreatePiecewiseFunction( Points=[255.0, 0.0, 0.5, 0.0, 360.62445840513925, 1.0, 0.5, 0.0] )

  DataRepresentation7 = Show()

  DataRepresentation6.Opacity = 0.62
  DataRepresentation6.LookupTable = a3_rgb_colors_PVLookupTable

  a3_rgb_colors_PVLookupTable.ScalarOpacityFunction = a3_rgb_colors_PiecewiseFunction
  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))

  return {'azimuth':90, 'dolly':3.0}

def svbRender():
        Render()
