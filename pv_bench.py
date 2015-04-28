import sys
#rauseContour = options.use_contour
#sys.path = sys.path+['', '/opt/apps/intel13/mvapich2_1_9/visit/current/linux-x86_64/lib/site-packages/visit', '/opt/apps/intel13/mvapich2_1_9/
#araview/4.1.0/python2.7/lib/python2.7/site-packages', '/opt/apps/intel13/mvapich2_1_9/paraview/4.1.0/python2.7/lib/python2.7', '/opt/apps/intel13/mvapich2_1_9/paraview/4.1.0/lib/paraview-4.1/site-packages', '/scratch/01336/carson/ParaView-v4.1.0/build', '/opt/apps/python/epd/7.3.2/modules/lib/python', '/opt/apps/python/epd/7.3.2/lib', '/opt/apps/python/epd/7.3.2/lib/python27.zip', '/opt/apps/python/epd/7.3.2/lib/python2.7', '/opt/apps/python/epd/7.3.2/lib/python2.7/plat-linux2', '/opt/apps/python/epd/7.3.2/lib/python2.7/lib-tk', '/opt/apps/python/epd/7.3.2/lib/python2.7/lib-old', '/opt/apps/python/epd/7.3.2/lib/python2.7/lib-dynload', '/opt/apps/python/epd/7.3.2/lib/python2.7/site-packages', '/opt/apps/python/epd/7.3.2/lib/python2.7/site-packages/PIL']
#sys.path=sys.path+['', '/opt/apps/intel13/mvapich2_1_9/visit/current/linux-x86_64/lib/site-packages/visit', '/opt/apps/intel13/mvapich2_1_9/paraview/4.1.0/python2.7/lib/python2.7/site-packages', '/opt/apps/intel13/mvapich2_1_9/paraview/4.1.0/python2.7/lib/python2.7', '/opt/apps/intel13/mvapich2_1_9/paraview/4.1.0/lib/paraview-4.1/site-packages', '/scratch/01336/carson/logs/glurayOSPRay', '/opt/apps/python/epd/7.3.2/modules/lib/python', '/opt/apps/python/epd/7.3.2/lib', '/opt/apps/python/epd/7.3.2/lib/python27.zip', '/opt/apps/python/epd/7.3.2/lib/python2.7', '/opt/apps/python/epd/7.3.2/lib/python2.7/plat-linux2', '/opt/apps/python/epd/7.3.2/lib/python2.7/lib-tk', '/opt/apps/python/epd/7.3.2/lib/python2.7/lib-old', '/opt/apps/python/epd/7.3.2/lib/python2.7/lib-dynload', '/opt/apps/python/epd/7.3.2/lib/python2.7/site-packages', '/opt/apps/python/epd/7.3.2/lib/python2.7/site-packages/PIL']
try: paraview.simple
except: from paraview.simple import *
#import paraview.benchmark
sys.path.append("/work/01336/carson/intelTACC/svb/pv_scripts")
import benchmark
from optparse import OptionParser
#import log_parser
import time
import os
import math
#try:
  #import Numeric
#except:
  #import numpy
import sys
paraview.simple._DisableFirstRenderCameraReset()
#manta_plugin =       "/scratch/01336/carson/ParaView-v4.1.0/buildICC/lib/libMantaView.so"
benchmark.maximize_logs()


from optparse import (OptionParser,BadOptionError,AmbiguousOptionError)

class PassThroughOptionParser(OptionParser):
  def _process_args(self, largs, rargs, values):
    while rargs:
      try:
        OptionParser._process_args(self,largs,rargs,values)
      except (BadOptionError,AmbiguousOptionError), e:
        largs.append(e.opt_str)

parser = PassThroughOptionParser()
parser.add_option("--osp",
                  action="store_true", dest="osp", default=False,
                  help="Use OSPRay plugin, default is No")
parser.add_option("--vbo",
                  action="store_true", dest="vbo", default=False,
                  help="Use VBO plugin, default is NO")
parser.add_option("-i", "--save-images",
                  action="store", dest="save_images", type ="string", default="",
                  help="Save's images to <string> when set")
