#!/usr/bin/python
from optparse import OptionParser
#import Numeric
import time
import os
import visit
import sys
#visit.Close()
#launchArguments=("-par","-np","16","-l","ibrun","-nn","2")
#visit.Launch()
#OpenComputeEngine("TACC longhorn", launchArguments)

parser = OptionParser()
parser.add_option("--manta",
                  action="store_true", dest="use_manta", default=False,
                  help="Use Manta rendering, default is Yes")
parser.add_option("--saveimages",
                  action="store", dest="save_images", type ="string", default="",
                  help="Save's images to <string> when set")
parser.add_option("--mantathreads", action="store", dest="threads",type="int",
                  default=16, help="set number of manta threads")
parser.add_option("--triangles", action="store", dest="triangles",type="int",
                  default=1, help="millions of triangles to render")
parser.add_option("--source", action="store", dest="source",
                  default="wavelet",
                  help="randomtriangles,daugton,wavelet")
parser.add_option("--numruns", action="store", dest="num_runs",type="int",
                  default=200, help="number of runs")
parser.add_option("--numsplits", action="store", dest="numsplits",type="int",
                  default=2, help="number of runs")
parser.add_option("--windowsize", action="store", dest="windowsize",type="int",
                  default=1024, help="windows size n^2")
parser.add_option("--binaryswap", action="store_true", dest="usebswap",
                  default=False, help="Loads the Generic View Plugin")
parser.add_option("--weakscale", action="store", dest="weakscale",type="int",
                  default=0, help="num nodes for weak scaling")
parser.add_option("--immediatemode", action="store_true", dest="immediatemode",
                  default=False, help="Use Immediate Mode Rendering")
print "visit run got arguments: "
print sys.argv
script = 1
engine = 10000;
try:
 script = sys.argv.index("-s")+1
except:
  pass
try:
 #engine = sys.argv.index("-launchengine")
 engine = sys.argv.index("-engineargs")
 pass
except:
 pass
print engine
print "remaining arguments: " + str(sys.argv[script:engine])
print "parsing"
(options, args) = parser.parse_args(sys.argv[script:engine])
print "done parsing"

#visit.Close()
#visit.Launch()
#pm = servermanager.vtkProcessModule.GetProcessModule()
#pm.SetLogBufferLength(servermanager.ActiveConnection.ID, 0x1, 1000000)
#pm.SetLogBufferLength(servermanager.ActiveConnection.ID, 0x4, 1000000)
#pm.SetLogBufferLength(servermanager.ActiveConnection.ID, 0x10, 1000000)

immediatemode = options.immediatemode
weakscale = options.weakscale
num_runs = options.num_runs
numsplits = options.numsplits
triangles = options.triangles   #triangles in millions
source = options.source
use_manta = options.use_manta
fn = "/scratch1/patchett/daughton/global.vpc"
windowsize = [options.windowsize, options.windowsize]
save_images = options.save_images
framecnt = 0 # framecount is used to name saved files
use_binaryswap = options.usebswap





if use_manta:
 r = GetRenderingAttributes()
 r.scalableActivationMode = r.Never
 r.displayListMode = r.Always
 SetRenderingAttributes(r)

w = WindowInformation()
print "using scalable rendering: " + str(w.usingScalableRendering)

ra = RenderingAttributes()
ra.colorTexturingFlag = 0
ra.multiresolutionMode = 0
ra.scalableActivationMode = ra.Always
if immediatemode:
  ra.displayListMode = ra.Never
else:
  ra.displayListMode = ra.Always

SetRenderingAttributes(ra)

#
#  VISIT is rendering twice for each draw call!
#
#num_runs /= 2;  

print GetLocalHostName()
if use_manta: print "using Manta rendering %d threads" % options.threads
else: print "NOT using Manta"
print "using %d million triangles" % triangles
print "using " + source
print "windowsize = " + str(windowsize)

manta_plugin =       "/home/01336/carson/ParaView_3_11_IceT/build/bin/libMantaView.so"
genericview_plugin = "/home/01336/carson/GenericViewPlugin/build/libGenericView.so"
daughtonisos = {1: [0.616],
                2: [0.622, 0.614], 
                4: [0.612, 0.616],
                8: [0.454 , 0.624],
                16:[0.416 , 0.476],
                32:[0.478 , 0.602], 
                64:[0.538 , 0.506], 
                128:[0.578 , 0.612],
                256:[0.558 , 0.602],
                512:[0.56  , 0.552] }

