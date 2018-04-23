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
    print f
    next(f)
    for line in f:
        print line
        eq_index = line.find('=')
        var_name = line[:eq_index].strip()
        paths = line[eq_index + 1:].strip()
        path_vars[var_name] = paths

rm_data_dir =  path_vars["RMDATA_DIR"]
print "rm_data_dir:%s" %  rm_data_dir

def svbGetStagesSize():
  return 1;

def svbSetup(geometryLevel=1, stage=0):
  global Contour1
  global reader

  numCells = 0
  numPolys = 0
  numPoints = 0
  st_reader = time.time()
  print("rm_data_dir: "+rm_data_dir)

  if geometryLevel > 6:
    st_reader = time.time()
    reader = NrrdReader( FileName=rm_data_dir+"/rm_0273.nhdr" )
    et_reader = time.time()
    tt_reader = (et_reader - st_reader)

    st_filter = time.time()
    Contour1 = Contour(Input=reader)
    Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'ImageFile']
    Contour1.Isosurfaces = [27.0]
    Contour1.ComputeNormals = 1
    Contour1.Update()
    et_filter = time.time()
    tt_filter = (et_filter-st_filter)
    DataRepresentation2 = Show()
    #DataRepresentation2.ScaleFactor = 25.5
    DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'

  if geometryLevel < 0:
    #ppmt273_256_256_256_nrrd = NrrdReader( FileName='/scratch/01336/carson/data/RM/ppmt273_256_256_256.nrrd' )
    #reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')
    st_reader = time.time()
    reader = NrrdReader( FileName='/work/01336/carson/intelTACC/data/rm/unblock/rm_0202.nhdr')
    #reader = NrrdReader( FileName='/work/01336/carson/intelTACC/data/fiu/rho_380x380x828_frame0010_subs00.nhdr' )
    et_reader = time.time()
    tt_reader = (et_reader - st_reader)
    st_filter = time.time()
    Contour1 = Contour(Input=reader)
    Contour1 = Contour( PointMergeMethod="Uniform Binning" )
    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'ImageFile']
    Contour1.Isosurfaces = [27.0]
    Contour1.ComputeNormals = 1
    Contour1.Update()
    et_filter = time.time()
    tt_filter = (et_filter-st_filter)

    DataRepresentation2 = Show()
    #DataRepresentation2.ScaleFactor = 25.5
    DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'

  else:
    #ppmt273_nrrd = NrrdReader( FileName='/scratch/01336/carson/intelTACC/rm/ppmt273.nrrd' )
    def computeFileName(x):
      return {
      0:"rm_yz_128.xmf",
      1:"rm_yz_256.xmf",
      2:"rm_yz_512.xmf",
      3:"rm_yz_1024.xmf",
      4:"rm_yz_1280.xmf",
      5:"rm_yz_1792.xmf",
      6:"rm_0273.xmf",
      }.get(x,6)
    fileName = computeFileName(geometryLevel)
    print(fileName)
    # name = '/scratch/01336/carson/intelTACC/rm/rm.xmf'
    st_reader = time.time()
    rm_xmf = XDMFReader( FileNames=[rm_data_dir+"-unblocked/"+fileName] )
    et_reader = time.time()
    tt_reader = (et_reader - st_reader)
    # rm_xmf.Sets = []
    # rm_xmf.Grids = ['Grid_5']
    # rm_xmf.PointArrays = ['ImageFile']
    # Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    #Contour1.PointMergeMethod = "Uniform Binning"
    #Contour1.ContourBy = ['POINTS', 'RTData']
    #Contour1.Isosurfaces = [27.0]
    #Contour1.ComputeNormals = 0

    #DataRepresentation2 = Show()
    #DataRepresentation2.ScaleFactor = 25.5
    #DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'

    RenderView2 = GetRenderView()

    # DataRepresentation2 = Show()
    # DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
    # #DataRepresentation2.Slice = 959
    # DataRepresentation2.SelectionPointFieldDataArrayName = 'ImageFile'
    # #DataRepresentation2.ScalarOpacityUnitDistance = -4.241863336756942
    # DataRepresentation2.Representation = 'Outline'
    # DataRepresentation2.ScaleFactor = 204.70000000000002

    RenderView2.CameraClippingRange = [4733.166751461594, 9213.860962357088]

    st_filter = time.time()
    Contour1 = Contour( PointMergeMethod="Uniform Binning" )

    Contour1.PointMergeMethod = "Uniform Binning"
    Contour1.ContourBy = ['POINTS', 'ImageFile']
    #Contour1.Isosurfaces = [115.0]

    Contour1.Isosurfaces = [27.0]
    if (geometryLevel == 7):
      Contour1.Isosurfaces = [27.0,33]
    if (geometryLevel == 8):
      Contour1.Isosurfaces = [27.0,33,56]
    if (geometryLevel == 9):
      Contour1.Isosurfaces = [22,27.0,33,56]
    if (geometryLevel == 10):
      Contour1.Isosurfaces = [18,22,27.0,33,56]

    Contour1.UpdatePipeline()
    et_filter = time.time()
    tt_filter = (et_filter - st_filter)

    DataRepresentation3 = Show()
    #DataRepresentation3.ScaleFactor = 204.70000000000002
    DataRepresentation3.SelectionPointFieldDataArrayName = 'Normals'
    DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]

    #RenderView1 = GetRenderView()

  #DataRepresentation1 = Show()
  #DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #DataRepresentation1.Slice = 127
  #DataRepresentation1.SelectionPointFieldDataArrayName = 'ImageFile'
  #DataRepresentation1.ScalarOpacityUnitDistance = 1.7320508075688774
  #DataRepresentation1.Representation = 'Outline'
  #DataRepresentation1.ScaleFactor = 25.5

  #RenderView1.CameraPosition = [729.0865354184773, -292.7342127551322, -307.84659539241414]
  #RenderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
  #RenderView1.CameraClippingRange = [411.40476465105576, 1411.4925876279806]
  #RenderView1.CameraParallelScale = 220.83647796503186

  #DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  #RenderView1.Background = [1.0,1.0,1.0]

  ResetCamera()
  cam = GetActiveCamera()
  cam.Roll(90)
  cam.Elevation(65)
  cam.Azimuth(-20)

  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))


  returnVals = {'azimuth':90, 'dolly':3.0, 'animateCamera':True, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
  return returnVals


def svbRender():
  Render()