#parser.add_option("-l", "--mantathreads", action="store", dest="threads",type="int",
                  #default=16, help="set number of manta threads")
parser.add_option("--geoLevel", action="store", dest="geoLevel",type="int",
                  default=1, help="number of triangles to render")
parser.add_option("-s", "--source", action="store", dest="source",
                  default="fiu",
                  help="randomtriangles,daugton,wavelet")
parser.add_option("-w", "--windowsize", action="store", dest="windowsize",type="string",
                  default="512x512", help="windows size widthxheight")
parser.add_option("--numruns", action="store", dest="numruns",type="int",
                  default=300, help="number of runs to do")
#parser.add_option("-b", "--binaryswap", action="store_true", dest="usebswap",
                  #default=False, help="Loads the Generic View Plugin")
parser.add_option("--immediatemode", action="store_true", dest="immediatemode",
                  default=False, help="Use Immediate Mode Rendering")
#parser.add_option("--save-data",
                  #action="store", dest="write_data", type ="string", default="",
                  #help="save generated data to file")
#parser.add_option("--noContour",
                  #action="store_false", dest="use_contour", default=True,
                  #help="render with contour")

(options, args) = parser.parse_args()

#pm = servermanager.vtkProcessModule.GetProcessModule()
#pm.SetLogBufferLength(servermanager.ActiveConnection.ID, 0x1, 1000000)
#pm.SetLogBufferLength(servermanager.ActiveConnection.ID, 0x4, 1000000)
#pm.SetLogBufferLength(servermanager.ActiveConnection.ID, 0x10, 1000000)


#write_data = options.write_data
source = options.source
plugin_osp = options.osp
plugin_vbo = options.vbo
geometryLevel = options.geoLevel
fn = "/scratch1/patchett/daughton/global.vpc"
winwidth=int(options.windowsize.split("x")[0])
winheight=int(options.windowsize.split("x")[1])
windowsize = [winwidth, winheight]
print "windowsize: " + str(windowsize)
save_images = options.save_images
framecnt = 0 # framecount is used to name saved files
use_immediate = 0
immediatemode = options.immediatemode
num_runs = options.numruns


if (plugin_vbo):
    #LoadPlugin("/scratch/01336/carson/ParaView-v4.1.0/buildICC/lib/libVBOView.so", True)
    LoadPlugin("/scratch/01336/carson/intelTACC/pvPlugins/libVBOView.so", True)
    #view = paraview.simple._create_view("MantaBatchView")
    view = CreateView("VBOView")
    #view.Threads = options.threads
    view.ViewSize =  windowsize


if (plugin_osp):
    # LoadPlugin("/scratch/01336/carson/ParaView-v4.1.0-3/buildICC/lib/libOSPRayView.so", True)
    #LoadPlugin("/work/01336/carson/opt/apps/pvospray/1.0.0/lib/libOSPRayView.so", True)
    #LoadPlugin("/work/01336/carson/opt/maverick/apps/pvospray/1.0.0/lib/libOSPRayView.so", True)
    print "loading ospray plugin"
    #LoadPlugin("/work/01336/carson/opt/apps/pvospray/1.0.0/lib/libOSPRayView.so", True)
    #LoadPlugin("/work/01336/carson/opt/maverick/apps/pvospray/1.0.0/lib/libOSPRayView.so", True)
    #LoadPlugin("/work/01336/carson/ParaView/ParaView-v4.1.0/buildStampedeICCDebug/lib/libOSPRayView.so", True)
    #LoadPlugin("/work/01336/carson/ParaView/ParaView-v4.1.0/buildMaverickICCRelease/lib/libOSPRayView.so", True)
    print "loaded ospray plugin"
    #view = paraview.simple._create_view("MantaBatchView")
    view = CreateView("OSPRayView")
    #view.Threads = options.threads
    view.ViewSize =  windowsize