sixteenmillion=[35, 36, 43, 144, 145, 146, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 167, 168, 169, 170, 173]
#waveisos = { 0:[54.4],
#             1:[36,66,115,120], 
#             2:[35,57,102,111,129,153],
#             4:[34,45,50,130,149,150,153,156,159],
#             8:[159,156,153,152,150,147,144,141,138,135,131,127,86,47,40,37,36,35],
#             16:sixteenmillion,
#             32:Numeric.arange(105,137,0.5).tolist(),
#             64:Numeric.arange(105,161,0.5).tolist(),
#             128:Numeric.arange(110.5,247.5,0.5).tolist(),
#             256:Numeric.arange(57.6,181.2,0.2).tolist(),
#	     512:Numeric.arange(57.6,181.2,0.1).tolist()  }

#if (use_manta):
#    LoadPlugin(manta_plugin, True)
#    view = paraview.simple._create_view("MantaView")
#    view.Threads = options.threads

#if (use_binaryswap and not use_manta):
#    print "loading Generic View Plugin"
#    LoadPlugin(genericview_plugin, True)
#    view = paraview.simple._create_view("GenericBatchView")
#    view.ViewSize =  windowsize

def SetSRMode():
	r = GetRenderingAttributes()
	r.scalableActivationMode = r.Always
	SetRenderingAttributes(r)
#SetSRMode()



if source == "randomtriangles":
  OpenDatabase("localhost:/scratch/01336/carson/randomtriangles_16.vtp", 0)
  print "doing random triangles plot now..."
  plot = AddPlot("Pseudocolor", "mesh_quality/area", 1,1)
  print "... added."
  
  #TS = TriangleSource()  
  #TS.Triangles = triangles * 1000000
  #TS.Fuzziness = 0.0
  #dr = Show()
  #dr.ColorArrayName = ''
  #dr.DiffuseColor = [1.0, 0.71372549019607845, 0.21568627450980393]
  #ResetCamera()


elif source == "daughton":
  dat1 = ""
  #if numsplits <= 1:
  #  dat1 = "localhost:/scratch/01336/carson/data/daughton.vtp"
  if numsplits < 16:
    dat1 = "localhost:/scratch/01336/carson/data/daughton_8.visit"
  elif numsplits < 64:
    dat1 = "localhost:/scratch/01336/carson/data/daughton_32.visit"
  else:
    dat1 = "localhost:/scratch/01336/carson/data/daughton_128.visit"
    #dat1 = "localhost:/scratch/01336/carson/data/daughton__split216.visit"
  OpenDatabase(dat1, 0)
  plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)
  #for i in range (0, 8):
  #  dat1 = "localhost:/scratch/01336/carson/data/daughton__"+ str(i) + ".vtu"
  #  OpenDatabase(dat1, 0)
  #  plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)


elif source == "wavelet":
  if triangles == 128:
    #dat1 = "localhost:/scratch/01336/carson/data/wavelet_128.visit"
    #OpenDatabase(dat1, 0)
    #plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)
    for i in range (0, 8):
      dat1 = "localhost:/scratch/01336/carson/data/wavelet_128__"+ str(i) + ".vtu"
      OpenDatabase(dat1, 0)
      plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)
    #plot2 = AddPlot("Pseudocolor", "mesh_quality/area", 1,1)
    #DrawPlots()

    #dat2 = "localhost:/scratch/01336/carson/data/wavelet_128_split_1.vtu"
    #OpenDatabase(dat2, 0)
    #plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)
    #ta = TransformAttributes()
    #ta.translateX = 0
    #ta.translateY = 1
    #ta.translateZ = 0
    #SetOperatorOptions(TransformAtts, 1)
    #DrawPlots()

  elif triangles == 256:
    #dat1 = "localhost:/scratch/01336/carson/data/wavelet_256.visit"
    #OpenDatabase(dat1, 0)
    #plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)

   for i in range (0, 8):
     dat1 = "localhost:/scratch/01336/carson/data/wavelet_256__"+ str(i) + ".vtu"
     OpenDatabase(dat1, 0)
     plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)
    #plot2 = AddPlot("Pseudocolor", "mesh_quality/area", 1,1)
    #plot3 = AddPlot("Pseudocolor", "mesh_quality/area", 1,1)
    #plot4 = AddPlot("Pseudocolor", "mesh_quality/area", 1,1)
    #DrawPlots()
  elif triangles == 64:
     dat1 = "localhost:/scratch/01336/carson/data/wavelet_64.visit"
     OpenDatabase(dat1, 0)
     plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)
  elif triangles == 16:
    dat1 = ""
    if numsplits < 2:
      dat = "localhost:/scratch/01336/carson/data/wavelet_" + str(triangles) + ".vtp"
      #dat = "localhost:/scratch/01336/carson/data/wavelet_split_test/blah.visit"
      OpenDatabase(dat, 0)
      plot = AddPlot("Pseudocolor", "mesh_quality/area", 1,1)
    elif numsplits == 2:
     dat1 = "localhost:/scratch/01336/carson/data/wavelet_16_" + str(numsplits) + ".visit"
    elif numsplits < 32:
     dat1 = "localhost:/scratch/01336/carson/data/wavelet_16_16.visit"
    elif numsplits >= 32:
     dat1 = "localhost:/scratch/01336/carson/data/wavelet_16_32.visit"
    if numsplits > 1:
     OpenDatabase(dat1, 0)
     plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)
  else:
    dat = "localhost:/scratch/01336/carson/data/wavelet_" + str(triangles) + ".vtp"
    #dat = "localhost:/scratch/01336/carson/data/wavelet_split_test/blah.visit"
    OpenDatabase(dat, 0)
    plot = AddPlot("Pseudocolor", "mesh_quality/area", 1,1)
    #plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)
    #plot = AddPlot("Subset", "domains", 1,1)

  pa = PseudocolorAttributes()
  pa.legendFlag = 0
  pa.colorTableName = "gold"
  #pa.colorTableName = "rainbow"
  SetPlotOptions(pa)


  DrawPlots()
  
  View3DAtts = View3DAttributes()
