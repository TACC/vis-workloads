try: paraview.simple
except: from paraview.simple import *
import os
#read in paths from the environment variables bash script generate by cmake
dir = os.path.dirname( os.path.dirname(os.path.abspath(__file__)))
pathsfile = os.path.join(dir,'paths.sh')
path_vars = dict()

with open(pathsfile) as f:
    #print f
    next(f)
    for line in f:
        #print line
        eq_index = line.find('=')
        var_name = line[:eq_index].strip()
        paths = line[eq_index + 1:].strip()
        path_vars[var_name] = paths

rm_data_dir =  path_vars["RMDATA_DIR"]
print "rm_data_dir:%s" %  rm_data_dir

def drange(start,stop,step):
  vals = []
  v = start
  while v < stop:
    vals.append(v)
    v+=step
  return vals


def svbGetStagesSize():
  return 5;

def svbSetup(geometryLevel=1, stage=0):
  global Contour1
  global reader

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False};

  valRanges = [0,200]
  valRange = valRanges[1]-valRanges[0]
  val = (float(stage+.5)/float(svbGetStagesSize()))*valRange+valRanges[0]
 
  if (geometryLevel == 0):
    isovals = [val]
  else:
    isovals = drange(val,val+50.0,51.0/float(geometryLevel))
    isovals = isovals[:geometryLevel]
  print "isosweep vals: " + str(isovals)

  if (stage != 0):  
    Contour1.Isosurfaces = isovals
    return returnVals;

  #print "h"
  #print(rm_data_dir+"/rm_0273.nhdr")
  filename = ""
  if (geometryLevel == 0):
    filename = rm_data_dir+ '/ppmt273_256_256_256.nrrd' 
    reader = NrrdReader( FileName=filename)
  else:
    filename = rm_data_dir+ '/rm_0273.xmf'
    reader = XDMFReader(FileNames=[filename])
  print "reading file: " + filename
  # reader = NrrdReader( FileName=rm_data_dir+ '/rm_0273.nhdr' )
  # reader = XDMFReader(FileNames=[rm_data_dir + '/rm_0202.xmf'])
  # reader = NrrdReader( FileName=rm_data_dir+ '/ppmt273_256_256_256.nrrd' )  
  # reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')

  Contour1 = Contour(Input=reader)

  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'ImageFile']
  Contour1.Isosurfaces = isovals
  # Contour1.Isosurfaces = [125.0]
  Contour1.PointMergeMethod = 'Uniform Binning'
  Contour1.ComputeNormals = 1
  Contour1.ComputeScalars = 1

  lut = imageFileLUT = GetColorTransferFunction('ImageFile')
  lut.RescaleTransferFunction(0,250)
  rep = Show()
  rep.LookupTable = lut
  imageFilePWF = GetOpacityTransferFunction('ImageFile')
  rep.ColorArrayName = ['POINTS','ImageFile']
  rep.SetRepresentationType('Surface')
  
  renderView1 = GetActiveView()
  #displayProperties = GetDisplayProperties(Contour1, renderView1)
  #displayProperties.RescaleTransferFunctionToDataRange(True)
  renderView1.CameraPosition = [582.5678621725423, 464.5664327088711, 765.7235282760473]
  renderView1.CameraFocalPoint = [127.50000000000001, 127.50000000000006, 127.50000000000001]
  renderView1.CameraViewUp = [-0.08930979131282728, 0.9056097848422845, -0.4146018316090396]
  renderView1.CameraParallelScale = 220.83647796503186
  renderView1.Background = [1,1,1]
  ResetCamera()
  return returnVals

def svbRender():
  Render()
