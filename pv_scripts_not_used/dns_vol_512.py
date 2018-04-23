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

data_dir =  path_vars["DNSDATA_DIR"]
print "data_dir:%s" %  data_dir

def drange(start,stop,step):
  vals = []
  v = start
  while v < stop:
    vals.append(v)
    v+=step
  return vals

global Contour1
global reader

def svbGetStagesSize():
  return 1;

def svbSetup(geometryLevel=1, stage=0):
  global reader

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':True, 'tt_reader':0.0, 'tt_filter':0.0};

  numCells = 0
  numPolys = 0
  numPoints = 0

  st_reader = time.time()
  #ppmt273_256_256_256_nrrd = NrrdReader( FileName='/scratch/01336/carson/data/RM/ppmt273_256_256_256.nrrd' )
  # reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')
  # reader = XdmfReader( FileName='/work/00401/pnav/workloads/dns/u_0035_pv.xmf')
  # reader = XDMFReader(FileNames=[data_dir + '/u_0032_pv.xmf'])
  numFiles=geometryLevel
  #name=dns_data_dir+"u_10000.xdmf"
  #name = dns_data_dir+"/u_yz_"+str(numFiles*128)+'.xmf'
  name = data_dir+"/u_"+str(numFiles*256)+'_pv.xmf'


  #reader = XDMFReader(FileNames=[data_dir + '/u_1024_pv.xmf'])
  reader = XDMFReader(FileNames=[name])
  reader.PointArrayStatus = ['dataset0']
  reader.GridStatus = ['Grid_2']
  reader.UpdatePipeline()
  et_reader = time.time()
  tt_reader = et_reader - st_reader
  st_filter = time.time()

  # get active view
  renderView1 = GetActiveViewOrCreate('RenderView')
  # uncomment following to set a specific view size
  # renderView1.ViewSize = [981, 809]

  # show data in view
  u_128xmfDisplay = Show(reader, renderView1)
  # trace defaults for the display properties.
  u_128xmfDisplay.Representation = 'Outline'
  u_128xmfDisplay.ColorArrayName = ['POINTS', '']
  u_128xmfDisplay.ScalarOpacityUnitDistance = 6.8464297236265645
  u_128xmfDisplay.Slice = 767

  # reset view to fit data
  renderView1.ResetCamera()

  # set scalar coloring
  ColorBy(u_128xmfDisplay, ('POINTS', 'dataset0'))

  # rescale color and/or opacity maps used to include current data range
  u_128xmfDisplay.RescaleTransferFunctionToDataRange(True)

  # change representation type
  u_128xmfDisplay.SetRepresentationType('Volume')

  # get color transfer function/color map for 'dataset0'
  dataset0LUT = GetColorTransferFunction('dataset0')
  dataset0LUT.RGBPoints = [-0.05184755101799965, 0.231373, 0.298039, 0.752941, 0.6090234648436308, 0.865003, 0.865003, 0.865003, 1.2698944807052612, 0.705882, 0.0156863, 0.14902]
  dataset0LUT.ScalarRangeInitialized = 1.0

  # get opacity transfer function/opacity map for 'dataset0'
  dataset0PWF = GetOpacityTransferFunction('dataset0')
  dataset0PWF.Points = [-0.05184755101799965, 0.0, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]
  dataset0PWF.ScalarRangeInitialized = 1
  et_filter = time.time()
  tt_filter = (et_filter - st_filter)

  ResetCamera()
  renderView1 = GetActiveView()
  renderView1.Background = [1,1,1]
  renderView1.CameraPosition = [-6051.988379672283, 17509.711278215327, -1388.3905660065536]
  renderView1.CameraFocalPoint = [63.50000000000163, 3839.5000000000027, 767.4999999999978]
  renderView1.CameraViewUp = [0.11947111278233497, -0.10229783033621284, -0.9875534451962862]
  renderView1.CameraParallelScale = 3915.9735379596223
  ResetCamera()
  #cam = GetActiveCamera()
  #cam.Roll(90)
  #cam.Elevation(65)
  #cam.Azimuth(-20)

  #numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  #numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  #numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  #print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  #print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  #print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))
  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':True, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
  return returnVals

def svbRender():
  Render()