#  View3DAtts.viewNormal = (0.361, -0.028, 0.932)
  View3DAtts.viewNormal = (0.426, 0.0253, 0.904)
  View3DAtts.focus = (0,0,0)
  #View3DAtts.viewUp = (0.076,0.997,0003)
  View3DAtts.viewUp = (0.0062,0.9995,-0.031)
  View3DAtts.viewAngle = 30
  View3DAtts.parallelScale = 173.205
  View3DAtts.nearPlane = -346
  View3DAtts.farPlane = 346
  View3DAtts.imagePan = (0, 0)
  View3DAtts.imageZoom = 1
  View3DAtts.perspective = 1
  View3DAtts.eyeAngle = 2
#  View3DAtts.centerOfRotationSet = 0
#  View3DAtts.centerOfRotation = (127.5, 127.5, 127.5)
#  View3DAtts.axis3DScaleFlag = 0
#  View3DAtts.axis3DScales = (1, 1, 1)
  View3DAtts.shear = (0, 0, 1)
  SetView3D(View3DAtts)



  """
  rtSource = Wavelet()
  rtSource.WholeExtent = [-100, 100, -100, 100, -100, 100]
  rtSource.XMag = 10.0
  rtSource.YMag =18.0
  rtSource.ZMag =5.0
  rtSource.Center= 0.0,0.0,0.0
  rtSource.Maximum= 255.0
  rtSource.StandardDeviation= .5
  rtSource.XFreq =60.0
  rtSource.YFreq =30.0
  rtSource.ZFreq =40.0
  c = Contour()
  c.Isosurfaces = waveisos[triangles]
  SetActiveSource(c)
  dr = Show()
  dr.ColorArrayName = ''
  dr.DiffuseColor = [1.0, 0.71372549019607845, 0.21568627450980393]
  ResetCamera()
  cam.Azimuth(25)
  """

