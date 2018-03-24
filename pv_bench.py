try: paraview.simple
except: from paraview.simple import *
from optparse import OptionParser
import time
import os
import math
import sys
import resource
paraview.simple._DisableFirstRenderCameraReset()


datasets=["fiu","wrf","geo","mol","whipple","enzo","rm","turbulence"]

path_vars = dict()
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'paths.sh')


#read in paths from the environment variables bash script generate by cmake
with open(filename) as f:
    next(f)
    for line in f:
        eq_index = line.find('=')
        var_name = line[:eq_index].strip()
        paths = line[eq_index + 1:].strip()
        path_vars[var_name] = paths

pv_script_path = "%s/pv_scripts" % path_vars["SVB_DIR"]
print "pv_scscript_path:%s" % pv_script_path
sys.path.append("%s/pv_scripts" % path_vars["SVB_DIR"])

import benchmark
benchmark.maximize_logs()

def PrintMemoryUsage():
   result = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

   print "Memory: " + str(float(result)/float(1024*1024)) + "GB"
   print "Page size: " + str(resource.getpagesize())

def WarmupRender():
    print "#"
    print "Warmup..."
    print "#"
    for i in range(0,3):
      if (i == 0):
        print "time to first frame: " + str(time.time()-start_time)
      warmup_st = time.time()
      print "rendering warmup frame"
      svbRender()
      warmup_et = time.time()
      warmup_tt = (warmup_et-warmup_st)
      print "warmup frame Render: " + str(warmup_tt)

#parse the command line arguments to pv_bench.py
from optparse import (OptionParser,BadOptionError,AmbiguousOptionError)

class PassThroughOptionParser(OptionParser):
  def _process_args(self, largs, rargs, values):
    while rargs:
      try:
        OptionParser._process_args(self,largs,rargs,values)
      except (BadOptionError,AmbiguousOptionError), e:
        largs.append(e.opt_str)

parser = PassThroughOptionParser()
parser.add_option("--gpu",
                  action="store_true", dest="gpu", default=False,
                  help="Use OSPRay plugin, default is No")
parser.add_option("--gpu2",
                  action="store_true", dest="gpu2", default=False,
                  help="Use OSPRay plugin, default is No")
parser.add_option("--osp",
                  action="store_true", dest="osp", default=False,
                  help="Use OSPRay plugin, default is No")
parser.add_option("--ao",
                  action="store_true", dest="use_ao", default=False,
                  help="Use OSPRay plugin, default is No")
parser.add_option("--vbo",
                  action="store_true", dest="vbo", default=False,
                  help="Use VBO plugin, default is NO")
parser.add_option("--swr",
                  action="store_true", dest="swr", default=False,
                                    help="Use SWR plugin, default is NO")
parser.add_option("--gluray",
                  action="store_true", dest="gluray", default=False,
                                                      help="Use GLURAY plugin, default is NO")
parser.add_option("-i", "--save-images",
                  action="store", dest="save_images", type ="string", default="",
                  help="Save's images to <string> when set")
parser.add_option("--geoLevel", action="store", dest="geoLevel",type="int",
                  default=1, help="number of triangles to render")
parser.add_option("-s", "--source", action="store", dest="source",
                  default="fiu",
                  help="randomtriangles,daugton,wavelet")
parser.add_option("-w", "--windowsize", action="store", dest="windowsize",type="string",
                  default="512x512", help="windows size widthxheight")
parser.add_option("--numruns", action="store", dest="numruns",type="int",
                  default=300, help="number of runs to do")
parser.add_option("--immediatemode", action="store_true", dest="immediatemode",
                  default=False, help="Use Immediate Mode Rendering")
(options, args) = parser.parse_args()

source = options.source
geo = options.geoLevel
plugin_osp = options.osp
use_ao = options.use_ao
plugin_vbo = options.vbo
plugin_swr = options.swr
plugin_gluray = options.gluray
plugin_gpu = options.gpu
plugin_gpu2 = options.gpu2

geometryLevel = options.geoLevel
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

    view = CreateView("VBOView")

    view.ViewSize =  windowsize
    renderer="vbo"

if(plugin_swr):
    renderer="swr"
if(plugin_gluray):
    renderer="gluray"
if(plugin_gpu):
    renderer="gpu"
if(plugin_gpu2):
    renderer="gpu2"


#Paraview is automatically loading ospray currently, the script will crash if you try to LoadPlugin when it is already loaded, this is why the LoadPlugin is commented out currently, we need to add a test to see if it is already loaded
#adb: do this using dirs() and checking if any of the entried == pvOSPRAY
if (plugin_osp):

    try:
      LoadPlugin(str(path_vars["ParaViewGL2_DIR"]) + "/lib/libpvOSPRay.so", True)
    except:
      print "Error could not load plugin!"
      exit(0)

    print "loading ospray plugin"

    print "loaded ospray plugin"

    view = CreateView('OSPRayView')

    view.ViewSize =  windowsize
    view.EnableProgressiveRefinement = 0
    if use_ao:
      view.EnableAO = 1
      renderer="ospao"
    else:
      view.EnableAO = 0
      renderer="osp"

try:
    if immediatemode == 1:
        use_immediate = 1
        print "enabling immediate mode"
    else:
        print "disabling immediate mode"
    obj = servermanager.misc.GlobalMapperProperties()
    obj.GlobalImmediateModeRendering = use_immediate
    print "immmediate mode set correctly"
except:
    print "setting immediate mode failed, using default"


