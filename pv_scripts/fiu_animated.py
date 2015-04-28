try: paraview.simple
except: from paraview.simple import *

u_380x380x828_frame0010_subs00_nhdr = NrrdReader( FileName='/work/01336/carson/intelTACC/data/fiu/u_380x380x828_frame0010_subs00.nhdr' )
rho_380x380x828_frame0010_subs00_nhdr = NrrdReader( FileName='/work/01336/carson/intelTACC/data/fiu/rho_380x380x828_frame0010_subs00.nhdr' )

streamlineResults = []
numberOfStreamlines = 1000

# source - vector source
# source2 - scalar source
# time - time in animation, 0 - 1
def createStreamlines(source, source2, time):
  length = time*700.0
  if (length < 0.5):
    return;
  # global writerIndex

  # u_380x380x828_frame0010_subs00_nhdr = NrrdReader( FileName='/scratch/01336/carson/intelTACC/FIU/u_380x380x828_frame0010_subs00.nhdr' )
  # source = u_380x380x828_frame0010_subs00_nhdr
  SetActiveSource(source)

  RenderView1 = GetRenderView()
  # DataRepresentation3 = Show()
  # DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  # DataRepresentation3.SelectionPointFieldDataArrayName = 'ImageFile'
  # #DataRepresentation3.ScalarOpacityUnitDistance = 2.0047589136882165
  # DataRepresentation3.Representation = 'Outline'
  # DataRepresentation3.ScaleFactor = 82.7

  StreamTracer1 = StreamTracer( SeedType="Point Source" )

  RenderView1.CameraClippingRange = [1061.9371333317906, 2968.215646799765]

  StreamTracer1.SeedType.Center = [189.5, 189.5, 413.5]
  StreamTracer1.SeedType.Radius = 82.7
  StreamTracer1.Vectors = ['POINTS', 'ImageFile']
  StreamTracer1.SeedType = "Point Source"
  StreamTracer1.MaximumStreamlineLength = 8.0
  active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')

  a3_ImageFile_PVLookupTable = GetLookupTableForArray( "ImageFile", 3, RGBPoints=[0.0, 0.133333333333333, 0.254901960784314, 0.407843137254902, 0.00556127075105906, 0.247058823529412, 0.407843137254902, 0.854901960784314, 0.0102825257927179, 1.0, 1.0, 1.0, 0.0191711561615985, 1.0, 1.0, 1.0], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0, AllowDuplicateScalars=1 )

  a3_ImageFile_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0] )

  #
  # to show streamlines as lines
  #
  # DataRepresentation4 = Show()
  # DataRepresentation4.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  # DataRepresentation4.SelectionPointFieldDataArrayName = 'ImageFile'
  # DataRepresentation4.SelectionCellFieldDataArrayName = 'ReasonForTermination'
  # DataRepresentation4.ColorArrayName = 'ImageFile'
  # DataRepresentation4.LookupTable = a3_ImageFile_PVLookupTable
  # DataRepresentation4.ScaleFactor = 82.70055550341495

  StreamTracer1.SeedType.Radius = 60.0
  StreamTracer1.SeedType.NumberOfPoints = numberOfStreamlines
  #StreamTracer1.SeedType.NumberOfPoints = 300
  StreamTracer1.MaximumStreamlineLength = length
  # StreamTracer1.MaximumPropagation = length

  a3_ImageFile_PVLookupTable.ScalarOpacityFunction = a3_ImageFile_PiecewiseFunction
  # """

  Tube1 = Tube()

  RenderView1.OrientationAxesVisibility = 0
  RenderView1.CameraClippingRange = [1061.9316971233097, 2968.2226978297904]

  Tube1.Scalars = ['POINTS', 'AngularVelocity']
  Tube1.Vectors = ['POINTS', 'Normals']
  Tube1.Radius = 8.270055550341494
  Tube1.VaryRadius = 'By Scalar'
  Tube1.NumberofSides = 6
  Tube1.Radius = 0.05270055550341494
  Tube1.RadiusFactor = 20.0

  # DataRepresentation5 = Show()
  # DataRepresentation5.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  # DataRepresentation5.SelectionPointFieldDataArrayName = 'ImageFile'
  # DataRepresentation5.SelectionCellFieldDataArrayName = 'ReasonForTermination'
  # #CARSON DEBUG: for some reason making this a function it now complains that ImageFile field doesn't exist.  We need this for the colormap
  # # DataRepresentation5.ColorArrayName = "ImageFile"
  # DataRepresentation5.LookupTable = a3_ImageFile_PVLookupTable
  # DataRepresentation5.ScaleFactor = 82.95756218433381

  # DataRepresentation4.Visibility = 0

  a3_ImageFile_PVLookupTable.RGBPoints = [0.0, 0.133333333333333, 0.254901960784314, 0.407843137254902, 0.005595855680303297, 0.247058823529412, 0.407843137254902, 0.854901960784314, 0.010346471686185769, 1.0, 1.0, 1.0, 0.01929037946667726, 1.0, 1.0, 1.0]

  # Tube1.Radius = 0.07270055550341494
  #Tube1.Radius = 0.05270055550341494
  # Tube1.RadiusFactor = 20.0

  RenderView1.CameraClippingRange = [1059.365355735317, 2971.4323511683565]


  a3_ImageFile_PVLookupTable.NanColor = [0.2500038147554742, 0.0, 0.0]
  a3_ImageFile_PVLookupTable.RGBPoints = [0.0, 0.13333333333333333, 0.2549019607843137, 0.40784313725490196, 0.0019700811244547367, 0.24705882352941178, 0.40784313725490196, 0.8549019607843137, 0.004859533626586199, 1.0, 1.0, 1.0, 0.01929037946667726, 1.0, 1.0, 1.0]

  a3_ImageFile_PiecewiseFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.01929037946667726, 1.0, 0.5, 0.0]

  # di = source.GetDataInformation()
  # pdinfo=di.GetPointDataInformation()
  # print "pdinfo " + str(pdinfo)
  # print "array0: " + str(pdinfo.GetArrayInformation(0).GetName())
  # print "array1: " + str(pdinfo.GetArrayInformation(1).GetName())


  # """
  DataRepresentation6 = Show()
  DataRepresentation6.ScaleFactor = 300.0
  # DataRepresentation6.SelectionPointFieldDataArrayName = 'Normals'
  DataRepresentation6.SelectionPointFieldDataArrayName = 'POINTS'
  DataRepresentation6.LookupTable = a3_ImageFile_PVLookupTable
  # DataRepresentation6.ColorArrayName = 'AngularVelocity'
  DataRepresentation6.ColorArrayName = 'ImageFile'
  # DataRepresentation6.ColorArrayName = pdinfo.GetArrayInformation(0).GetName()
  # DataRepresentation6.EdgeColor = [0.0, 0.0, 0.5000076295109483]

  # rho_380x380x828_frame0010_subs00_nhdr = NrrdReader( FileName='/scratch/01336/carson/intelTACC/FIU/rho_380x380x828_frame0010_subs00.nhdr' )
  SetActiveSource(source2)
  originz = -800.0+(430.92--800.0)*time

  #DataRepresentation1 = Show()
  #DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #DataRepresentation1.SelectionPointFieldDataArrayName = 'ImageFile'
  #DataRepresentation1.ScalarOpacityUnitDistance = 2.0047589136882165
  #DataRepresentation1.Representation = 'Outline'
  #DataRepresentation1.ScaleFactor = 82.7

  Contour1 = Contour( PointMergeMethod="Uniform Binning" )
  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'ImageFile']
  #Contour1.Isosurfaces = [0.503040273885536]
  Contour1.Isosurfaces = [0.3]

  #DataRepresentation2 = Show()
  #DataRepresentation2.ScaleFactor = 82.7
  #DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
  #DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]

  Clip1 = Clip( ClipType="Plane" )

  #DataRepresentation2.DiffuseColor = [0.6823529411764706, 0.4627450980392157, 0.08627450980392157]

  Clip1.Scalars = ['POINTS', '']
  # Clip1.ClipType.Origin = [192.49998569488525, 189.50039958953857, originz]
  Clip1.ClipType = "Plane"

  Clip1.InsideOut = 1

  Clip1.ClipType.Origin = [230.97, 220.84, originz]
  #Clip1.ClipType.Origin = [-230.97, 220.84, 430.92]
  Clip1.ClipType.Normal = [0.69, 0.65, 0.3]
  # Show()

  DataRepresentation3 = Show()
  DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #DataRepresentation3.SelectionPointFieldDataArrayName = 'Normals'
  #DataRepresentation3.DiffuseColor = [1.0, 1.0, 1.0]
  DataRepresentation3.DiffuseColor = [0.6823529411764706, 0.4627450980392157, 0.08627450980392157]
  #DataRepresentation3.DiffuseColor = [0.7823529411764706, 0.4627450980392157, 0.08627450980392157]
  #DataRepresentation3.ScalarOpacityUnitDistance = 4.932379654708959
  DataRepresentation3.ScaleFactor = 82.7

  #DataRepresentation2.Visibility = 0

  # writerIndex += 1

  return {'slRepresentation':DataRepresentation6,'cRepresentation':DataRepresentation3}