elif source == "rm_zoomed_in" or source == "rm_zoomed_out" or source == "rm_zoomed_in6" or source == "rm_zoomed_out6":
  print "rm"
  if weakscale > 0:

    file = "localhost:/scratch/01336/carson/data/ppmt273_crop000.vti"
    #if weakscale == 2 or weakscale == 8 or weakscale == 32 or weakscale == 128:
    # subset = ExtractSubset()
    # subset.VOI = [0,511,0,1023,0,1919]
    # subset.SampleRateI = 2
    # SetActiveSource(subset)

    print "opening file: " + str(file)
    OpenDatabase(file, 0)
  
    #dr2 = Show()
    #dr2.Representation = 'Outline'

    #Contour1 = Contour( PointMergeMethod="Uniform Binning" )
    #Contour1.PointMergeMethod = "Uniform Binning"
    #Contour1.ContourBy = ['POINTS', 'ImageFile']
    cisos = range(0, 256,2)
    #Contour1.Isosurfaces = [27]
    #Contour1.ComputeNormals = 0
    #SetActiveSource(Contour1)
    #dr3 = Show()

    isovalues = [27]

    if weakscale == 2:
      isovalues = [27,78]
      print "isosurfaces: " + str(isovalues)
    if weakscale == 4:
      isovalues = [27,78, 125, 128]
      print "isosurfaces: " + str(isovalues)
    if weakscale == 8:
      isovalues = [27,78,125,128,180,230, 15,90]
      print "isosurfaces: " + str(isovalues)
    if weakscale == 16:
      isovalues = cisos[0:weakscale]
      print "isosurfaces: " + str(isovalues)
    elif weakscale == 32:
      isovalues = cisos[0:256:9]
      print "isosurfaces: " + str(isovalues)
    elif weakscale == 64:
      isovalues = cisos[0:256:6]
      print "isosurfaces: " + str(isovalues)
    elif weakscale == 128:
      isovalues = cisos[0:256:4]
      print "isosurfaces: " + str(isovalues)


    isovaluesTuple = tuple(isovalues)
    #for i in range(0, len(isovalues)):
    #  isovaluesTuple += (isovalues[i])
  
    plot = AddPlot("Contour", "ImageFile", 0, 1)
    #plot = AddPlot("Contour", "ImageFile", 1,1)
    ca = ContourAttributes()
    ca.defaultPalette.GetControlPoints(0).colors = (255, 0.71372549019607845*255, 0.21568627450980393*255, 255)
    ca.defaultPalette.GetControlPoints(0).position = 0
    #ca.defaultPalette.GetControlPoints(1).colors = (1.0*255, 0.71372549019607845*255, 0.21568627450980393*255, 255)
    #ca.defaultPalette.GetControlPoints(1).position = 1
    ca.defaultPalette.smoothingFlag = 0
    ca.colorType = ca.ColorBySingleColor
    ca.singleColor = (1.0*255, 0.71372549019607845*255, 0.21568627450980393*255)
    ca.contourValue = isovaluesTuple
    ca.contourMethod = ca.Value
    ca.contourNLevels = 0
    ca.contourPercent = ()
    SetPlotOptions(ca)
    ca.colorTableName = "gold"

    print "drawing contours"
    #SetActivePlots((0,1,2,3,4,5,6,7))
    DrawPlots()






    """
    contours = []
    plotNums = []
    plotNum = 0
    plotsTuple = ()
    print "loading rm contours"
    for x in range (0,2):
     for y in range (0,2):
      for z in range (0,1):
        plotNums.append(plotNum)
        #plotsTuple += ()
        filename = '/scratch/01336/carson/ppmt273_crop'+str(x)+str(y)+str(z)+'.vti'
        #filename = '/scratch/01336/carson/ppmt273_256_256_256.vti'
        print "loading: " + str(filename)
        xoffset = x*1024;
        yoffset = y*1024;
        zoffset = z*960;
        position = [xoffset,yoffset,zoffset]
        OpenDatabase(filename, 0)
        plot = AddPlot("Contour", "ImageFile", 1, 1)
        SetActivePlots(plotNum)
        ta = TransformAttributes()
        ta.translateX = xoffset
        ta.translateY = yoffset
        ta.translateZ = zoffset
        ta.transformVectors = 0
        SetOperatorOptions(ta, plotNum)
  

        #dat = "localhost:/scratch/01336/carson/ppmt273_crop000.vti"
        #OpenDatabase(dat, 0)
        #if weakscale == 2 or weakscale == 8 or weakscale == 32 or weakscale == 128:
        # subset = ExtractSubset()
        # subset.VOI = [0,511,0,1023,0,1919]
        # subset.SampleRateI = 2
        # SetActiveSource(subset)

      
        #dr2 = Show()
        #dr2.Representation = 'Outline'

        #Contour1 = Contour( PointMergeMethod="Uniform Binning" )
        #Contour1.PointMergeMethod = "Uniform Binning"
        #Contour1.ContourBy = ['POINTS', 'ImageFile']
        cisos = range(0, 256,2)
        #Contour1.Isosurfaces = [27]
        #Contour1.ComputeNormals = 0
        #SetActiveSource(Contour1)
        #dr3 = Show()
        
        isovalues = [27]

        if weakscale == 2:
          isovalues = [27,78]
          print "isosurfaces: " + isovalues
        if weakscale == 4:
          isovalues = [27,78, 125, 128]
          print "isosurfaces: " + isovalues
        if weakscale == 8:
          isovalues = [27,78,125,128,180,230, 15,90]
          print "isosurfaces: " + isovalues
        if weakscale == 16:
          isovalues = cisos[0:weakscale]
          print "isosurfaces: " + isovalues
        elif weakscale == 32:
          isovalues = cisos[0:256:9]
          print "isosurfaces: " + isovalues
        elif weakscale == 64:
          isovalues = cisos[0:256:5]
          print "isosurfaces: " + isovalues
        elif weakscale == 128:
          isovalues = cisos[0:256:3]
          print "isosurfaces: " + isovalues

        isovaluesTuple = (27)
        #for i in range(0, len(isovalues)):
        #  isovaluesTuple += (isovalues[i])
      
        #plot = AddPlot("Contour", "ImageFile", 1,1)
        ca = ContourAttributes()
        ca.defaultPalette.GetControlPoints(0).colors = (255, 0.71372549019607845*255, 0.21568627450980393*255, 255)
        ca.defaultPalette.GetControlPoints(0).position = 0
        #ca.defaultPalette.GetControlPoints(1).colors = (1.0*255, 0.71372549019607845*255, 0.21568627450980393*255, 255)
        #ca.defaultPalette.GetControlPoints(1).position = 1
        ca.defaultPalette.smoothingFlag = 0
        ca.colorType = ca.ColorBySingleColor
        ca.singleColor = (1.0*255, 0.71372549019607845*255, 0.21568627450980393*255)
        ca.contourValue = isovaluesTuple
        ca.contourMethod = ca.Value
        ca.contourNLevels = 0
        ca.contourPercent = ()
        SetPlotOptions(ca)
        ca.colorTableName = "Default"

        plotNum += 1

    print "drawing contours"
    SetActivePlots((0,1,2,3,4,5,6,7))
    DrawPlots()
    """

  else:
    plotNums = []
    plotNum = 0
    plotsTuple = ()
    splits = 1
    if numsplits > 8:
      splits = 16
    if numsplits== 64:
      splits = 8 #yeah I messed this ones name up
    print "loading rm contour poly files"
    """
    for x in range (0,2):
     for y in range (0,2):
      for z in range (0,2):
       for s in range (0, splits):
        plotNums.append(plotNum)
        #plotsTuple += ()
        if numsplits == 64:
          filename = "/scratch/01336/carson/data/rm_zoomed_out_clipping_"+ str(64) + "__"+ str(x) + str(y) + str(z) + "_" + str(s) + ".vtu"
        else:
          filename = "/scratch/01336/carson/data/rm_zoomed_out_clipping_"+ str(splits) + "__"+ str(x) + str(y) + str(z) + "_" + str(s) + ".vtu"
        #filename = '/scratch/01336/carson/ppmt273_256_256_256.vti'
        print "loading: " + str(filename)
        xoffset = x*1024;
        yoffset = y*1024;
        zoffset = z*960;
        position = [xoffset,yoffset,zoffset]
        OpenDatabase(filename)
        #plot = AddPlot("Contour", "ImageFile", 1, 1)
        #SetActivePlots(plotNum)
        plot = AddPlot("Pseudocolor", "mesh_quality/aspect")
        AddOperator("Transform", 0)
        SetActivePlots(plotNum)
        ta = TransformAttributes()
        ta.translateX = xoffset
        ta.translateY = yoffset
        ta.translateZ = zoffset
        ta.transformVectors = 0
        ta.doTranslate = 1
        ta.doRotate = 0
        ta.doScale = 0
        #ta.transformType = ta.Similarity
        #ta.inputCoordSys = ta.Cartesian
        #ta.outputCoordSys = ta.Spherical
        SetOperatorOptions(ta, 0)
        plotNum += 1
        DrawPlots()
        #print "plots:"
        #ListPlots()
    """
    filename = "localhost:/scratch/01336/carson/data/RM/ppmt273_crop000.vti"
    OpenDatabase(filename)
    #plot = AddPlot("Contour", "ImageFile", 1, 1)
    #SetActivePlots(plotNum)
    #plot = AddPlot("Contour", "ImageFile")
    #AddOperator("Transform", 0)
    #SetActivePlots(plotNum)


    isovalues = [27]

    isovaluesTuple = tuple(isovalues)
    #for i in range(0, len(isovalues)):
    #  isovaluesTuple += (isovalues[i])
  
    plot = AddPlot("Contour", "ImageFile", 0, 1)
    #plot = AddPlot("Contour", "ImageFile", 1,1)
    ca = ContourAttributes()
    ca.defaultPalette.GetControlPoints(0).colors = (255, 0.71372549019607845*255, 0.21568627450980393*255, 255)
    ca.defaultPalette.GetControlPoints(0).position = 0
    #ca.defaultPalette.GetControlPoints(1).colors = (1.0*255, 0.71372549019607845*255, 0.21568627450980393*255, 255)
    #ca.defaultPalette.GetControlPoints(1).position = 1
    ca.defaultPalette.smoothingFlag = 0
    ca.colorType = ca.ColorBySingleColor
    ca.singleColor = (1.0*255, 0.71372549019607845*255, 0.21568627450980393*255)
    ca.contourValue = isovaluesTuple
    ca.contourMethod = ca.Value
    ca.contourNLevels = 0
    ca.contourPercent = ()
    SetPlotOptions(ca)
    ca.colorTableName = "gold"
  
    #SetActivePlots((0,1))
    DrawPlots()
    print "all plots:"
    ListPlots()

    
    #if source == "rm_zoomed_in":
    #for i in range (0, 27):
    #  dat1 = "localhost:/scratch/01336/carson/data/rm_zoomed_out_64split__"+ str(i) + ".vtu"
    #  OpenDatabase(dat1, 0)
    #  plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)
    #if source == "rm_zoomed_out":
    # for i in range (0, 8):
    #   dat1 = "localhost:/scratch/01336/carson/data/rm_zoomed_out__"+ str(i) + ".vtu"
    #   OpenDatabase(dat1, 0)
    #   plot = AddPlot("Pseudocolor", "mesh_quality/aspect", 1,1)

    #if numsplits < 16:
    #  dat1 = "localhost:/scratch/01336/carson/data/rm_zoomed_out_8.visit"
    """
    if numsplits < 128:
      dat1 = "localhost:/scratch/01336/carson/data/rm_zoomed_out_64.visit"
      for i in range(0, 64):
        dat1 = "localhost:/scratch/01336/carson/data/rm_zoomed_out_64__"+ str(i)+".vtu"
        OpenDatabase(dat1, 0)
        plot = AddPlot("Pseudocolor", "mesh_quality/aspect")
    else:
      dat1 = "localhost:/scratch/01336/carson/data/rm_zoomed_out__split216.visit"
      OpenDatabase(dat1, 0)
      plot = AddPlot("Pseudocolor", "mesh_quality/aspect")
    """
    #OpenDatabase("localhost:/scratch/01336/carson/rm_256_cell.vtk", 0)
    #AddPlot("Contour", "ImageFile", 1, 1)
    pa = PseudocolorAttributes()
    pa.legendFlag = 0
    pa.colorTableName = "gold"
    #pa.colorTableName = "rainbow"
    SetPlotOptions(pa)



    """
    contours = []
    for x in range (0,2):
     for y in range (0,2):
      for z in range (0,2):
       filename = '/scratch/01336/carson/ppmt273_crop'+str(x)+str(y)+str(z)+'.nrrd'
       print filename
       reader = NrrdReader( FileName=filename)
       Contour1 = Contour( PointMergeMethod="Uniform Binning" )
       Contour1.PointMergeMethod = "Uniform Binning"
       Contour1.ContourBy = ['POINTS', 'ImageFile']
       Contour1.Isosurfaces = [27]
       if source == "rm_zoomed_in6" or source == "rm_zoomed_out6":
        Contour1.Isosurfaces = [27.0, 77.75, 125.0, 128.5, 179.25, 230.0]
       SetActiveSource(Contour1)
       contours.append(Contour1)

       DataRepresentation1 = Show()
       DataRepresentation1.DiffuseColor = [1.0, 0.71372549019607845, 0.21568627450980393]
       xoffset = x*1024;
       yoffset = y*1024;
       zoffset = z*960;
       DataRepresentation1.Position = [xoffset,yoffset,zoffset]
     
    Show()
    
    if source == "rm_zoomed_in" or source == "rm_zoomed_out":
      reader = PLYReader( FileName=['/scratch/01336/carson/rm_1iso.ply'] )
    else:
      reader = PLYReader( FileName=['/scratch/01336/carson/rm_6iso.ply'] )
    
    RenderView1 = GetRenderView()
    if source == "rm_zoomed_out" or source == "rm_zoomed_out6":
      RenderView1.CameraViewUp = [-0.67143087325620165, -0.38502986177985904, -0.63319237833078612]
      RenderView1.CameraPosition = [296.23715980857042, 552.93796554307903, -310.12633460700761]
      RenderView1.CameraClippingRange = [213.47970479866075, 1163.1477196171645]
      RenderView1.CameraFocalPoint = [68.873819856719791, -20.314523108100506, 279.54926026502233]
      ResetCamera()
    else:
      RenderView1.CameraParallelScale = 194.77849974381161
      RenderView1.CenterOfRotation = [127.5, 127.5, 122.33749961853027]

      RenderView1.CameraViewUp = [0.51904306900949748, -0.29282113324794734, -0.80302557645232553]
      RenderView1.CameraFocalPoint = [565.7958982381291, -213.44487497601432, 463.54995949645701]
      RenderView1.CameraClippingRange = [0.51171201004687994, 511.71201004687998]
      RenderView1.CameraPosition = [84.876455934952617, 156.05255473620838, 17.966942127699074]
      Show()
      ResetCamera()
      cam = GetActiveCamera()
      cam.Dolly(6.0)
      cam.Zoom(0.7)

    Show()
    #ResetCamera()
    """