def import_from(module, name):
    print("inside import_from")
    print("module: " + module)
    print("name: " + name)
    module = __import__(module, fromlist=[name])
    return getattr(module, name)


try:
    print "trying to import from source"
    svbSetup = import_from(source, "svbSetup")
    print "finished svbSetup"
    svbRender = import_from(source, "svbRender")
    print "finished svbRender"
    svbGetStagesSize = import_from(source, "svbGetStagesSize")
    print "finished svbGetStageSize"
except:
    print "ERROR: could not load source module"
    if source != "sphere":
        print("exiting...")
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
RenderView1.CameraPosition = [2008.3637843775757, -314.68686783528074, 164.22317987438336]
RenderView1.OrientationAxesVisibility = 0
RenderView1.Background = [1,1,1]

view = GetActiveView()
view.ViewSize=windowsize
view.LODThreshold = 9999999999999
view.RemoteRenderThreshold = 9999999

numStages = svbGetStagesSize()

print "Total Stages: " + str(numStages)

for stage in range(numStages):
    print "#"
    print "Stage " + str(stage) + str("...")
    print "#"
    start_time=time.time()
    svbResults = svbSetup(geometryLevel, stage)
    PrintMemoryUsage()
    print("done printing memory usage")
    azimuth = 90
    dolly = 2.0
    azimuth=0
    dolly=0
    animateCamera = True
    tt_reader=-1
    tt_filter=-1
    print("about to go into try/except block")
    try:
        print("inside try/except block")
        azimuth = svbResults['azimuth']
        print("azimuth success")
        dolly = svbResults['dolly']
        print("dolly success")
        animateCamera = svbResults['animateCamera']
        print("animateCamera success")
        tt_reader = svbResults['tt_reader']
        print("tt_reader success")
        tt_filter = svbResults['tt_filter']
        print("tt_filter success")
    except:
        print "Error reading parameters from svbSetup"
        pass

    WarmupRender()
    print "#"
    print "Running..."
    print "#"
    times = []
    still_out_times = []
    rotate_out_times = []
    zoom_times = []
    rotate_in_times = []
    still_in_times = []

    #finds the average and std deviation when there are multiple runs
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

    #prints the average and std deviation when there are multiple runs
    def printTimings(timings, name):
        results = parseTimings(timings)
        if (results['numFrames'] > 0):
            print str(name) + " results avg: " + str(results['avg']) + " dev: " + str(results['dev'])


    cam = GetActiveCamera()
    for i in range(0,num_runs):
        #move the camera for static datasets
        #for dynamic and time series data I am setting frac to 0.1 so everything will be recorded in the still_out_times
        if animateCamera == False:
            frac = 0.1
        elif animateCamera == True:
            frac = float(i)/float(num_runs)
            print "frac: " + str(frac)
            if (frac < .2):
                pass
            elif (frac < .4):
                cam.Azimuth(-azimuth/(float(num_runs)/5.0))
                print "cam.Azimuth: " + str(-azimuth/(float(num_runs)/5.0))
                print "cam.Dolly: " + str(dolly)
            elif (frac < .6):
                cam.Dolly(1.0 + dolly/(float(num_runs)/5.0))
                print "cam.Azimuth: " + str(azimuth)
                print "cam.Dolly: " + str(1 + dolly/(float(num_runs)/5.0))
            elif (frac < .8):
                cam.Azimuth(azimuth/(float(num_runs)/5.0))
                print "cam.Azimuth: " + str(azimuth/(float(num_runs)/5.0))
                print "cam.Dolly: " + str(dolly)
            else:
                pass

        #start time
        st_render = time.time()
        svbRender()
        #end time
        et_render = time.time()
        tt_render = (et_render-st_render)
        times.append(tt_render)
        #if the camera us disabled frac will be 0.1 and all times will be added to still_out_times
        if (frac < .2):
            still_out_times.append(tt_render)
        elif (frac < .4):
            rotate_out_times.append(tt_render)
        elif (frac < .6):
            zoom_times.append(tt_render)
        elif (frac < .8):
            rotate_in_times.append(tt_render)
        else:
            still_in_times.append(tt_render)


        if save_images != "":
            file = save_images + 'd%s_r%s_t%d_%05d.jpg' % (source, renderer, geo, framecnt)

            SaveScreenshot(file)
            print "saved image: " + file
            framecnt += 1

    end_time = time.time()
    print "#"
    print "parsing..."
    print "#"

    pv_logs = benchmark.parse_logs(True)
    print "paraview benchmark log:"
    print pv_logs

    fps = float( num_runs ) / ( end_time - start_time );

    print "fps: " + str( fps )
    print "times: "
    print times


    printTimings(times,            "overall render time" )
    printTimings(still_out_times,  "still zoomed out"    )
    printTimings(rotate_out_times, "rotate zoomed out"   )
    printTimings(zoom_times,       "zooming"             )
    printTimings(still_in_times,   "still zoomed in"     )
    printTimings(rotate_in_times,  "rotate zoomed in"    )



    readerTime = -1.0
    filterTime = -1.0
    if pv_logs[0][0].get('reader') != None:
        readerTime = pv_logs[0][0]['reader']
    print "pv_reader time " + str(readerTime)
    if pv_logs[0][0].get('filter') != None:
        filterTime = pv_logs[0][0]['filter']
    print "pv_filter time " + str(filterTime)
    benchmark.clear_logs()
    benchmark.clear_all()
    print "reader time " + str(tt_reader)
    print "filter time " + str(tt_filter)

view=GetActiveView()
