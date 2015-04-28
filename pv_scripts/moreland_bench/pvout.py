try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

Wavelet1 = Wavelet()

Wavelet1.WholeExtent = [-100, 100, -100, 100, -100, 100]

RenderView1 = GetRenderView()

DataRepresentation1 = Show()
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation1.Slice = 100
DataRepresentation1.SelectionPointFieldDataArrayName = 'RTData'
DataRepresentation1.ScalarOpacityUnitDistance = 1.7320508075688772
DataRepresentation1.Representation = 'Outline'
DataRepresentation1.ScaleFactor = 20.0

RenderView1.CameraViewUp = [0.0012887685077927545, 0.9998848349441063, 0.01512137310335118]
RenderView1.CameraPosition = [73.8108220673545, -10.152803028258734, 665.0526144935272]
RenderView1.CameraClippingRange = [439.7902989844048, 959.6231919053153]
RenderView1.CameraParallelScale = 173.20508075688772

DataRepresentation1.Opacity = 1.0
DataRepresentation1.Representation = 'Surface'
DataRepresentation1.ColorArrayName = ('POINT_DATA', 'RTData')

a1_RTData_PVLookupTable = GetLookupTableForArray( "RTData", 1, RGBPoints=[33.95114517211914, 0.23, 0.299, 0.754, 160.14612007141113, 0.865, 0.865, 0.865, 286.3410949707031, 0.706, 0.016, 0.15], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

a1_RTData_PiecewiseFunction = CreatePiecewiseFunction( Points=[33.95114517211914, 0.0, 0.5, 0.0, 286.3410949707031, 1.0, 0.5, 0.0] )

Contour1 = Contour( PointMergeMethod="Uniform Binning" )

DataRepresentation1.ScalarOpacityFunction = a1_RTData_PiecewiseFunction
DataRepresentation1.LookupTable = a1_RTData_PVLookupTable

a1_RTData_PVLookupTable.ScalarOpacityFunction = a1_RTData_PiecewiseFunction

Contour1.PointMergeMethod = "Uniform Binning"
Contour1.ContourBy = ['POINTS', 'RTData']
Contour1.Isosurfaces = [160.14612007141113]

DataRepresentation2 = Show()
DataRepresentation2.ColorArrayName = ('POINT_DATA', '')
DataRepresentation2.ScaleFactor = 20.0
DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]

DataRepresentation1.Visibility = 0

RenderView1.CameraViewUp = [0.0012887685077927517, 0.9998848349441063, 0.015121373103351182]
RenderView1.CameraPosition = [85.10984187955833, -10.14693085117321, 663.7013270423705]
RenderView1.CameraClippingRange = [436.876425684926, 963.1951020489158]

a3_cellNormals_PVLookupTable = GetLookupTableForArray( "cellNormals", 3, RGBPoints=[-0.9999977350234985, 0.23, 0.299, 0.754, -5.206577412586455e-05, 0.865, 0.865, 0.865, 0.9998936057090759, 0.706, 0.016, 0.15], VectorMode='Component', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

a3_cellNormals_PiecewiseFunction = CreatePiecewiseFunction( Points=[-0.9999977350234985, 0.0, 0.5, 0.0, 0.9998936057090759, 1.0, 0.5, 0.0] )

DataRepresentation2.ColorArrayName = ('CELL_DATA', 'cellNormals')
DataRepresentation2.LookupTable = a3_cellNormals_PVLookupTable
DataRepresentation2.ColorAttributeType = 'CELL_DATA'

Clip1 = Clip( ClipType="Plane" )

a3_cellNormals_PVLookupTable.ScalarOpacityFunction = a3_cellNormals_PiecewiseFunction

Clip1.ClipType.Origin = [0.0, -2.8016510009765625, 0.0]
Clip1.ClipType = "Plane"

# toggle the 3D widget visibility.
active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
RenderView1.CameraClippingRange = [387.39265521589584, 1025.484973920735]

# toggle the 3D widget visibility.
active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
RenderView1.CameraClippingRange = [436.876425684926, 963.1951020489158]

DataRepresentation3 = Show()
DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation3.ColorAttributeType = 'POINT_DATA'
DataRepresentation3.SelectionPointFieldDataArrayName = 'Normals'
DataRepresentation3.ColorArrayName = ('POINT_DATA', '')
DataRepresentation3.ScalarOpacityUnitDistance = 4.254755234308723
DataRepresentation3.ScaleFactor = 20.0

DataRepresentation2.Visibility = 0

RenderView1.CameraViewUp = [0.003983775461067583, 0.9995403728524186, 0.030052829669162843]
RenderView1.CameraPosition = [152.24662605854266, -20.19076654221791, 651.3519745179975]
RenderView1.CameraClippingRange = [429.0314132914365, 947.2168901127079]

DataRepresentation3.ScalarOpacityFunction = a3_cellNormals_PiecewiseFunction
DataRepresentation3.ColorArrayName = ('CELL_DATA', 'cellNormals')
DataRepresentation3.LookupTable = a3_cellNormals_PVLookupTable
DataRepresentation3.ColorAttributeType = 'CELL_DATA'

Render()
