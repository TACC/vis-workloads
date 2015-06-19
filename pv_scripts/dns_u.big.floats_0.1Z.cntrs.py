try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

BigDns_halfX_raw = ImageReader( FilePrefix='/scratch/02029/foss/WRF/BigDns_halfX.raw' )

BigDns_halfX_raw.ScalarArrayName = 'dns_floats_halfZ'
BigDns_halfX_raw.DataScalarType = 'float'
BigDns_halfX_raw.DataByteOrder = 'LittleEndian'
BigDns_halfX_raw.DataExtent = [0, 10239, 0, 7679, 0, 152]

RenderView2 = GetRenderView()
RenderView2.CenterOfRotation = [5119.5, 3839.5, 76.0]

DataRepresentation1 = Show()
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation1.Slice = 76
DataRepresentation1.SelectionPointFieldDataArrayName = 'dns_floats_halfZ'
DataRepresentation1.ScalarOpacityUnitDistance = -13.094812823138732
DataRepresentation1.Representation = 'Outline'
DataRepresentation1.ScaleFactor = 1023.9000000000001

RenderView2.CameraViewUp = [0.06814911090070715, 0.3877779809613524, 0.9192300779266201]
RenderView2.CameraPosition = [2399.659840264723, -16343.318890262815, 8494.03597987259]
RenderView2.CameraClippingRange = [13501.752286542744, 32828.730814209186]
RenderView2.InteractionMode = '3D'
RenderView2.CameraFocalPoint = [5203.5761526481565, 3718.4391775782915, -176.9079254765782]
RenderView2.CameraParallelScale = 6399.751284229724
RenderView2.CenterOfRotation = [5203.5761526481565, 3718.4391775782915, -176.9079254765782]

DataRepresentation1.Representation = 'Surface'
DataRepresentation1.ColorArrayName = ('POINT_DATA', 'dns_floats_halfZ')

a1_dns_floats_halfZ_PVLookupTable = GetLookupTableForArray( "dns_floats_halfZ", 1, RGBPoints=[0.0, 0.0, 0.254902, 0.376471, 0.104021, 0.368627, 0.678431, 0.901961, 0.208042, 0.0, 0.239216, 0.0, 0.318007, 0.376471, 0.482353, 0.356863, 0.422028, 1.0, 1.0, 0.498039, 0.526049, 1.0, 1.0, 0.498039, 0.636014, 1.0, 0.443137, 0.0980392, 0.743007, 1.0, 0.0, 0.0, 0.85, 0.494118, 0.0, 0.0], VectorMode='Magnitude', NanColor=[0.250004, 0.0, 0.0], ColorSpace='RGB', ScalarRangeInitialized=1.0 )

a1_dns_floats_halfZ_PiecewiseFunction = CreatePiecewiseFunction( Points=[-0.13956387341022491, 0.0, 0.5, 0.0, 1.2644177675247192, 1.0, 0.5, 0.0] )

ScalarBarWidgetRepresentation1 = CreateScalarBar( Title='dns_floats_halfZ', Enabled=0, Visibility=0, LabelFontSize=12, LookupTable=a1_dns_floats_halfZ_PVLookupTable, TitleFontSize=12 )
GetRenderView().Representations.append(ScalarBarWidgetRepresentation1)

Contour1 = Contour( PointMergeMethod="Uniform Binning" )

DataRepresentation1.ScalarOpacityFunction = a1_dns_floats_halfZ_PiecewiseFunction
DataRepresentation1.LookupTable = a1_dns_floats_halfZ_PVLookupTable

a1_dns_floats_halfZ_PVLookupTable.ScalarOpacityFunction = a1_dns_floats_halfZ_PiecewiseFunction

Contour1.PointMergeMethod = "Uniform Binning"
Contour1.ContourBy = ['POINTS', 'dns_floats_halfZ']
Contour1.Isosurfaces = [0.5624269470572472]

Contour1.Isosurfaces = [1.0]
Contour1.ComputeScalars = 1

DataRepresentation2 = Show()
DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation2.SelectionPointFieldDataArrayName = 'dns_floats_halfZ'
DataRepresentation2.ColorArrayName = ('POINT_DATA', 'dns_floats_halfZ')
DataRepresentation2.LookupTable = a1_dns_floats_halfZ_PVLookupTable
DataRepresentation2.ScaleFactor = 1023.9000000000001

a1_dns_floats_halfZ_PVLookupTable.RGBPoints = [0.0, 0.0, 0.254902, 0.376471, 0.12237764705882354, 0.368627, 0.678431, 0.901961, 0.24475529411764707, 0.0, 0.239216, 0.0, 0.3741258823529412, 0.376471, 0.482353, 0.356863, 0.49650352941176473, 1.0, 1.0, 0.498039, 0.6188811764705883, 1.0, 1.0, 0.498039, 0.7482517647058824, 1.0, 0.443137, 0.0980392, 0.8741258823529412, 1.0, 0.0, 0.0, 1.0, 0.494118, 0.0, 0.0]

DataRepresentation1.Visibility = 0

RenderView2.CameraClippingRange = [13504.87462392578, 32817.740186620904]

Contour1.Isosurfaces = [1.0, 0.5]

RenderView2.CameraClippingRange = [13502.781871985348, 32825.10667345122]

Contour1.Isosurfaces = [0.5]

SetActiveSource(BigDns_halfX_raw)
Contour2 = Contour( PointMergeMethod="Uniform Binning" )

Contour2.PointMergeMethod = "Uniform Binning"
Contour2.ContourBy = ['POINTS', 'dns_floats_halfZ']
Contour2.Isosurfaces = [0.5624269470572472]

Contour2.Isosurfaces = [0.1]

DataRepresentation3 = Show()
DataRepresentation3.ColorArrayName = ('POINT_DATA', '')
DataRepresentation3.ScaleFactor = 1023.9000000000001
DataRepresentation3.SelectionPointFieldDataArrayName = 'Normals'
DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]

RenderView2.CameraClippingRange = [13502.014449855798, 32827.807999347235]

SetActiveSource(BigDns_halfX_raw)
Contour3 = Contour( PointMergeMethod="Uniform Binning" )

Contour3.PointMergeMethod = "Uniform Binning"
Contour3.ContourBy = ['POINTS', 'dns_floats_halfZ']
Contour3.Isosurfaces = [0.5624269470572472]

Contour3.Isosurfaces = [0.7]
Contour3.ComputeScalars = 1

DataRepresentation4 = Show()
DataRepresentation4.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation4.SelectionPointFieldDataArrayName = 'dns_floats_halfZ'
DataRepresentation4.ColorArrayName = ('POINT_DATA', 'dns_floats_halfZ')
DataRepresentation4.LookupTable = a1_dns_floats_halfZ_PVLookupTable
DataRepresentation4.ScaleFactor = 1023.9000000000001

Render()