elif source == "boeing":
  OpenDatabase("localhost:/scratch/01336/carson/boeing.vtp", 0)
  plot = AddPlot("Pseudocolor", "mesh_quality/area", 1,1)
  """
  for dir in ["Sub1","Sub2","Sub3","Sub4","Sub5","Sub6","Sub7","Sub8"]:
   dirstring = '/scratch/01336/carson/boeing/'+dir
   objs = os.listdir(dirstring)
   for objfile in objs:
    filename = '/scratch/01336/carson/boeing/Sub1/' + objfile
    obj = WavefrontOBJReader( FileName=filename )   
    SetActiveSource(obj)
    DataRepresentation1 = Show()
    DataRepresentation1.DiffuseColor = [1.0, 0.71372549019607845, 0.21568627450980393]
  Show()
  ResetCamera()
  cam = GetActiveCamera()
  cam.Zoom(0.8)
  cam.Dolly(2.5)
  cam.Azimuth(-55)
  cam.Elevation(45)
  objs = []
  #for dir in ["Sub1","Sub2","Sub3","Sub4","Sub5","Sub6","Sub7","Sub8","Sub9"]:
  if (1):
   dirstring = '/scratch/01336/carson/boeing/ply-incomplete'
   #objs = os.listdir(dirstring)
   objfiles = os.listdir(dirstring)
   for objfile in objfiles:
   # filename = '/scratch/01336/carson/boeing/Sub1/' + objfile
   #filename = '/scratch/01336/carson/boeing/vtp/'+dir+'.vtp'
    filename = '/scratch/01336/carson/boeing/ply-incomplete/'+objfile
   #obj = WavefrontOBJReader( FileName=filename )
   #obj = XMLPolyDataReader(FileName=filename )
    print "loading file " + filename
    obj = PLYReader(FileName=filename)
    objs.append(obj)
    SetActiveSource(obj)
    DataRepresentation1 = Show()
    DataRepresentation1.DiffuseColor = [1.0, 0.71372549019607845, 0.21568627450980393]
  #group = AppendGeometry( Input = objs )
  #SetActiveSource(group)
  Show()
  ResetCamera()
  cam = GetActiveCamera()
  cam.Zoom(0.6)
  cam.Dolly(2.0)
  cam.Azimuth(-75)
  cam.Elevation(-45)
  """

