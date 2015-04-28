try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

def svbGetStagesSize():
  return 5;

Wavelet1 = Wavelet()
global DataRepresentation1
global DataRepresentation2
global DataRepresentation3
DataRepresentation1 = Show()
DataRepresentation2 = Show()
DataRepresentation3 = Show()

def svbSetup(geometryLevel=1, stage=0):
  #
  # Load wavelet, surface representation with RTData
  #
  if (stage ==0):
    global Wavelet1
    global DataRepresentation1
    global DataRepresentation2
    global DataRepresentation3
    DataRepresentation1.Visibility = 0
    DataRepresentation2.Visibility = 0
    DataRepresentation3.Visibility = 0
    Wavelet1 = Wavelet()

    Wavelet1.WholeExtent = [-500, 500, -500, 500, -500, 500]
    if (geometryLevel == 4):    
        Wavelet1.WholeExtent = [-2000, 2000, -2000, 2000, -2000, 2000]
    if (geometryLevel == 6):    
        Wavelet1.WholeExtent = [-4000, 4000, -4000, 4000, -4000, 4000]

    RenderView1 = GetRenderView()

    DataRepresentation1 = Show()
    DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
    # DataRepresentation1.Slice = 100
    DataRepresentation1.SelectionPointFieldDataArrayName = 'RTData'
    # DataRepresentation1.ScalarOpacityUnitDistance = 1.7320508075688772
    DataRepresentation1.Representation = 'Outline'
    DataRepresentation1.ScaleFactor = 20.0

    RenderView1.CameraViewUp = [0.0012887685077927545, 0.9998848349441063, 0.01512137310335118]
    RenderView1.CameraPosition = [73.8108220673545, -10.152803028258734, 665.0526144935272]
    RenderView1.CameraClippingRange = [439.7902989844048, 959.6231919053153]
    RenderView1.CameraParallelScale = 173.20508075688772

    DataRepresentation1.Opacity = 1.0
    DataRepresentation1.Representation = 'Surface'
    DataRepresentation1.ColorArrayName = ('POINT_DATA', 'RTData')

    ResetCamera()
    
    #
    # Change opacity to 0.5
    #
  if (stage == 1 ):  
    #global DataRepresentation1
    # global DataRepresentation2
    # global DataRepresentation3
    # DataRepresentation1 = Show()
    DataRepresentation1.Opacity = 0.5
    DataRepresentation1.Representation = 'Surface'
    DataRepresentation1.ColorArrayName = ('POINT_DATA', 'RTData')



    #
    # Opacity to 1.0.  Contour filter.  RTdata.  Take default value (around 128).  Apply.  Color by Cell Normals, X coordinate.
    #
  if (stage == 2 ):  
    #global DataRepresentation2
    a1_RTData_PVLookupTable = GetLookupTableForArray( "RTData", 1, RGBPoints=[33.95114517211914, 0.23, 0.299, 0.754, 160.14612007141113, 0.865, 0.865, 0.865, 286.3410949707031, 0.706, 0.016, 0.15], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

    a1_RTData_PiecewiseFunction = CreatePiecewiseFunction( Points=[33.95114517211914, 0.0, 0.5, 0.0, 286.3410949707031, 1.0, 0.5, 0.0] )
    Contour1 = Contour( PointMergeMethod="Uniform Binning" )
    # DataRepresentation1 = Show()
    # DataRepresentation1.ScalarOpacityFunction = a1_RTData_PiecewiseFunction
    DataRepresentation1.LookupTable = a1_RTData_PVLookupTable

    # a1_RTData_PVLookupTable.ScalarOpacityFunction = a1_RTData_PiecewiseFunction

    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'RTData']
    Contour1.Isosurfaces = [160.14612007141113]

    DataRepresentation2 = Show()
    DataRepresentation2.ColorArrayName = ('CELL_DATA', 'cellNormals')
    DataRepresentation2.ScaleFactor = 20.0
    DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
    DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]

    DataRepresentation1.Visibility = 0
    RenderView1 = GetRenderView()
    RenderView1.CameraViewUp = [0.0012887685077927517, 0.9998848349441063, 0.015121373103351182]
    RenderView1.CameraPosition = [85.10984187955833, -10.14693085117321, 663.7013270423705]
    RenderView1.CameraClippingRange = [436.876425684926, 963.1951020489158]

    a3_cellNormals_PVLookupTable = GetLookupTableForArray( "cellNormals", 3, RGBPoints=[-0.9999977350234985, 0.23, 0.299, 0.754, -5.206577412586455e-05, 0.865, 0.865, 0.865, 0.9998936057090759, 0.706, 0.016, 0.15], VectorMode='Component', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

    a3_cellNormals_PiecewiseFunction = CreatePiecewiseFunction( Points=[-0.9999977350234985, 0.0, 0.5, 0.0, 0.9998936057090759, 1.0, 0.5, 0.0] )

    DataRepresentation2.ColorArrayName = ('CELL_DATA', 'cellNormals')
    DataRepresentation2.LookupTable = a3_cellNormals_PVLookupTable
    # DataRepresentation2.ColorAttributeType = 'CELL_DATA'
#
# Clip filter, color by cell normals
#
  if (stage == 3 ):
    # global DataRepresentation1
    #global DataRepresentation2
    #global DataRepresentation3
    Clip1 = Clip( ClipType="Plane" )
    RenderView1 = GetRenderView()
    # a3_cellNormals_PVLookupTable.ScalarOpacityFunction = a3_cellNormals_PiecewiseFunction

    Clip1.ClipType.Origin = [0.0, -2.8016510009765625, 0.0]
    Clip1.ClipType = "Plane"

    # toggle the 3D widget visibility.
    active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
    RenderView1.CameraClippingRange = [387.39265521589584, 1025.484973920735]

    # toggle the 3D widget visibility.
    active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
    RenderView1.CameraClippingRange = [436.876425684926, 963.1951020489158]

    DataRepresentation3 = Show()
    DataRepresentation3.Opacity = 1.0
    DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
    # DataRepresentation3.ColorAttributeType = 'POINT_DATA'
    DataRepresentation3.SelectionPointFieldDataArrayName = 'Normals'
    DataRepresentation3.ColorArrayName = ('POINT_DATA', '')
    # DataRepresentation3.ScalarOpacityUnitDistance = 4.254755234308723
    DataRepresentation3.ScaleFactor = 20.0

    DataRepresentation2.Visibility = 0

    RenderView1.CameraViewUp = [0.003983775461067583, 0.9995403728524186, 0.030052829669162843]
    RenderView1.CameraPosition = [152.24662605854266, -20.19076654221791, 651.3519745179975]
    RenderView1.CameraClippingRange = [429.0314132914365, 947.2168901127079]
    ResetCamera()
    a3_cellNormals_PVLookupTable = GetLookupTableForArray( "cellNormals", 3, RGBPoints=[-0.9999977350234985, 0.23, 0.299, 0.754, -5.206577412586455e-05, 0.865, 0.865, 0.865, 0.9998936057090759, 0.706, 0.016, 0.15], VectorMode='Component', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )


    # DataRepresentation3.ScalarOpacityFunction = a3_cellNormals_PiecewiseFunction
    DataRepresentation3.ColorArrayName = ('CELL_DATA', 'cellNormals')
    DataRepresentation3.LookupTable = a3_cellNormals_PVLookupTable
    # DataRepresentation3.ColorAttributeType = 'CELL_DATA'

#
# Whipple
#
  if (stage == 4 ):
    DataRepresentation1.Visibility = 0
    DataRepresentation2.Visibility = 0
    DataRepresentation3.Visibility = 0
    files=['/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.000', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.001', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.002', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.003', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.004', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.005', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.006', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.007', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.008', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.009', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.010', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.011', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.012', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.013', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.014', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.015', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.016', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.017', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.018', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.019', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.020', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.021', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.022', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.023', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.024', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.025', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.026', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.027', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.028', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.029', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.030', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.031', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.032', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.033', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.034', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.035', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.036', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.037', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.038', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.039', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.040', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.041', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.042', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.043', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.044', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.045', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.046', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.047', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.048', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.049', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.050', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.051', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.052', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.053', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.054', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.055', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.056', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.057', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.058', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.059', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.060', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.061', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.062', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.063', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.064', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.065', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.066', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.067', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.068', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.069', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.070', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.071', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.072', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.073', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.074', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.075', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.076', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.077', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.078', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.079', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.080', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.081', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.082', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.083', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.084', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.085', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.086', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.087', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.088', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.089', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.090', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.091', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.092', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.093', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.094', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.095', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.096', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.097', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.098', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.099', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.100', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.101', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.102', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.103', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.104', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.105', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.106', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.107', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.108', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.109', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.110', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.111', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.112', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.113', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.114', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.115', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.116', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.117', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.118', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.119', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.120', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.121', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.122', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.123', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.124', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.125', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.126', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.127', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.128', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.129', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.130', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.131', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.132', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.133', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.134', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.135', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.136', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.137', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.138', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.139', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.140', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.141', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.142', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.143', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.144', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.145', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.146', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.147', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.148', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.149', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.150', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.151', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.152', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.153', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.154', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.155', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.156', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.157', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.158', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.159', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.160', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.161', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.162', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.163', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.164', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.165', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.166', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.167', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.168', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.169', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.170', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.171', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.172', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.173', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.174', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.175', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.176', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.177', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.178', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.179', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.180', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.181', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.182', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.183', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.184', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.185', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.186', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.187', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.188', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.189', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.190', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.191', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.192', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.193', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.194', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.195', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.196', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.197', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.198', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.199', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.200', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.201', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.202', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.203', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.204', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.205', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.206', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.207', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.208', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.209', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.210', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.211', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.212', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.213', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.214', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.215', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.216', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.217', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.218', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.219', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.220', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.221', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.222', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.223', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.224', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.225', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.226', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.227', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.228', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.229', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.230', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.231', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.232', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.233', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.234', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.235', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.236', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.237', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.238', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.239', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.240', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.241', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.242', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.243', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.244', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.245', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.246', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.247', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.248', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.249', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.250', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.251', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.252', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.253', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.254', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.255', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.256', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.257', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.258', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.259', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.260', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.261', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.262', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.263', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.264', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.265', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.266', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.267', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.268', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.269', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.270', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.271', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.272', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.273', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.274', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.275', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.276', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.277', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.278', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.279', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.280', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.281', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.282', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.283', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.284', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.285', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.286', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.287', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.288', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.289', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.290', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.291', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.292', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.293', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.294', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.295', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.296', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.297', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.298', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.299'] 
    # files=['/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.000', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.001']
    files = files[0:19]

    #Whipple_Shield_exo_300_000 = ExodusIIReader( FileName=['/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.000'] )
    Whipple_Shield_exo_300_ = ExodusIIReader( FileName=files )

    Whipple_Shield_exo_300_.FileRange = [0, 299]
    Whipple_Shield_exo_300_.XMLFileName = 'Invalid result'
    Whipple_Shield_exo_300_.FilePrefix = '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.'
    Whipple_Shield_exo_300_.ModeShape = 20
    Whipple_Shield_exo_300_.FilePattern = '%s%03i'

    Whipple_Shield_exo_300_.NodeSetArrayStatus = []
    Whipple_Shield_exo_300_.ElementVariables = ['VOID_FRC', 'VOLFRC1', 'VOLFRC2', 'DENSITY', 'TEMPERATURE', 'PRESSURE']
    Whipple_Shield_exo_300_.ElementBlocks = ['Unnamed block ID: 1 Type: HEX']
    """
    AnimationScene1 = GetAnimationScene()
    AnimationScene1.EndTime = 2.000108543143142e-05
    AnimationScene1.PlayMode = 'Snap To TimeSteps'

    Whipple_Shield_exo_300_000.FileRange = [0, 299]
    Whipple_Shield_exo_300_000.XMLFileName = 'Invalid result'
    Whipple_Shield_exo_300_000.FilePrefix = '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.'
    Whipple_Shield_exo_300_000.ModeShape = 20
    Whipple_Shield_exo_300_000.FilePattern = '%s%03i'

    Whipple_Shield_exo_300_001 = ExodusIIReader( FileName=['/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.001'] )

    Whipple_Shield_exo_300_001.FileRange = [0, 299]
    Whipple_Shield_exo_300_001.XMLFileName = 'Invalid result'
    Whipple_Shield_exo_300_001.FilePrefix = '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.'
    Whipple_Shield_exo_300_001.ModeShape = 20
    Whipple_Shield_exo_300_001.FilePattern = '%s%03i'

    Whipple_Shield_exo_300_000.NodeSetArrayStatus = []
    Whipple_Shield_exo_300_000.ElementVariables = []
    Whipple_Shield_exo_300_000.ElementBlocks = ['Unnamed block ID: 1 Type: HEX']

    SetActiveSource(Whipple_Shield_exo_300_000)

    RenderView1 = GetRenderView()
    RenderView1.CenterOfRotation = [0.0, 0.0, 0.018435800448060036]

    DataRepresentation1 = Show()
    DataRepresentation1.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    DataRepresentation1.SelectionPointFieldDataArrayName = 'GlobalNodeId'
    DataRepresentation1.SelectionCellFieldDataArrayName = 'GlobalElementId'
    DataRepresentation1.ScalarOpacityUnitDistance = 0.00028215277189116728
    DataRepresentation1.ExtractedBlockIndex = 2
    DataRepresentation1.ScaleFactor = 0.0050799999386072162

    Whipple_Shield_exo_300_001.NodeSetArrayStatus = []
    Whipple_Shield_exo_300_001.ElementVariables = ['VOID_FRC', 'VOLFRC1', 'VOLFRC2', 'DENSITY', 'TEMPERATURE', 'PRESSURE']
    Whipple_Shield_exo_300_001.ElementBlocks = ['Unnamed block ID: 1 Type: HEX']

    SetActiveSource(Whipple_Shield_exo_300_001)
    """
    RenderView1 = GetRenderView()
    RenderView1.CenterOfRotation = [0.0, 0.0, 0.018435800448060036]
    SetActiveSource(Whipple_Shield_exo_300_)

    AnimationScene1 = GetAnimationScene()
    AnimationScene1.EndTime = 2.000108543143142e-05
    AnimationScene1.PlayMode = 'Snap To TimeSteps'

    # DataRepresentation2 = Show()
    # DataRepresentation2.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    # DataRepresentation2.SelectionPointFieldDataArrayName = 'GlobalNodeId'
    # DataRepresentation2.SelectionCellFieldDataArrayName = 'DENSITY'
    # DataRepresentation2.ScalarOpacityUnitDistance = 0.00028215277189116728
    # DataRepresentation2.ExtractedBlockIndex = 2
    # DataRepresentation2.ScaleFactor = 0.0050799999386072162

    RenderView1.CameraPosition = [0.0, 0.0, 0.18813575352296963]
    RenderView1.CameraFocalPoint = [0.0, 0.0, 0.018435800448060036]
    RenderView1.CameraClippingRange = [0.11770729481791534, 0.23555732428522624]
    RenderView1.CameraParallelScale = 0.043921579808790676

    # Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    # Contour1.PointMergeMethod = "Uniform Binning"
    # Contour1.ContourBy = ['POINTS', 'GlobalNodeId']
    # Contour1.Isosurfaces = [15234180.0]

    # Contour1.Input = []
    # Contour1.PointMergeMethod = []

    #Delete(PointMergeMethod)
    #Delete(Contour1)
    #SetActiveSource(Whipple_Shield_exo_300_001)
    SetActiveSource(Whipple_Shield_exo_300_)
    CellDatatoPointData1 = CellDatatoPointData()

    # DataRepresentation3 = Show()
    # DataRepresentation3.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    # DataRepresentation3.SelectionPointFieldDataArrayName = 'DENSITY'
    # DataRepresentation3.SelectionCellFieldDataArrayName = 'DENSITY'
    # DataRepresentation3.ScalarOpacityUnitDistance = 0.00028215277189116728
    # DataRepresentation3.ExtractedBlockIndex = 2
    # DataRepresentation3.ScaleFactor = 0.0050799999386072162

    DataRepresentation2.Visibility = 0
    SetActiveSource(CellDatatoPointData1)
    Contour2 = Contour( PointMergeMethod="Uniform Binning" )

    Contour2.PointMergeMethod = "Uniform Binning"
    # Contour2.ContourBy = ['POINTS', 'DENSITY']
    # Contour2.Isosurfaces = [3936.18994140625]
    Contour2.ContourBy = ['POINTS', 'VOLFRC1']
    Contour2.Isosurfaces = [0.5]

    DataRepresentation4 = Show()
    DataRepresentation4.ScaleFactor = 0.0050799999386072162
    DataRepresentation4.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    DataRepresentation4.SelectionPointFieldDataArrayName = 'PRESSURE'
    DataRepresentation4.SelectionCellFieldDataArrayName = 'PRESSURE'

    a1_PRESSURE_PVLookupTable = GetLookupTableForArray( "PRESSURE", 1, RGBPoints=[31221.053294090299, 0.23000000000000001, 0.29899999999999999, 0.754, 31744.814032097096, 0.86499999999999999, 0.86499999999999999, 0.86499999999999999, 32268.574770103893, 0.70599999999999996, 0.016, 0.14999999999999999], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

    a1_PRESSURE_PiecewiseFunction = CreatePiecewiseFunction( Points=[31221.053294090299, 0.0, 0.5, 0.0, 32268.574770103893, 1.0, 0.5, 0.0] )

    DataRepresentation4.ColorArrayName = ('POINT_DATA', 'PRESSURE')
    DataRepresentation4.LookupTable = a1_PRESSURE_PVLookupTable

    # DataRepresentation3.Visibility = 0

    # DataRepresentation1.Visibility = 0

    RenderView1.CameraViewUp = [-0.28226359121893679, 0.79763654762218528, -0.53301332344468688]
    RenderView1.CameraPosition = [-0.083261624296263742, -0.10139085621914616, -0.089200021973301097]
    RenderView1.CameraClippingRange = [0.088706156398575015, 0.2548696042949255]
    # return


    SetActiveSource(CellDatatoPointData1)
    Clip1 = Clip( ClipType="Plane" )

    # Clip1.Scalars = ['POINTS', 'DENSITY']
    # Clip1.ClipType.Origin = [0.0, 0.0, 0.018435800448060036]
    # Clip1.ClipType = "Plane"
    # Clip1.Value = 3936.18994140625

    # # toggle the 3D widget visibility.
    # active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
    # RenderView1.CameraClippingRange = [0.10727958993603862, 0.24868365525694414]

    # toggle the 3D widget visibility.
    active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
    RenderView1.CameraClippingRange = [0.11770729481791534, 0.23555732428522624]

    Clip1.Scalars = ['POINTS', 'VOLFRC2']
    Clip1.ClipType = "Scalar"
    Clip1.Value = 0.5

    # DataRepresentation3 = Show()
    # DataRepresentation3.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    # DataRepresentation3.SelectionPointFieldDataArrayName = 'DENSITY'
    # DataRepresentation3.SelectionCellFieldDataArrayName = 'DENSITY'
    # # DataRepresentation3.ScalarOpacityUnitDistance = 0.00049793065251967571
    # # DataRepresentation3.ExtractedBlockIndex = 2
    # DataRepresentation3.ScaleFactor = 0.0050799999386072162

    # # DataRepresentation2.Visibility = 0

    # RenderView1.CameraClippingRange = [0.15140449219932237, 0.21870872559452276]

    Clip2 = Clip( ClipType="Plane" )

    Clip2.Scalars = ['POINTS', 'VOLFRC2']
    Clip2.ClipType.Origin = [-0.0012411912903189659, 0.0, 0.0071280160918831825]
    Clip2.ClipType = "Plane"
    Clip2.Value = 3317.7668240797921

    # # toggle the 3D widget visibility.
    # active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
    # RenderView1.CameraClippingRange = [0.14545272476588764, 0.22620077349671941]

    # # toggle the 3D widget visibility.
    # active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
    RenderView1.CameraClippingRange = [0.15140449219932237, 0.21870872559452276]

    Clip2.InsideOut = 1
    Clip2.ClipType.Normal = [0.0, 1.0, 0.0]

    DataRepresentationClip = Show()
    DataRepresentationClip.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    DataRepresentationClip.SelectionPointFieldDataArrayName = 'DENSITY'
    DataRepresentationClip.SelectionCellFieldDataArrayName = 'DENSITY'
    # DataRepresentation3.ScalarOpacityUnitDistance = 0.00049793065251967571
    # DataRepresentation3.ExtractedBlockIndex = 2
    DataRepresentationClip.ScaleFactor = 0.0050799999386072162 

    # AnimationScene1.AnimationTime = 2.0010922980873147e-06
    for i in range(len(files)):
        print "rendering frame " + str(i)
        AnimationScene1.AnimationTime = 2.000108543143142e-05*float(i)/float(len(files))

    return()
    # DataRepresentation3.Visibility=0

    Whipple_Shield_exo_300_ = ExodusIIReader( FileName=['/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.000', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.001'] )
    #, '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.002', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.003', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.004', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.005', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.006', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.007', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.008', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.009', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.010', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.011', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.012', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.013', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.014', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.015', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.016', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.017', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.018', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.019', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.020', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.021', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.022', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.023', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.024', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.025', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.026', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.027', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.028', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.029', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.030', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.031', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.032', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.033', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.034', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.035', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.036', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.037', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.038', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.039', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.040', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.041', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.042', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.043', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.044', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.045', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.046', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.047', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.048', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.049', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.050', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.051', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.052', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.053', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.054', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.055', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.056', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.057', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.058', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.059', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.060', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.061', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.062', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.063', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.064', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.065', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.066', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.067', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.068', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.069', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.070', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.071', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.072', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.073', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.074', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.075', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.076', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.077', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.078', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.079', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.080', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.081', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.082', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.083', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.084', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.085', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.086', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.087', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.088', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.089', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.090', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.091', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.092', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.093', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.094', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.095', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.096', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.097', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.098', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.099', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.100', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.101', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.102', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.103', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.104', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.105', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.106', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.107', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.108', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.109', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.110', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.111', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.112', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.113', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.114', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.115', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.116', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.117', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.118', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.119', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.120', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.121', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.122', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.123', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.124', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.125', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.126', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.127', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.128', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.129', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.130', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.131', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.132', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.133', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.134', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.135', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.136', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.137', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.138', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.139', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.140', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.141', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.142', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.143', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.144', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.145', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.146', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.147', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.148', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.149', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.150', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.151', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.152', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.153', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.154', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.155', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.156', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.157', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.158', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.159', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.160', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.161', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.162', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.163', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.164', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.165', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.166', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.167', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.168', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.169', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.170', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.171', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.172', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.173', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.174', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.175', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.176', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.177', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.178', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.179', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.180', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.181', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.182', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.183', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.184', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.185', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.186', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.187', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.188', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.189', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.190', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.191', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.192', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.193', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.194', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.195', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.196', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.197', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.198', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.199', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.200', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.201', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.202', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.203', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.204', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.205', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.206', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.207', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.208', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.209', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.210', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.211', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.212', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.213', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.214', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.215', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.216', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.217', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.218', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.219', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.220', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.221', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.222', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.223', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.224', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.225', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.226', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.227', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.228', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.229', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.230', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.231', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.232', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.233', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.234', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.235', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.236', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.237', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.238', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.239', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.240', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.241', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.242', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.243', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.244', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.245', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.246', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.247', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.248', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.249', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.250', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.251', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.252', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.253', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.254', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.255', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.256', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.257', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.258', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.259', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.260', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.261', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.262', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.263', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.264', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.265', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.266', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.267', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.268', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.269', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.270', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.271', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.272', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.273', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.274', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.275', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.276', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.277', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.278', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.279', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.280', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.281', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.282', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.283', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.284', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.285', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.286', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.287', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.288', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.289', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.290', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.291', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.292', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.293', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.294', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.295', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.296', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.297', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.298', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.299'] )

    # AnimationScene1 = GetAnimationScene()
    # AnimationScene1.EndTime = 2.000108543143142e-05
    # AnimationScene1.PlayMode = 'Snap To TimeSteps'

    Whipple_Shield_exo_300_.FileRange = [0, 1]
    Whipple_Shield_exo_300_.XMLFileName = 'Invalid result'
    Whipple_Shield_exo_300_.FilePrefix = '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.'
    Whipple_Shield_exo_300_.ModeShape = 20
    Whipple_Shield_exo_300_.FilePattern = '%s%03i'

    Whipple_Shield_exo_300_.NodeSetArrayStatus = []
    Whipple_Shield_exo_300_.ElementVariables = ['VOID_FRC', 'VOLFRC1', 'VOLFRC2', 'DENSITY', 'TEMPERATURE', 'PRESSURE']
    Whipple_Shield_exo_300_.ElementBlocks = ['Unnamed block ID: 1 Type: HEX']

    RenderView1 = GetRenderView()
    RenderView1.CenterOfRotation = [0.0, 0.0, 0.018435800448060036]

    DataRepresentation1 = Show()
    DataRepresentation1.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    DataRepresentation1.SelectionPointFieldDataArrayName = 'GlobalNodeId'
    DataRepresentation1.SelectionCellFieldDataArrayName = 'DENSITY'
    # DataRepresentation1.ScalarOpacityUnitDistance = 0.00028215277189116728
    # DataRepresentation1.ExtractedBlockIndex = 2
    DataRepresentation1.ScaleFactor = 0.0050799999386072162

    RenderView1.CameraPosition = [0.0, 0.0, 0.18813575352296963]
    RenderView1.CameraFocalPoint = [0.0, 0.0, 0.018435800448060036]
    RenderView1.CameraClippingRange = [0.11770729481791534, 0.23555732428522624]
    RenderView1.CameraParallelScale = 0.043921579808790676

    CellDatatoPointData1 = CellDatatoPointData()

    SetActiveSource(CellDatatoPointData1)
    Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'DENSITY']
    Contour1.Isosurfaces = [3936.18994140625]

    Contour1.Isosurfaces = [0.5]
    Contour1.ContourBy = ['POINTS', 'VOLFRC1']

    DataRepresentation2 = Show()
    DataRepresentation2.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    DataRepresentation2.SelectionPointFieldDataArrayName = 'DENSITY'
    DataRepresentation2.SelectionCellFieldDataArrayName = 'DENSITY'
    # DataRepresentation2.ScalarOpacityUnitDistance = 0.00028215277189116728
    # DataRepresentation2.ExtractedBlockIndex = 2
    DataRepresentation2.ScaleFactor = 0.0050799999386072162


    DataRepresentation1.Visibility = 0
    ResetCamera()
    return

    Clip1 = Clip( ClipType="Plane" )

    Clip1.Scalars = ['POINTS', 'DENSITY']
    Clip1.ClipType.Origin = [0.0, 0.0, 0.018435800448060036]
    Clip1.ClipType = "Plane"
    Clip1.Value = 3936.18994140625

    # toggle the 3D widget visibility.
    active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
    RenderView1.CameraClippingRange = [0.10727958993603862, 0.24868365525694414]

    # toggle the 3D widget visibility.
    active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
    RenderView1.CameraClippingRange = [0.11770729481791534, 0.23555732428522624]

    Clip1.Scalars = ['POINTS', 'VOLFRC2']
    Clip1.ClipType = "Scalar"
    Clip1.Value = 0.5

    DataRepresentation3 = Show()
    DataRepresentation3.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    DataRepresentation3.SelectionPointFieldDataArrayName = 'DENSITY'
    DataRepresentation3.SelectionCellFieldDataArrayName = 'DENSITY'
    # DataRepresentation3.ScalarOpacityUnitDistance = 0.00049793065251967571
    # DataRepresentation3.ExtractedBlockIndex = 2
    DataRepresentation3.ScaleFactor = 0.0050799999386072162

    DataRepresentation2.Visibility = 0

    RenderView1.CameraClippingRange = [0.15140449219932237, 0.21870872559452276]

    Clip2 = Clip( ClipType="Plane" )

    Clip2.Scalars = ['POINTS', 'DENSITY']
    Clip2.ClipType.Origin = [-0.0012411912903189659, 0.0, 0.0071280160918831825]
    Clip2.ClipType = "Plane"
    Clip2.Value = 3317.7668240797921

    # toggle the 3D widget visibility.
    active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
    RenderView1.CameraClippingRange = [0.14545272476588764, 0.22620077349671941]

    # toggle the 3D widget visibility.
    active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
    RenderView1.CameraClippingRange = [0.15140449219932237, 0.21870872559452276]

    Clip2.InsideOut = 1
    Clip2.ClipType.Normal = [0.0, 1.0, 0.0]

    DataRepresentation4 = Show()
    DataRepresentation4.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    DataRepresentation4.SelectionPointFieldDataArrayName = 'DENSITY'
    DataRepresentation4.SelectionCellFieldDataArrayName = 'DENSITY'
    # DataRepresentation4.ScalarOpacityUnitDistance = 0.00050973077886331262
    # DataRepresentation4.ExtractedBlockIndex = 2
    DataRepresentation4.ScaleFactor = 0.0048317616805434232

    DataRepresentation3.Visibility = 0

    SetActiveSource(CellDatatoPointData1)
    Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'DENSITY']
    Contour1.Isosurfaces = [3936.18994140625]

    Contour1.Isosurfaces = [0.5]
    Contour1.ContourBy = ['POINTS', 'VOLFRC1']

    DataRepresentation5 = Show()
    DataRepresentation5.ScaleFactor = 0.00063445850537391379
    DataRepresentation5.EdgeColor = [0.0, 0.0, 0.50000762951094835]
    DataRepresentation5.SelectionPointFieldDataArrayName = 'DENSITY'
    DataRepresentation5.SelectionCellFieldDataArrayName = 'DENSITY'

    a1_PRESSURE_PVLookupTable = GetLookupTableForArray( "PRESSURE", 1, RGBPoints=[31221.053294090299, 0.23000000000000001, 0.29899999999999999, 0.754, 31744.814032097096, 0.86499999999999999, 0.86499999999999999, 0.86499999999999999, 32268.574770103893, 0.70599999999999996, 0.016, 0.14999999999999999], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

    a1_PRESSURE_PiecewiseFunction = CreatePiecewiseFunction( Points=[31221.053294090299, 0.0, 0.5, 0.0, 32268.574770103893, 1.0, 0.5, 0.0] )

    DataRepresentation5.ColorArrayName = ('POINT_DATA', 'PRESSURE')
    DataRepresentation5.LookupTable = a1_PRESSURE_PVLookupTable
    DataRepresentation5.Visibility = 0

    RenderView1.CameraClippingRange = [0.002091118926200427, 2.0911189262004268]

    # AnimationScene1.AnimationTime = 2.0010922980873147e-06

    DataRepresentation4.Visibility = 0
    ResetCamera()

    Render()



def svbRender():
  Render()
