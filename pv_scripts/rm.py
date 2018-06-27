#/* =======================================================================================
#   This file is released as part of SVBench: Scientific Visualization Benchmarking Suite
#	 https://github.com/TACC/vis-workloads
#
#   Copyright 2013-2015 Texas Advanced Computing Center, The University of Texas at Austin
#   All rights reserved.
#
#   Licensed under the BSD 3-Clause License, (the "License"); you may not use this file
#   except in compliance with the License.
#   A copy of the License is included with this software in the file LICENSE.
#   If your copy does not contain the License, you may obtain a copy of the License at:
#
#       http://opensource.org/licenses/BSD-3-Clause
#
#   Unless required by applicable law or agreed to in writing, software distributed under
#   the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#   KIND, either express or implied.
#   See the License for the specific language governing permissions and limitations under
#   limitations under the License.
#
#
#   SVBench: Scientific Visualization Benchmarking Suite is funded in part by an Intel Cooperation award
#   ======================================================================================= */

try: paraview.simple
except: from paraview.simple import *
import os
import time
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
  return 1;

def svbSetup(geometryLevel=1, stage=0):
  ## get active view
  #oSPRayRendered3DView1 = GetActiveView()
  ## uncomment following to set a specific view size
  ## oSPRayRendered3DView1.ViewSize = [845, 535]

  ## get color transfer function/color map for 'ImageFile'
  #imageFileLUT = GetColorTransferFunction('ImageFile')

  ## show data in view
  #rm_0202nhdrDisplay = Show(rm_0202nhdr, oSPRayRendered3DView1)
  ## trace defaults for the display properties.
  #rm_0202nhdrDisplay.AmbientColor = [0.3803921568627451, 0.3803921568627451, 0.3803921568627451]
  #rm_0202nhdrDisplay.ColorArrayName = ['POINTS', 'ImageFile']
  #rm_0202nhdrDisplay.LookupTable = imageFileLUT
  #rm_0202nhdrDisplay.ScalarOpacityUnitDistance = -4.241863336756942
  #rm_0202nhdrDisplay.CubeAxesColor = [0.3803921568627451, 0.3803921568627451, 0.3803921568627451]

  ## reset view to fit data
  #oSPRayRendered3DView1.ResetCamera()

  ## show color bar/color legend
  #rm_0202nhdrDisplay.SetScalarBarVisibility(oSPRayRendered3DView1, True)

  ## get opacity transfer function/opacity map for 'ImageFile'
  #imageFilePWF = GetOpacityTransferFunction('ImageFile')

  ##### saving camera placements for all active views

  ## current camera placement for oSPRayRendered3DView1
  #oSPRayRendered3DView1.CameraPosition = [5257.914254142258, 1587.2581359505887, 6133.624390377831]
  #oSPRayRendered3DView1.CameraFocalPoint = [1023.5000000000001, 1023.5000000000001, 959.5]
  #oSPRayRendered3DView1.CameraViewUp = [-0.020754560419573215, 0.995589552531291, -0.09149148109159688]
  #oSPRayRendered3DView1.CameraParallelScale = 1736.5899775134026
  #return

  global Contour1
  global reader

  numCells = 0
  numPolys = 0
  numPoints = 0

  useNormals = False

  returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':False, 'tt_reader':0, 'tt_filter':0};
  valRanges = [27,150]
  valRange = valRanges[1]-valRanges[0]
  val = (float(stage+.5)/float(svbGetStagesSize()))*valRange+valRanges[0]

  if (geometryLevel == 0):
    isovals = [val]
  else:
    val = 27
    isovals = drange(val,val+50.0,51.0/float(geometryLevel))
    isovals = isovals[:geometryLevel]
  print "isovals: " + str(isovals)

  #print "h"
  #print(rm_data_dir+"/rm_0273.nhdr")
  filename = ""
  if (geometryLevel == 0):
    filename = rm_data_dir+ '/ppmt273_256_256_256.nrrd'
    st_reader = time.time()
    reader = NrrdReader( FileName=filename)
    reader.UpdatePipeline()
    et_reader = time.time()
    tt_reader = time.time()
  else:
    filename = rm_data_dir+ '/rm_0273.xmf'
    #filename = rm_data_dir+'/rm_0202.nhdr'
    print "reading file: " + filename
    st_reader = time.time()
    reader = XDMFReader(FileNames=[filename])
    #filename = '/work/01336/carson/data/ppmt273_256_256_256.nrrd'
    #reader = NrrdReader(FileName=filename)
    #reader = NrrdReader( FileName='/work/01336/carson/intelTACC/data/rm/unblock/rm_0202.nrrd' )
    reader.UpdatePipeline()
    et_reader = time.time()
    tt_reader = (et_reader-st_reader)
    print "read file"

  # reader = NrrdReader( FileName=rm_data_dir+ '/rm_0273.nhdr' )
  # reader = XDMFReader(FileNames=[rm_data_dir + '/rm_0273.xmf'])
  # reader = NrrdReader( FileName=rm_data_dir+ '/ppmt273_256_256_256.nrrd' )
  # reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')

  st_filter = time.time()
  Contour1 = Contour(Input=reader)

  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'ImageFile']
  Contour1.Isosurfaces = isovals
  # Contour1.Isosurfaces = [125.0]
  Contour1.PointMergeMethod = 'Uniform Binning'
  Contour1.ComputeNormals = int(useNormals)
  Contour1.ComputeScalars = 0

  #just checking if Update will work here
  Contour1.UpdatePipeline()
  et_filter = time.time()
  tt_filter = (et_filter-st_filter)
  print "contoured"
  lut = imageFileLUT = GetColorTransferFunction('ImageFile')
  lut.RescaleTransferFunction(0,250)
  rep = Show()
  rep.LookupTable = lut
  imageFilePWF = GetOpacityTransferFunction('ImageFile')
  rep.ColorArrayName = ['POINTS','ImageFile']
  rep.SetRepresentationType('Surface')
  rep.DiffuseColor = [1.0, 0.71372549019607845, 0.21568627450980393]

  renderView1 = GetActiveView()
  renderView1.LODThreshold = 1000000000000
  #LODResolution=0 implies lowest level1 should max level of LOD
  UseOutlineForLODRendering = 0 #when set to true ovverrides LOD REsolution

  #displayProperties = GetDisplayProperties(Contour1, renderView1)
  #displayProperties.RescaleTransferFunctionToDataRange(True)

  renderView1.CameraPosition = [582.5678621725423, 464.5664327088711, 765.7235282760473]
  renderView1.CameraFocalPoint = [127.50000000000001, 127.50000000000006, 127.50000000000001]
  renderView1.CameraViewUp = [-0.08930979131282728, 0.9056097848422845, -0.4146018316090396]
  renderView1.CameraParallelScale = 220.83647796503186


  if useNormals:
    contour1Display = GetDisplayProperties(Contour1, view=renderView1)

    # set scalar coloring
    ColorBy(contour1Display, ('POINTS', 'Normals'))

    # rescale color and/or opacity maps used to include current data range
    contour1Display.RescaleTransferFunctionToDataRange(True)

    # get color transfer function/color map for 'Normals'
    normalsLUT = GetColorTransferFunction('Normals')
    normalsLUT.ScalarRangeInitialized = 1

    # get opacity transfer function/opacity map for 'Normals'
    normalsPWF = GetOpacityTransferFunction('Normals')

    #change array component used for coloring
    normalsLUT.VectorMode = 'Component'

    # Properties modified on normalsPWF
    #normalsPWF.Points = [-0.9999991059303284, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
    normalsPWF.Points = [         -0.99999886751174905,         0,         0.5,         0,         -0.99999886751174905,         1,         0.5,         0,         -0.61212044518361797,         1,         0.5,         0,         0.27878784282692798,         1,         0.5,         0,         0.99999934434890703,         1,         0.5,         0]
    #change array component used for coloring
    normalsLUT.VectorComponent = 0

    #normalsLUT.RGBPoints = [-0.9999991059303284, 0.058823529411764705, 0.0784313725490196, 0.2, -0.6878973245620728, 0.28627450980392155, 0.3803921568627451, 0.8235294117647058, 4.4702373369620574e-07, 0.865003, 0.865003, 0.865003, 1.0, 0.5568627450980392, 0.07450980392156863, 0.0392156862745098]
    #normalsLUT.RGBPoints = [-0.9999991059303284, 0.058823529411764705, 0.0784313725490196, 0.2, -0.6878973245620728, 0.28627450980392155, 0.3803921568627451, 0.8235294117647058, 4.4702373369620574e-07, 0.865003, 0.865003, 0.865003, 1.0, 0.5568627450980392, 0.07450980392156863, 0.0392156862745098]
    normalsLUT.RGBPoints = [         -0.99999886751174905,         0.105882352941176,         0.14117647058823499,         0.35294117647058798,         -0.36969637870788602,         0.28235294117647097,         0.37254901960784298,         0.81568627450980402,         0.060606263577938101,         0.56078431372548998,         0.69411764705882395,         0.99607843137254903,         0.35757571458816501,         0.86666666666666703,         0.86666666666666703,         0.86666666666666703,         0.99999934434890703,         0.53725490196078396,         0.14509803921568601,         0.090196078431372506]
    #### saving camera placements for all active views

  # current camera placement for oSPRayRendered3DView1
  renderView1.CameraPosition = [-343.804513858627, 484.2377950087568, -331.00118857283326]
  renderView1.CameraFocalPoint = [127.50000000000018, 127.49999999999984, 112.4193172454835]
  renderView1.CameraViewUp = [0.4505229216329572, -0.39806930949541297, -0.799105701344415]
  renderView1.CameraParallelScale = 191.24810607783527


  renderView1.Background = [1,1,1]
  ResetCamera()
  returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':False, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))
  print "rm setup finished"
  returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':False, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
  return returnVals

def svbRender():
  Render()