elif source == "particles":
 OpenDatabase("localhost:/scratch/01336/carson/2DArray64_tight.uda.000/index.xml", 0)
 AddPlot("Molecule", "p.temperature/0", 1, 1)
 MoleculeAtts = MoleculeAttributes()
 MoleculeAtts.drawAtomsAs = MoleculeAtts.ImposterAtoms  # NoAtoms, SphereAtoms, ImposterAtoms
 MoleculeAtts.scaleRadiusBy = MoleculeAtts.Fixed  # Fixed, Covalent, Atomic, Variable
 MoleculeAtts.drawBondsAs = MoleculeAtts.CylinderBonds  # NoBonds, LineBonds, CylinderBonds
 MoleculeAtts.colorBonds = MoleculeAtts.ColorByAtom  # ColorByAtom, SingleColor
 MoleculeAtts.bondSingleColor = (128, 128, 128, 255)
 MoleculeAtts.radiusVariable = "Default"
 MoleculeAtts.radiusScaleFactor = 1
 MoleculeAtts.radiusFixed = 0.0003
 MoleculeAtts.atomSphereQuality = MoleculeAtts.Low  # Low, Medium, High, Super
 MoleculeAtts.bondCylinderQuality = MoleculeAtts.Medium  # Low, Medium, High, Super
 MoleculeAtts.bondRadius = 0.12
 MoleculeAtts.bondLineWidth = 0
 MoleculeAtts.bondLineStyle = MoleculeAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
 MoleculeAtts.elementColorTable = "cpk_jmol"
 MoleculeAtts.residueTypeColorTable = "amino_shapely"
 MoleculeAtts.residueSequenceColorTable = "Default"
 MoleculeAtts.continuousColorTable = "Default"
 MoleculeAtts.legendFlag = 1
 MoleculeAtts.minFlag = 0
 MoleculeAtts.scalarMin = 0
 MoleculeAtts.maxFlag = 0
 MoleculeAtts.scalarMax = 1
 SetPlotOptions(MoleculeAtts)
 DrawPlots()

