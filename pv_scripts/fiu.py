try: paraview.simple
except: from paraview.simple import *
import os
import sys
import time
#read in paths from the environment variables bash script generate by cmake
dir = os.path.dirname( os.path.dirname(os.path.abspath(__file__)))
pathsfile = os.path.join(dir,'paths.sh')
path_vars = dict()

with open(pathsfile) as f:
    print f
    next(f)
    for line in f:
        print line
        eq_index = line.find('=')
        var_name = line[:eq_index].strip()
        paths = line[eq_index + 1:].strip()
        path_vars[var_name] = paths

fiu_data_dir =  path_vars["FIUDATA_DIR"]
print "fiu_data_dir:%s" %  fiu_data_dir





def svbGetStagesSize():
  return 1;

def svbSetup(geometryLevel=1, stage=0):
  global Contour1
  global u_380x380x828_frame0010_subs00_nhdr
  global rho_380x380x828_frame0010_subs00_nhdr
   
  #try:
    #parser = PassThroughOptionParser()
    #parser.add_option("--numStreamlines", action="store", dest="numStreamlines",type="int",
      #default=100, help="number of streamlines")
    #(options, args) = parser.parse_args()
    #numStreamlines = options.numStreamlines
  #except   #pass
  
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
  returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':True, 'tt_reader':0, 'tt_filter':0};
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


  st_reader = time.time()
  u_380x380x828_frame0010_subs00_nhdr = NrrdReader( FileName=fiu_data_dir+"/u_380x380x828_frame0010_subs00.nhdr" )


  #RenderView1 = GetRenderView()
  #DataRepresentation1 = Show()
  #DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #DataRepresentation1.SelectionPointFieldDataArrayName = 'ImageFile'
  ##DataRepresentation1.ScalarOpacityUnitDistance = 2.0047589136882165
  #DataRepresentation1.Representation = 'Outline'
  #DataRepresentation1.ScaleFactor = 82.7

  #RenderView1.CenterOfRotation = [189.5, 189.5, 413.5]


  rho_380x380x828_frame0010_subs00_nhdr = NrrdReader( FileName=fiu_data_dir+"/rho_380x380x828_frame0010_subs00.nhdr" )
  rho_380x380x828_frame0010_subs00_nhdr.UpdatePipeline()
  u_380x380x828_frame0010_subs00_nhdr.UpdatePipeline()
  et_reader = time.time()
  tt_reader = (et_reader - st_reader)

  #RenderView1.CameraPosition = [189.5, 189.5, 2317.3405387189805]
  #RenderView1.CameraFocalPoint = [189.5, 189.5, 413.5]
  #RenderView1.CameraClippingRange = [1061.9371333317906, 2968.215646799765]
  #RenderView1.CameraParallelScale = 492.7501902587152

  #DataRepresentation2 = Show()
  #DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #DataRepresentation2.SelectionPointFieldDataArrayName = 'ImageFile'
  ##DataRepresentation2.ScalarOpacityUnitDistance = 2.0047589136882165
  #DataRepresentation2.Representation = 'Outline'
  #DataRepresentation2.ScaleFactor = 82.7

  st_filter_streamline = time.time()
  SetActiveSource(u_380x380x828_frame0010_subs00_nhdr)
  StreamTracer1 = StreamTracer( SeedType="Point Source" )

  StreamTracer1.SeedType.Center = [189.5, 189.5, 413.5]
  StreamTracer1.SeedType.Radius = 82.7
  print "number of streamlines: " + str(numStreamlines)
  StreamTracer1.SeedType.NumberOfPoints = numStreamlines
  StreamTracer1.Vectors = ['POINTS', 'ImageFile']
  StreamTracer1.SeedType = "Point Source"
  StreamTracer1.MaximumStreamlineLength = 827.0

  active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')

  Tube1 = Tube()
  Tube1.Scalars = ['POINTS','AngularVelocity']
  Tube1.Vectors = ['POINTS','Normals']
  Tube1.Radius = 1.0


  a3_ImageFile_PVLookupTable = GetLookupTableForArray( "ImageFile", 3, RGBPoints=[0.0, 0.23, 0.299, 0.754, 0.018618378756478694, 0.706, 0.016, 0.15], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0, AllowDuplicateScalars=1 )

  a3_ImageFile_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0] )

  StreamTracer1.SeedType.Radius = 60.0
  
  StreamTracer1.UpdatePipeline()
  Tube1.UpdatePipeline()
  et_filter_streamline = time.time()
  tt_filter_streamline = (et_filter_streamline-st_filter_streamline)
  DataRepresentation3 = Show()
  DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #DataRepresentation3.SelectionPointFieldDataArrayName = 'ImageFile'
 # DataRepresentation3.SelectionCellFieldDataArrayName = 'ReasonForTermination'
  DataRepresentation3.ColorArrayName = ('POINT_DATA','ImageFile')
  DataRepresentation3.LookupTable = a3_ImageFile_PVLookupTable
  #DataRepresentation3.ScaleFactor = 82.69024540111423

  
  a3_ImageFile_PVLookupTable.ScalarOpacityFunction = a3_ImageFile_PiecewiseFunction

  RenderView1 = GetRenderView()
  RenderView1.CameraViewUp = [0.1220323904995946, 0.9179892738319476, -0.3773642653967754]
  RenderView1.CameraPosition = [1641.8585346768702, 487.40856690408344, 1607.8676022842458]
  RenderView1.CameraClippingRange = [1021.8948997770883, 3018.6205689377375]
  RenderView1.CameraFocalPoint = [189.50000000000009, 189.5000000000001, 413.5]

  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))
  
  returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':True, 'tt_reader':tt_reader, 'tt_filter':tt_filter_streamline};
  return returnVals
  if (useContour):
    st_filter_contour = time.time()
    SetActiveSource(rho_380x380x828_frame0010_subs00_nhdr)
    Contour1 = Contour(Input=rho_380x380x828_frame0010_subs00_nhdr)

    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'ImageFile']
    Contour1.Isosurfaces = [0.503040273885536]

    Contour1.Isosurfaces = [0.3]

    Countour1.UpdatePipeline()
    et_filter_contour = time.time()
    tt_filter_contour = (et_filter_contour - st_filter_contour)
    DataRepresentation4 = Show()

    #DataRepresentation4.ScaleFactor = 82.7
    #DataRepresentation4.SelectionPointFieldDataArrayName = 'Normals'


    DataRepresentation4.EdgeColor = [0.0, 0.0, 0.5000076295109483]
    DataRepresentation4.DiffuseColor = [1.0, 0.71372549019607845, 0.21568627450980393]


    st_filter_clip = time.time()
    Clip1 = Clip( ClipType="Plane" )

    Clip1.Scalars = ['POINTS', '']
    Clip1.ClipType.Origin = [192.49998569488525, 189.50039958953857, 413.5]
    Clip1.ClipType = "Plane"

    active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')


    RenderView1.CameraClippingRange = [775.4151925055533, 3333.0640307903323]

    Clip1.ClipType.Normal = [0.7325209930676672, 0.663549941673441, 0.15203443563986424]
    #DataRepresentation4.Visibility = 0
    Clip1.InsideOut = 1

    Clip1.UpdatePipeline()
    et_filter_clip = time.time()
    tt_filter_clip = (et_filter_clip - st_filter_clip)
    DataRepresentation5 = Show()

    DataRepresentation5.ScaleFactor = 82.7
    DataRepresentation5.ScalarOpacityUnitDistance = 5.357494554385383
    DataRepresentation5.SelectionPointFieldDataArrayName = 'Normals'
    DataRepresentation5.EdgeColor = [0.0, 0.0, 0.5000076295109483]
    DataRepresentation5.DiffuseColor = [1.0, 0.71372549019607845, 0.21568627450980393]


    RenderView1.CameraClippingRange = [776.2726362511573, 3330.2827710502524]

    Clip1.ClipType.Normal = [0.7438769158737222, 0.5671401800076783, 0.3535521888647525]

    RenderView1.CameraViewUp = [0.1962873715201739, 0.9002484677398408, -0.3886180182567067]
    RenderView1.CameraFocalPoint = [189.50000000000014, 189.5000000000001, 413.49999999999994]
    RenderView1.CameraClippingRange = [1074.1386677858422, 2867.7684315317306]
    RenderView1.CameraPosition = [2008.3637843775757, -314.68686783528074, 164.22317987438336]

    Clip1.ClipType.Origin = [235.79504344847828, 222.5090416428755, 434.0774128880307]

    RenderView1.CameraClippingRange = [1110.3564373301474, 2842.7199687385264]

    Clip1.ClipType.Origin = [230.795043448478, 220.509041642876, 430.077412888031]
    Clip1.ClipType.Normal = [0.693876915873722, 0.657140180007678, 0.303552188864752]

    active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
    RenderView1.CameraClippingRange = [1316.9209663918095, 2647.243535334783]
    RenderView1.Background = [1.0,1.0,1.0]

    numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
    numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
    numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

    print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
    print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
    print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))

    tt_all = (tt_filter_streamlines + tt_filter_contour + tt_filter_clip)
    cam = GetActiveCamera()
    returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':True, 'tt_reader':tt_reader, 'tt_filter':tt_all};
    return returnVals


def svbRender():
  Render()