try:
 if immediatemode == 1:
  use_immediate = 1
  print "enabling immediate mode"
 else:
  print "disabling immediate mode"
 #v.UseImmediateMode = use_immediate
 obj = servermanager.misc.GlobalMapperProperties()
 obj.GlobalImmediateModeRendering = use_immediate
 print "immmediate mode set correctly"
except:
 print "setting immediate mode failed, using default"
 #v.UseImmediateMode = 0

sys.path.append("pv_scripts")
sys.path.append("/work/01336/carson/intelTACC/pv_scripts")
# sys.path.append("/work/01336/carson/git/svb/pv_scripts")
#import fiu
# import importlib
def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)
try:
 # sourceLib = importlib.import_module(source)
 svbSetup = import_from(source, "svbSetup")
 svbRender = import_from(source, "svbRender")
 svbGetStagesSize = import_from(source, "svbGetStagesSize")
except:
 print "ERROR: could not load source module"
 if source != "sphere":
   exit(1)
 def svbSetup(geo, stage):
  ResetCamera()
 def svbRender():
   Render() 
 def svbGetStagesSize():
  return 1;

r = GetRenderView()
try:
 r.OrientationAxesVisibility = 0
 r.CenterAxesVisibility = 0
except:
 pass
RenderView1 = GetRenderView()
RenderView1.CameraViewUp = [0.1962873715201739, 0.9002484677398408, -0.3886180182567067]
RenderView1.CameraFocalPoint = [189.50000000000014, 189.5000000000001, 413.49999999999994]
RenderView1.CameraClippingRange = [1074.1386677858422, 2867.7684315317306]
RenderView1.CameraPosition = [2008.3637843775757, -314.68686783528074, 164.22317987438336]
RenderView1.OrientationAxesVisibility = 0
RenderView1.Background = [1,1,1]

#sp = Sphere()
#sp.PhiResolution = 100;
#sp.ThetaResolution = 100;
#Show()
#Render()
view = GetActiveView()
view.ViewSize=windowsize