"""
r = GetRenderingAttributes()
r.displayListMode = r.Always #r.Always = Always fail to do what I want
#display lists not on bad visit, bad!  hardcoded it in visitopenglpolydatamapper...
SetRenderingAttributes(r)

#DrawPlots()
#view.PrintRendererType()
#print "total Polygons:" + str(dr.SMProxy.GetRepresentedDataInformation(0).GetPolygonCount())

pa = PseudocolorAttributes()
pa.legendFlag = 0
#pa.lightingFlag = 0
pa.colorTableName = "gold"
SetPlotOptions(pa)

ia = GetInteractorAttributes()
ia.boundingBoxMode = ia.Never
SetInteractorAttributes(ia)

#r = GetRenderingAttributes()
#r.scalableActivationMode = r.Always
#r.displayListMode = r.Always
SetRenderingAttributes(r)
SetRenderingAttributes(r)
#DrawPlots()
#r = GetRenderingAttributes()
#r.scalableActivationMode = r.Always
#r.displayListMode = r.Always
SetRenderingAttributes(r)
w = WindowInformation()
print "using scalable rendering: " + str(w.usingScalableRendering)
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.00389754, -0.0219155, 0.999752)
View3DAtts.focus = (127.5, 127.5, 127.5)
View3DAtts.viewUp = (-0.00518489, 0.999746, 0.0219356)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 220.836
View3DAtts.nearPlane = -441.673
View3DAtts.farPlane = 441.673
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (127.5, 127.5, 127.5)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state
ResetView()


AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 0
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
DrawPlots()
#ToggleSpinMode()

print "#"
print "warmup..."
print "#"
for i in range(0,num_runs/10+1):
  st = time.time()
  print "rendering warmup frame"
 # DrawPlots()
  RedrawWindow()
  et = time.time()
  tt = (et-st)
  print "warmup frame Render: " + str(tt)
print "#"
print "running..."
print "#"
"""
zoom = 1
def carson_default(num):
        DisableRedraw()
 	global zoom
	for i in range(0,num):
          st = time.time()
	  zoom += 0.0001
	  v = GetView3D()
	  v.imageZoom = zoom
	  SetView3D(v)
          DrawPlots()
          if save_images != "":
		 s = SaveWindowAttributes()
		 s.format = s.JPEG
		 s.fileName = str(save_images)
	         s.width, s.height = windowsize[0], windowsize[1]
		 #s.screenCapture = 0
		 #s.width, s.height = 1024,768
		 SetSaveWindowAttributes(s)
		 SaveWindow()
                 global framecnt
		 framecnt += 1
                 #p = PrinterAttributes()
	         #p.printerName = "a"
	         #SetPrinterAttributes(p)
	         #PrintWindow()
	
          et = time.time()
          tt = (et-st)
          print "frame Render: " + str(tt)


	#  cam.Azimuth(3)
	#  cam.Dolly(5)
	#ClearWindow()
	#DrawPlots()
	#DrawPlots()
	#p = PrinterAttributes()
	#p.printerName = "a"
	#SetPrinterAttributes(p)
	#PrintWindow()
	#RedrawWindow()  # look at me Im redrawWindow but I wont redraw because I suck

def tfogal_blah(num):
	DisableRedraw()
	s = GetSaveWindowAttributes()
	s.format = s.JPEG
	s.width, s.height = 450, 450
	s.quality = 100
	s.screenCapture = 0
        s.fileName = str(save_images)
	SetSaveWindowAttributes(s)
	global zoom
	for i in range(0, num):
		v = GetView3D()
		zoom += .0001
		v.imageZoom = zoom
		SetView3D(v)

		DrawPlots()
		SaveWindow()
print "warmup..."
#tfogal_blah()
carson_default(num_runs/3)
print "rendering..."
start_time = time.time()
carson_default(num_runs)
#tfogal_blah(num_runs)
#DisableRedraw()
#for i in range(0, 100):
#  DrawPlots()
end_time = time.time()
#import log_parser
#log_parser.print_logs()

#if (save_images == ""):
#  num_runs *= 2
fps = float(num_runs)/(end_time-start_time+0.000001);
print "fps: " + str(fps)
sys.exit(0)
