try: paraview.simple
except: from paraview.simple import *
def svbSetup(geometryLevel=1):

	numCells = 0
	numPolys = 0 
	numPoints = 0

	paraview.simple._DisableFirstRenderCameraReset()

	Top_Albian_large_normals_fixed_obj = WavefrontOBJReader( FileName='/scratch/01891/adb/geo/Top_Albian_large_normals_fixed.obj' )

	RenderView1 = GetRenderView()

	DataRepresentation2 = Show()
	DataRepresentation2.ScaleFactor = 4038.859375
	DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	RenderView1.CameraFocalPoint = [311041.546875, 3514944.25, 4050.0]
	RenderView1.CameraClippingRange = [66132.27016710148, 154040.97004230513]
	RenderView1.CameraPosition = [328631.4299478206, 3427661.9289184036, 59588.36001851113]
	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

	Basement_large_normalsgaain_obj = WavefrontOBJReader( FileName='/scratch/01891/adb/geo/Basement.large.normalsgaain.obj' )

	DataRepresentation3 = Show()
	DataRepresentation3.ScaleFactor = 3493.5687500000004
	DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	RenderView1.CameraClippingRange = [64530.62887441108, 155259.5969791027]
	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

	Base_MTC_large_obj = WavefrontOBJReader( FileName='/scratch/01891/adb/geo/Base_MTC_large.obj' )

	DataRepresentation4 = Show()
	DataRepresentation4.ScaleFactor = 4129.846875
	DataRepresentation4.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	RenderView1.CameraClippingRange = [64410.7310588127, 155587.59056582034]
	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

	Seafloor_zap_asc_obj = WavefrontOBJReader( FileName='/scratch/01891/adb/geo/Seafloor_zap.asc.obj' )

	DataRepresentation5 = Show()
	DataRepresentation5.ScaleFactor = 5525.181250000001
	DataRepresentation5.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	RenderView1.CameraClippingRange = [51508.49633040225, 163055.0999913982]
	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

	Top_MTC_large_obj = WavefrontOBJReader( FileName='/scratch/01891/adb/geo/Top_MTC_large.obj' )

	DataRepresentation6 = Show()
	DataRepresentation6.ScaleFactor = 4129.846875
	DataRepresentation6.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	DataRepresentation3.DiffuseColor = [0.6666666666666666, 0.0, 0.0]

	DataRepresentation4.DiffuseColor = [0.47058823529411764, 0.6666666666666666, 0.5803921568627451]

	DataRepresentation2.Visibility = 0

	DataRepresentation6.DiffuseColor = [0.47058823529411764, 0.7372549019607844, 1.0]

	DataRepresentation5.DiffuseColor = [1.0, 0.7843137254901961, 0.5372549019607843]
	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

	SetActiveSource(Seafloor_zap_asc_obj)
	Transform1 = Transform( Transform="Transform" )

	Transform1.Transform = "Transform"

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
	Transform1.Transform.Translate = [0.0, 0.0, -4000.0]

	DataRepresentation7 = Show()
	DataRepresentation7.ScaleFactor = 5525.181250000001
	DataRepresentation7.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation7.DiffuseColor = [1.0, 1.0, 1.0]

	DataRepresentation5.Visibility = 0

	RenderView1.CameraClippingRange = [50450.00418731889, 166780.99233505165]

	DataRepresentation7.DiffuseColor = [1.0, 0.7843137254901961, 0.5372549019607843]

	SetActiveSource(Top_MTC_large_obj)
	Transform2 = Transform( Transform="Transform" )

	Transform2.Transform = "Transform"

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
	Transform2.Transform.Translate = [0.0, 0.0, -2000.0]

	DataRepresentation8 = Show()
	DataRepresentation8.ScaleFactor = 4129.846875
	DataRepresentation8.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation8.DiffuseColor = [1.0, 1.0, 1.0]

	DataRepresentation6.Visibility = 0

	DataRepresentation8.DiffuseColor = [0.47058823529411764, 0.7372549019607844, 1.0]

	DataRepresentation2.Visibility = 1

	SetActiveSource(Basement_large_normalsgaain_obj)
	Transform3 = Transform( Transform="Transform" )

	Transform3.Transform = "Transform"

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
	RenderView1.CameraClippingRange = [46507.12095433405, 168752.43395154408]

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
	Transform3.Transform.Translate = [0.0, 0.0, 5000.0]

	DataRepresentation9 = Show()
	DataRepresentation9.ScaleFactor = 3493.5687500000004
	DataRepresentation9.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation9.DiffuseColor = [1.0, 1.0, 1.0]

	DataRepresentation3.Visibility = 0

	DataRepresentation9.DiffuseColor = [0.592156862745098, 0.0, 0.0]

	SetActiveSource(Top_Albian_large_normals_fixed_obj)
	Transform4 = Transform( Transform="Transform" )

	Transform4.Transform = "Transform"

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
	Transform4.Transform.Translate = [0.0, 0.0, 4000.0]

	DataRepresentation10 = Show()
	DataRepresentation10.ScaleFactor = 4038.859375
	DataRepresentation10.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	DataRepresentation2.Visibility = 0

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
	Transform3.Transform.Translate = [0.0, 0.0, 2000.0]

	RenderView1.CameraClippingRange = [48758.99243982868, 167626.49820879675]

	Transform4.Transform.Translate = [0.0, 0.0, 6000.0]

	RenderView1.CameraClippingRange = [47181.83914663448, 168415.07485539385]

	Transform3.Transform.Translate = [0.0, 0.0, 3000.0]

	Transform4.Transform.Translate = [0.0, 0.0, 9000.0]

	RenderView1.CameraClippingRange = [44816.109206843845, 169597.93982528918]

	Transform2.Transform.Translate = [0.0, 0.0, -6000.0]

	RenderView1.CameraClippingRange = [44577.90163585609, 170436.43047516607]

	Transform2.Transform.Translate = [0.0, 0.0, -8000.0]

	RenderView1.CameraViewUp = [0.0, 0.0, 1.0]
	RenderView1.CameraPosition = [317777.46875, 3369926.9481848134, 4338.0]
	RenderView1.CameraClippingRange = [96496.28879703477, 198458.75384241441]
	RenderView1.InteractionMode = 3
	RenderView1.CameraFocalPoint = [317777.46875, 3511412.375, 4338.0]
	RenderView1.CameraParallelScale = 36619.123064229214
	RenderView1.CenterOfRotation = [317777.46875, 3511412.375, 4338.0]

	Transform1.Transform.Translate = [0.0, 0.0, -8000.0]

	Transform1.Transform.Translate = [0.0, 0.0, -9000.0]

	Transform2.Transform.Translate = [0.0, 0.0, -6000.0]

	Transform2.Transform.Translate = [0.0, 0.0, -4500.0]

	Transform2.Transform.Translate = [0.0, 0.0, -5000.0]

	Transform4.Transform.Translate = [0.0, 0.0, 10000.0]

	RenderView1.CameraViewUp = [0.3401946549046027, 0.2820674051694079, 0.8970538310019835]
	RenderView1.CameraPosition = [256948.26399729348, 3429270.222812952, 50494.51975791374]
	RenderView1.CameraClippingRange = [40247.273637994265, 203394.3616118409]
	RenderView1.InteractionMode = '3D'
	RenderView1.CameraFocalPoint = [318063.7046413446, 3510067.578090641, 1911.6531775491044]
	RenderView1.CameraParallelScale = 37058.23649598536
	RenderView1.CenterOfRotation = [318063.7046413446, 3510067.578090641, 1911.6531775491044]

	print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
	print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
	print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))

	return {'azimuth':90, 'dolly':4.0}

def svbRender():
	Render()