numStages = svbGetStagesSize()
for stage in range(numStages):
  print "#"
  print "Stage " + str(stage) + str("...")
  print "#"
  start_time=time.time()
  svbResults = svbSetup(geometryLevel, stage)
  azimuth = 90
  dolly = 2.0
  try:
    azimuth = svbResults['azimuth']
    dolly = svbResults['dolly']
  except:
    pass

  print "#"
  print "Warmup..."
  print "#"
  for i in range(0,num_runs/10+1):
    st = time.time()
    print "rendering warmup frame"
    svbRender()
    if (i == 0):
      print "time to first frame: " + str(time.time()-start_time)
    et = time.time()
    tt = (et-st)
    print "warmup frame Render: " + str(tt)

  print "#"
  print "Running..."
  print "#"
  times = []
  still_out_times = []
  rotate_out_times = []
  zoom_times = []
  rotate_in_times = []
  still_in_times = []

  def parseTimings(timings):
    sum = 0.0
    for i in range(0,len(timings)):
      sum += float(timings[i])
    avg = 0.0
    if (len(timings) > 0):
      avg = sum/float(len(timings))
    dev = 0.0
    for i in range(0, len(timings) ):
      val = float(timings[i])-avg
      dev += val*val
    if (len(timings) > 0):
      dev = dev/float(len(timings))
    dev = math.sqrt(dev)
    total = 0.0
    if (len(timings) > 0):
      total = timings[len(timings)-1]-timings[0]
    numFrames = len(timings)
    return {'avg':avg, 'dev':dev, 'total':sum, 'numFrames':numFrames}

  def printTimings(timings, name):
    restuls = parseTimings(timings)
    if (results['numFrames'] > 0):
      print str(name) + " results avg: " + str(results['avg']) + " dev: " + str(results['dev'])


  cam = GetActiveCamera()
  start_time = time.time()
  for i in range(0,num_runs):
    frac = float(i)/float(num_runs)
    if (frac < .2):
      pass
    elif (frac < .4):
      cam.Azimuth(-azimuth/(float(num_runs)/5.0))
    elif (frac < .6):
      cam.Dolly(1.0 + dolly/(float(num_runs)/5.0))
    elif (frac < .8):
      cam.Azimuth(azimuth/(float(num_runs)/5.0))
    else:
      pass

  #  cam.Azimuth(3)
  #  cam.Dolly(5)
    st = time.time()
    svbRender()
    et = time.time()
    tt = (et-st)
    times.append(tt)
    if (frac < .2):
      still_out_times.append(tt)
    elif (frac < .4):
      rotate_out_times.append(tt)
    elif (frac < .6):
      zoom_times.append(tt)
    elif (frac < .8):
      rotate_in_times.append(tt)
    else:
      still_in_times.append(tt)


    #print "frame Render: " + str(tt)
    if save_images != "":
       file = save_images + '%d.jpg' % framecnt
       WriteImage(file)
       print "saved image: " + file
       framecnt += 1
  end_time = time.time()
  print "#"
  print "parsing..."
  print "#"
  #log_parser.print_logs()

  #benchmark.run()
  pv_logs = benchmark.parse_logs(True)
  print pv_logs
  benchmark.print_logs()

  fps = float(num_runs)/(end_time-start_time);
  results = parseTimings(times)
  if (results['numFrames'] > 0):
    print "overall time avg fps: " + str(1.0/results['avg']) + " avg: " + str(results['avg']) + " dev: " + str(results['dev'])

  #results = parseTimings(still_out_times)

  #if (results['numFrames'] > 0):
    #print "still zoomed out results avg fps: " + str(1.0/results['avg']) + " avg: " + str(results['avg']) + " dev: " + str(results['dev'])
  #results = parseTimings(rotate_out_times)
  #if (results['numFrames'] > 0):
    #print "rotate zoomed out results avg fps: " + str(1.0/results['avg']) + " avg: " + str(results['avg']) + " dev: " + str(results['dev'])
  #results = parseTimings(zoom_times)
  #if (results['numFrames'] > 0):
    #print "zoom results avg fps: " + str(1.0/results['avg']) + " avg: " + str(results['avg']) + " dev: " + str(results['dev'])
  #results = parseTimings(rotate_in_times)
  #if (results['numFrames'] > 0):
    #print "rotate zoomed in results avg fps: " + str(1.0/results['avg']) + " avg: " + str(results['avg']) + " dev: " + str(results['dev'])
  #results = parseTimings(still_in_times)
  #if (results['numFrames'] > 0):
    #print "still zoomed in results avg fps: " + str(1.0/results['avg']) + " avg: " + str(results['avg']) + " dev: " + str(results['dev'])


  times = []
  for i in range (0, len(pv_logs)):
    if len(pv_logs[i]):
      if pv_logs[i][0].get('Still') != None:
        stime = pv_logs[i][0]['Still']
        times.append(stime)
  times = times[num_runs/10+1:]

  printTimings(times[:int(num_runs*.2)], "overall frame time")

  times = []
  for i in range (0, len(pv_logs)):
    if len(pv_logs[i]):
      if pv_logs[i][0].get('OpenGL Dev'):
        rtime = pv_logs[i][0]['OpenGL Dev']
        times.append(rtime)
  times = times[num_runs/10+1:]

  printTimings(times[:int(num_runs*.2)], "overall render time")
  printTimings(times[int(num_runs):int(num_runs*.2)], "still zoomed out")
  printTimings(times[int(num_runs*.2):int(num_runs*.4)], "rotate zoomed out")
  printTimings(times[int(num_runs*.4):int(num_runs*.6)], "zooming")
  printTimings(times[int(num_runs*.6):int(num_runs*.8)], "rotate zoomed in")
  printTimings(times[int(num_runs*.8):], "still zoomed in")

  readerTime = -1.0
  filterTime = -1.0
  if pv_logs[0][0].get('reader') != None:
    readerTime = pv_logs[0][0]['reader']
  print "reader time " + str(readerTime)
  if pv_logs[0][0].get('filter') != None:
    filterTime = pv_logs[0][0]['filter']
  print "filter time " + str(filterTime)

view=GetActiveView()
# exit()

