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


streamlineResults = []
numberOfStreamlines = 1000

# source - vector source
# source2 - scalar source
# time - time in animation, 0 - 1
def createStreamlines(source, source2, t):
  length = t*700.0
  if (length < 0.5):
    return;
  SetActiveSource(source)
  RenderView1 = GetRenderView()
  st_filter_streamline = time.time()
  StreamTracer1 = StreamTracer( SeedType="Point Source" )
  StreamTracer1.SeedType.Center = [189.5, 189.5, 413.5]
  StreamTracer1.SeedType.Radius = 82.7
  StreamTracer1.Vectors = ['POINTS', 'ImageFile']
  StreamTracer1.SeedType = "Point Source"
  StreamTracer1.MaximumStreamlineLength = 8.0
  active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')

  a3_ImageFile_PVLookupTable = GetLookupTableForArray( "ImageFile", 3, RGBPoints=[0.0, 0.133333333333333, 0.254901960784314, 0.407843137254902, 0.00556127075105906, 0.247058823529412, 0.407843137254902, 0.854901960784314, 0.0102825257927179, 1.0, 1.0, 1.0, 0.0191711561615985, 1.0, 1.0, 1.0], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0, AllowDuplicateScalars=1 )

  a3_ImageFile_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0] )
  StreamTracer1.SeedType.Radius = 60.0
  StreamTracer1.SeedType.NumberOfPoints = numberOfStreamlines
  #StreamTracer1.SeedType.NumberOfPoints = 300
  StreamTracer1.MaximumStreamlineLength = length
  # StreamTracer1.MaximumPropagation = length

  a3_ImageFile_PVLookupTable.ScalarOpacityFunction = a3_ImageFile_PiecewiseFunction
  # """


  RenderView1.CameraViewUp = [-0.6976752257395223, 0.7157372315836574, 0.031136710074581617]
  RenderView1.CameraPosition = [198.095, 180.662, 902.466]
  RenderView1.CameraFocalPoint = [179.604, 186.099, 263.144]
  #RenderView1.CameraClippingRange = [4.173792286478831, 4173.792286478831]


  Tube1 = Tube()

  RenderView1.OrientationAxesVisibility = 0
  #RenderView1.CameraClippingRange = [1061.9316971233097, 2968.2226978297904]

  Tube1.Scalars = ['POINTS', 'AngularVelocity']
  Tube1.Vectors = ['POINTS', 'Normals']
  Tube1.Radius = 8.270055550341494
  Tube1.VaryRadius = 'By Scalar'
  Tube1.NumberofSides = 6
  Tube1.Radius = 0.05270055550341494
  Tube1.RadiusFactor = 20.0


  a3_ImageFile_PVLookupTable.RGBPoints = [0.0, 0.133333333333333, 0.254901960784314, 0.407843137254902, 0.005595855680303297, 0.247058823529412, 0.407843137254902, 0.854901960784314, 0.010346471686185769, 1.0, 1.0, 1.0, 0.01929037946667726, 1.0, 1.0, 1.0]


  #RenderView1.CameraClippingRange = [1059.365355735317, 2971.4323511683565]


  a3_ImageFile_PVLookupTable.NanColor = [0.2500038147554742, 0.0, 0.0]
  a3_ImageFile_PVLookupTable.RGBPoints = [0.0, 0.13333333333333333, 0.2549019607843137, 0.40784313725490196, 0.0019700811244547367, 0.24705882352941178, 0.40784313725490196, 0.8549019607843137, 0.004859533626586199, 1.0, 1.0, 1.0, 0.01929037946667726, 1.0, 1.0, 1.0]

  a3_ImageFile_PiecewiseFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.01929037946667726, 1.0, 0.5, 0.0]

  Tube1.UpdatePipeline()
  StreamTracer1.UpdatePipeline()
  et_filter_streamline = time.time()
  tt_filter_streamline = (et_filter_streamline-st_filter_streamline)
  DataRepresentation6 = Show()

  #DataRepresentation6.ScaleFactor = 300.0
  DataRepresentation6.SelectionPointFieldDataArrayName = 'POINTS'
  DataRepresentation6.LookupTable = a3_ImageFile_PVLookupTable
  DataRepresentation6.ColorArrayName = 'ImageFile'
  SetActiveSource(source2)
  originz = -800.0+(430.92--800.0)*t

  st_filter_contour = time.time()
  Contour1 = Contour(Input=source2)
  Contour1 = Contour( PointMergeMethod="Uniform Binning" )
  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'ImageFile']
  #Contour1.Isosurfaces = [0.503040273885536]
  Contour1.Isosurfaces = [0.3]


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

  Contour1.UpdatePipeline()
  Clip1.UpdatePipeline()
  et_filter_contour = time.time()
  tt_filter_contour = (et_filter_contour - st_filter_contour)

  DataRepresentation3 = Show()
  DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  DataRepresentation3.SelectionPointFieldDataArrayName = 'Normals'
  DataRepresentation3.DiffuseColor = [1.0, 1.0, 1.0]
  DataRepresentation3.DiffuseColor = [0.6823529411764706, 0.4627450980392157, 0.08627450980392157]
  DataRepresentation3.DiffuseColor = [0.7823529411764706, 0.4627450980392157, 0.08627450980392157]
  DataRepresentation3.ScalarOpacityUnitDistance = 4.932379654708959
  #DataRepresentation3.ScaleFactor = 82.7

  #DataRepresentation2.Visibility = 0

  # writerIndex += 1
  tt_filter_streamall = tt_filter_contour + tt_filter_streamline
  return {'slRepresentation':DataRepresentation6,'cRepresentation':DataRepresentation3,'tt_filter_streamall':tt_filter_streamall}



def svbGetStagesSize():
  return 5;

def svbSetup(geometryLevel=1, stage=0):


  global Contour1
  #readers
  global u_380x380x828_frame0010_subs00_nhdr
  global rho_380x380x828_frame0010_subs00_nhdr

  numCells = 0
  numPolys = 0
  numPoints = 0


  if(stage ==0):
    st_reader = time.time()
    u_380x380x828_frame0010_subs00_nhdr = NrrdReader( FileName=fiu_data_dir+"/u_380x380x828_frame0010_subs00.nhdr" )



    rho_380x380x828_frame0010_subs00_nhdr = NrrdReader( FileName=fiu_data_dir+"/rho_380x380x828_frame0010_subs00.nhdr" )
    rho_380x380x828_frame0010_subs00_nhdr.UpdatePipeline()
    u_380x380x828_frame0010_subs00_nhdr.UpdatePipeline()
    et_reader = time.time()
    tt_reader = (et_reader - st_reader)


  RenderView1 = GetRenderView()

  AnimationScene1 = GetAnimationScene()

  AnimationScene1.Caching = 0

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


    #streamlineResults = []
  streamIndex = 0
  i=stage
  tt_filter_all = -1
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
    tt_filter_all = streamlineResults[streamIndex]['tt_filter_streamall']
    streamIndex+=1

  print 'tt_filter_all: ' + str(tt_filter_all)
  AnimationScene1.AnimationTime = lerp

  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))


  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':tt_reader, 'tt_filter':tt_filter_all};
  return returnVals


def svbRender():
  Render()