def svbGetStagesSize():
  return 5;

def svbSetup(geometryLevel=1, stage=0):
  RenderView1 = GetRenderView()

  AnimationScene1 = GetAnimationScene()
  CameraAnimationCue1 = GetCameraTrack()
  CameraAnimationCue1.Mode = 'Interpolate Camera'

  TimeAnimationCue1 = GetTimeTrack()

  KeyFrame3196 = CameraKeyFrame( FocalPathPoints=[189.45121002197266, 190.12999725341797, 416.1247253417969], FocalPoint=[286.0130337520959, 178.34157026957035, 157.68427564227449], PositionPathPoints=[189.45121002197266, 314.3047150387376, 719.0042288897554, 329.16238822864443, 412.99678271403013, 610.9747621113049, 415.5086449686611, 426.56131330679966, 428.5192039960692, 415.5086449686611, 349.81711717204604, 241.3293763077366, 329.1623882286443, 212.07786879395684, 120.90543087501385, 189.4512100219726, 65.95527946809835, 113.24522179383854, 49.740031815300966, -32.73678820719408, 221.27468857228894, -36.60622492471566, -46.30131879996361, 403.7302466875246, -36.606224924715576, 30.442877334789983, 590.9200743758572, 49.74003181530114, 168.1821257128791, 711.3440198085798], ClosedPositionPath=1, Position=[225.4620337520957, 327.54657026957045, 672.7672756422737], ViewUp=[-0.6875730560667721, 0.6718440547841821, -0.27544302246045105] )

  KeyFrame3197 = CameraKeyFrame( Position=[225.4620337520957, 327.54657026957045, 672.7672756422737], ViewUp=[-0.6875730560667721, 0.6718440547841821, -0.27544302246045105], KeyTime=0.6, FocalPoint=[286.0130337520959, 178.34157026957035, 157.68427564227449] )
  #KeyFrame3197 = CameraKeyFrame( Position=[225.4620337520957, 327.54657026957045, 672.7672756422737], ViewUp=[-0.6875730560667721, 0.6718440547841821, -0.27544302246045105], KeyTime=1.0, FocalPoint=[286.0130337520959, 178.34157026957035, 157.68427564227449] )

  #KeyFrame3196 = CameraKeyFrame( FocalPathPoints=[189.45121002197266, 190.12999725341797, 416.1247253417969], FocalPoint=[286.0130337520959, 178.34157026957035, 157.68427564227449], PositionPathPoints=[189.45121002197266, 314.3047150387376, 719.0042288897554, 329.16238822864443, 412.99678271403013, 610.9747621113049, 415.5086449686611, 426.56131330679966, 428.5192039960692, 415.5086449686611, 349.81711717204604, 241.3293763077366, 329.1623882286443, 212.07786879395684, 120.90543087501385, 189.4512100219726, 65.95527946809835, 113.24522179383854, 49.740031815300966, -32.73678820719408, 221.27468857228894, -36.60622492471566, -46.30131879996361, 403.7302466875246, -36.606224924715576, 30.442877334789983, 590.9200743758572, 49.74003181530114, 168.1821257128791, 711.3440198085798], ClosedPositionPath=1, Position=[225.4620337520957, 327.54657026957045, 672.7672756422737], ViewUp=[-0.6875730560667721, 0.6718440547841821, -0.27544302246045105] )

  #KeyFrame3197 = CameraKeyFrame( Position=[225.4620337520957, 327.54657026957045, 672.7672756422737], ViewUp=[-0.6875730560667721, 0.6718440547841821, -0.27544302246045105], KeyTime=1.0, FocalPoint=[286.0130337520959, 178.34157026957035, 157.68427564227449] )

  RenderView1.CameraFocalPoint = [286.0130337520959, 178.34157026957035, 157.68427564227449]
  RenderView1.CameraClippingRange = [4.7891677655235645, 4789.167765523564]
  RenderView1.CameraPosition = [225.4620337520957, 327.54657026957045, 672.7672756422737]


  CameraAnimationCue1.KeyFrames = [ KeyFrame3196, KeyFrame3197 ]

  RenderView1.CameraViewUp = [-0.6976752257395223, 0.7157372315836574, 0.031136710074581617]
  RenderView1.CameraPosition = [198.095, 180.662, 802.466]
  RenderView1.CameraFocalPoint = [179.604, 186.099, 263.144]
  RenderView1.CameraClippingRange = [4.173792286478831, 4173.792286478831]

  #KeyFrame3196.Position = [225.462, 327.547, 672.767]
  #KeyFrame3196.ViewUp = [-0.687573, 0.671844, -0.275443]
  #KeyFrame3196.FocalPoint = [286.013, 178.342, 157.684]
  #KeyFrame3196.ViewAngle = 30.0

  #KeyFrame3196.Position = [213.457, 315.566, 707.492]
  #KeyFrame3196.ViewUp = [-0.687573, 0.671844, -0.275443]
  #KeyFrame3196.FocalPoint = [272.785, 168.755, 192.033]
  #KeyFrame3196.ViewAngle = 30.0

  KeyFrame3196.Position = [219.457, 279.266, 581.192]
  KeyFrame3196.ViewUp = [-0.687573, 0.671844, -0.275443]
  KeyFrame3196.FocalPoint = [278.785, 132.755, 65.033]
  KeyFrame3196.ViewAngle = 60.0

  #KeyFrame3197.Position = [225.462, 327.547, 672.767]
  #KeyFrame3197.ViewUp = [-0.687573, 0.671844, -0.275443]
  #KeyFrame3197.FocalPoint = [286.013, 178.342, 157.684]
  #KeyFrame3197.ViewAngle = 30.0

  KeyFrame3197.Position = [225.462, 327.547, 672.767]
  KeyFrame3197.ViewUp = [-0.687573, 0.671844, -0.275443]
  KeyFrame3197.FocalPoint = [286.013, 178.342, 157.684]
  KeyFrame3197.ViewAngle = 50.0

  KeyFrame3197.Position = [198.095, 180.662, 802.466]
  KeyFrame3197.ViewUp = [-0.697675, 0.715737, 0.0311367]
  KeyFrame3197.FocalPoint = [179.604, 186.099, 263.144]

  AnimationScene1.AnimationTime = 0.0
  AnimationScene1.Caching = 0


  # KeyFrameAnimationCue1 = GetAnimationTrack( 'MaximumPropagation' )

  # KeyFrame3231 = CompositeKeyFrame()

  # KeyFrame3232 = CompositeKeyFrame( KeyTime=1.0, KeyValues=[700.0] )
  # KeyFrameAnimationCue1.KeyFrames = [ KeyFrame3231, KeyFrame3232 ]

  RenderView1.CameraViewUp = [-0.687573056066772, 0.671844054784182, -0.27544302246045127]
  RenderView1.CacheKey = 1.0
  RenderView1.CameraPosition = [225.462, 327.547, 672.767]
  RenderView1.CameraClippingRange = [4.789167518263233, 4789.167518263233]
  RenderView1.ViewTime = 0.0
  RenderView1.UseCache = 0
  RenderView1.CameraFocalPoint = [286.013, 178.342, 157.684]

  #try:
    #parser = PassThroughOptionParser()
    #parser.add_option("--numStreamlines", action="store", dest="numStreamlines",type="int",
      #default=100, help="number of streamlines")
    #(options, args) = parser.parse_args()
    #numStreamlines = options.numStreamlines
  #except:
    #pass
  
  numStreamlines = 1000
  useContour = True
  #if (geometryLevel == 0):
    #numStreamlines = 1
    #useContour = False
  #if (geometryLevel == 1):
    #numStreamlines = 1000
  #if (geometryLevel == 2):
    #numStreamlines = 2000
  #if (geometryLevel == 3):
    #numStreamlines = 4000
  #if (geometryLevel == 4):
    #numStreamlines = 8000
  #if (geometryLevel == 5):
    #numStreamlines = 16000
  #if (geometryLevel == 6):
    #numStreamlines = 32000
  def computeStreamlines(x):
    return {
        0:10,
        1:500,
        2:1,
        3:100,
        4:1000,
        5:2000,
        6:4000,
        7:8000,
        8:16000,
        9:32000,
        }.get(x,9)
  numStreamlines = computeStreamlines(geometryLevel)
  if geometryLevel < 2:
    useContour = False

  numCells = 0
  numPolys = 0 
  numPoints = 0


  #streamlineResults = []
  streamIndex = 0
  i=stage
  frames = svbGetStagesSize()
  AnimationScene1.AnimationTime = 0.0
  print "animation frame " + str(i+1) + "/" + str(frames)
  # st = time.time()
  lerp = float(i)/float(frames)
  if (lerp > 0.0):
    if len(streamlineResults) <= streamIndex:
      streamlineResults.append(createStreamlines(u_380x380x828_frame0010_subs00_nhdr, rho_380x380x828_frame0010_subs00_nhdr, lerp))
    if len(streamlineResults) > 0:
      streamlineResults[(streamIndex-1)%len(streamlineResults)]['slRepresentation'].Visibility = 0
      streamlineResults[(streamIndex-1)%len(streamlineResults)]['cRepresentation'].Visibility = 0
    streamlineResults[streamIndex]['slRepresentation'].Visibility = 1
    streamlineResults[streamIndex]['cRepresentation'].Visibility = 1
    streamIndex+=1
  AnimationScene1.AnimationTime = lerp

  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))
  

def svbRender():
  Render()
