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

global Contour1
global reader

def svbGetStagesSize():
  return 1;


AnimationScene1 = GetAnimationScene()
timesteps = []

def svbSetup(geometryLevel=1, stage=0):
  global Contour1
  global reader

  #returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False};

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':0, 'tt_filter':0};


  numCells = 0
  numPolys = 0
  numPoints = 0
  print(rm_data_dir+ '/rm_0000.xmf')
  global AnimationScene1
  global timesteps
  if stage == 0:
          st_reader = time.time()
          reader= XDMFReader(FileNames=[rm_data_dir + '/rm_0000.xmf', rm_data_dir + '/rm_0001.xmf', rm_data_dir + '/rm_0002.xmf', rm_data_dir + '/rm_0003.xmf', rm_data_dir + '/rm_0004.xmf', rm_data_dir + '/rm_0005.xmf', rm_data_dir + '/rm_0006.xmf', rm_data_dir + '/rm_0007.xmf', rm_data_dir + '/rm_0008.xmf', rm_data_dir + '/rm_0009.xmf', rm_data_dir + '/rm_0010.xmf', rm_data_dir + '/rm_0011.xmf', rm_data_dir + '/rm_0012.xmf', rm_data_dir + '/rm_0013.xmf', rm_data_dir + '/rm_0014.xmf', rm_data_dir + '/rm_0015.xmf', rm_data_dir + '/rm_0016.xmf', rm_data_dir + '/rm_0017.xmf', rm_data_dir + '/rm_0018.xmf', rm_data_dir + '/rm_0019.xmf', rm_data_dir + '/rm_0020.xmf', rm_data_dir + '/rm_0021.xmf', rm_data_dir + '/rm_0022.xmf', rm_data_dir + '/rm_0023.xmf', rm_data_dir + '/rm_0024.xmf', rm_data_dir + '/rm_0025.xmf', rm_data_dir + '/rm_0026.xmf', rm_data_dir + '/rm_0027.xmf', rm_data_dir + '/rm_0028.xmf', rm_data_dir + '/rm_0029.xmf', rm_data_dir + '/rm_0030.xmf', rm_data_dir + '/rm_0031.xmf', rm_data_dir + '/rm_0032.xmf', rm_data_dir + '/rm_0033.xmf', rm_data_dir + '/rm_0034.xmf', rm_data_dir + '/rm_0035.xmf', rm_data_dir + '/rm_0036.xmf', rm_data_dir + '/rm_0037.xmf', rm_data_dir + '/rm_0038.xmf', rm_data_dir + '/rm_0039.xmf', rm_data_dir + '/rm_0040.xmf', rm_data_dir + '/rm_0041.xmf', rm_data_dir + '/rm_0042.xmf', rm_data_dir + '/rm_0043.xmf', rm_data_dir + '/rm_0044.xmf', rm_data_dir + '/rm_0045.xmf', rm_data_dir + '/rm_0046.xmf', rm_data_dir + '/rm_0047.xmf', rm_data_dir + '/rm_0048.xmf', rm_data_dir + '/rm_0049.xmf', rm_data_dir + '/rm_0050.xmf', rm_data_dir + '/rm_0051.xmf', rm_data_dir + '/rm_0052.xmf', rm_data_dir + '/rm_0053.xmf', rm_data_dir + '/rm_0054.xmf', rm_data_dir + '/rm_0055.xmf', rm_data_dir + '/rm_0056.xmf', rm_data_dir + '/rm_0057.xmf', rm_data_dir + '/rm_0058.xmf', rm_data_dir + '/rm_0059.xmf', rm_data_dir + '/rm_0060.xmf', rm_data_dir + '/rm_0061.xmf', rm_data_dir + '/rm_0062.xmf', rm_data_dir + '/rm_0063.xmf', rm_data_dir + '/rm_0064.xmf', rm_data_dir + '/rm_0065.xmf', rm_data_dir + '/rm_0066.xmf', rm_data_dir + '/rm_0067.xmf', rm_data_dir + '/rm_0068.xmf', rm_data_dir + '/rm_0069.xmf', rm_data_dir + '/rm_0070.xmf', rm_data_dir + '/rm_0071.xmf', rm_data_dir + '/rm_0072.xmf', rm_data_dir + '/rm_0073.xmf', rm_data_dir + '/rm_0074.xmf', rm_data_dir + '/rm_0075.xmf', rm_data_dir + '/rm_0076.xmf', rm_data_dir + '/rm_0077.xmf', rm_data_dir + '/rm_0078.xmf', rm_data_dir + '/rm_0079.xmf', rm_data_dir + '/rm_0080.xmf', rm_data_dir + '/rm_0081.xmf', rm_data_dir + '/rm_0082.xmf', rm_data_dir + '/rm_0083.xmf', rm_data_dir + '/rm_0084.xmf', rm_data_dir + '/rm_0085.xmf', rm_data_dir + '/rm_0086.xmf', rm_data_dir + '/rm_0087.xmf', rm_data_dir + '/rm_0088.xmf', rm_data_dir + '/rm_0089.xmf', rm_data_dir + '/rm_0090.xmf', rm_data_dir + '/rm_0091.xmf', rm_data_dir + '/rm_0092.xmf', rm_data_dir + '/rm_0093.xmf', rm_data_dir + '/rm_0094.xmf', rm_data_dir + '/rm_0095.xmf', rm_data_dir + '/rm_0096.xmf', rm_data_dir + '/rm_0097.xmf', rm_data_dir + '/rm_0098.xmf', rm_data_dir + '/rm_0099.xmf', rm_data_dir + '/rm_0100.xmf', rm_data_dir + '/rm_0101.xmf', rm_data_dir + '/rm_0102.xmf', rm_data_dir + '/rm_0103.xmf', rm_data_dir + '/rm_0104.xmf', rm_data_dir + '/rm_0105.xmf', rm_data_dir + '/rm_0106.xmf', rm_data_dir + '/rm_0107.xmf', rm_data_dir + '/rm_0108.xmf', rm_data_dir + '/rm_0109.xmf', rm_data_dir + '/rm_0110.xmf', rm_data_dir + '/rm_0111.xmf', rm_data_dir + '/rm_0112.xmf', rm_data_dir + '/rm_0113.xmf', rm_data_dir + '/rm_0114.xmf', rm_data_dir + '/rm_0115.xmf', rm_data_dir + '/rm_0116.xmf', rm_data_dir + '/rm_0117.xmf', rm_data_dir + '/rm_0118.xmf', rm_data_dir + '/rm_0119.xmf', rm_data_dir + '/rm_0120.xmf', rm_data_dir + '/rm_0121.xmf', rm_data_dir + '/rm_0122.xmf', rm_data_dir + '/rm_0123.xmf', rm_data_dir + '/rm_0124.xmf', rm_data_dir + '/rm_0125.xmf', rm_data_dir + '/rm_0126.xmf', rm_data_dir + '/rm_0127.xmf', rm_data_dir + '/rm_0128.xmf', rm_data_dir + '/rm_0129.xmf', rm_data_dir + '/rm_0130.xmf', rm_data_dir + '/rm_0131.xmf', rm_data_dir + '/rm_0132.xmf', rm_data_dir + '/rm_0133.xmf', rm_data_dir + '/rm_0134.xmf', rm_data_dir + '/rm_0135.xmf', rm_data_dir + '/rm_0136.xmf', rm_data_dir + '/rm_0137.xmf', rm_data_dir + '/rm_0138.xmf', rm_data_dir + '/rm_0139.xmf', rm_data_dir + '/rm_0140.xmf', rm_data_dir + '/rm_0141.xmf', rm_data_dir + '/rm_0142.xmf', rm_data_dir + '/rm_0143.xmf', rm_data_dir + '/rm_0144.xmf', rm_data_dir + '/rm_0145.xmf', rm_data_dir + '/rm_0146.xmf', rm_data_dir + '/rm_0147.xmf', rm_data_dir + '/rm_0148.xmf', rm_data_dir + '/rm_0149.xmf', rm_data_dir + '/rm_0150.xmf', rm_data_dir + '/rm_0151.xmf', rm_data_dir + '/rm_0152.xmf', rm_data_dir + '/rm_0153.xmf', rm_data_dir + '/rm_0154.xmf', rm_data_dir + '/rm_0155.xmf', rm_data_dir + '/rm_0156.xmf', rm_data_dir + '/rm_0157.xmf', rm_data_dir + '/rm_0158.xmf', rm_data_dir + '/rm_0159.xmf', rm_data_dir + '/rm_0160.xmf', rm_data_dir + '/rm_0161.xmf', rm_data_dir + '/rm_0162.xmf', rm_data_dir + '/rm_0163.xmf', rm_data_dir + '/rm_0164.xmf', rm_data_dir + '/rm_0165.xmf', rm_data_dir + '/rm_0166.xmf', rm_data_dir + '/rm_0167.xmf', rm_data_dir + '/rm_0168.xmf', rm_data_dir + '/rm_0169.xmf', rm_data_dir + '/rm_0170.xmf', rm_data_dir + '/rm_0171.xmf', rm_data_dir + '/rm_0172.xmf', rm_data_dir + '/rm_0173.xmf', rm_data_dir + '/rm_0174.xmf', rm_data_dir + '/rm_0175.xmf', rm_data_dir + '/rm_0176.xmf', rm_data_dir + '/rm_0177.xmf', rm_data_dir + '/rm_0178.xmf', rm_data_dir + '/rm_0179.xmf', rm_data_dir + '/rm_0180.xmf', rm_data_dir + '/rm_0181.xmf', rm_data_dir + '/rm_0182.xmf', rm_data_dir + '/rm_0183.xmf', rm_data_dir + '/rm_0184.xmf', rm_data_dir + '/rm_0185.xmf', rm_data_dir + '/rm_0186.xmf', rm_data_dir + '/rm_0187.xmf', rm_data_dir + '/rm_0188.xmf', rm_data_dir + '/rm_0189.xmf', rm_data_dir + '/rm_0190.xmf', rm_data_dir + '/rm_0191.xmf', rm_data_dir + '/rm_0192.xmf', rm_data_dir + '/rm_0193.xmf', rm_data_dir + '/rm_0194.xmf', rm_data_dir + '/rm_0195.xmf', rm_data_dir + '/rm_0196.xmf', rm_data_dir + '/rm_0197.xmf', rm_data_dir + '/rm_0198.xmf', rm_data_dir + '/rm_0199.xmf', rm_data_dir + '/rm_0200.xmf', rm_data_dir + '/rm_0201.xmf', rm_data_dir + '/rm_0202.xmf', rm_data_dir + '/rm_0203.xmf', rm_data_dir + '/rm_0204.xmf', rm_data_dir + '/rm_0205.xmf', rm_data_dir + '/rm_0206.xmf', rm_data_dir + '/rm_0207.xmf', rm_data_dir + '/rm_0208.xmf', rm_data_dir + '/rm_0209.xmf', rm_data_dir + '/rm_0210.xmf', rm_data_dir + '/rm_0211.xmf', rm_data_dir + '/rm_0212.xmf', rm_data_dir + '/rm_0213.xmf', rm_data_dir + '/rm_0214.xmf', rm_data_dir + '/rm_0215.xmf', rm_data_dir + '/rm_0216.xmf', rm_data_dir + '/rm_0217.xmf', rm_data_dir + '/rm_0218.xmf', rm_data_dir + '/rm_0219.xmf', rm_data_dir + '/rm_0220.xmf', rm_data_dir + '/rm_0221.xmf', rm_data_dir + '/rm_0222.xmf', rm_data_dir + '/rm_0223.xmf', rm_data_dir + '/rm_0224.xmf', rm_data_dir + '/rm_0225.xmf', rm_data_dir + '/rm_0226.xmf', rm_data_dir + '/rm_0227.xmf', rm_data_dir + '/rm_0228.xmf', rm_data_dir + '/rm_0229.xmf', rm_data_dir + '/rm_0230.xmf', rm_data_dir + '/rm_0231.xmf', rm_data_dir + '/rm_0232.xmf', rm_data_dir + '/rm_0233.xmf', rm_data_dir + '/rm_0234.xmf', rm_data_dir + '/rm_0235.xmf', rm_data_dir + '/rm_0236.xmf', rm_data_dir + '/rm_0237.xmf', rm_data_dir + '/rm_0238.xmf', rm_data_dir + '/rm_0239.xmf', rm_data_dir + '/rm_0240.xmf', rm_data_dir + '/rm_0241.xmf', rm_data_dir + '/rm_0242.xmf', rm_data_dir + '/rm_0243.xmf', rm_data_dir + '/rm_0244.xmf', rm_data_dir + '/rm_0245.xmf', rm_data_dir + '/rm_0246.xmf', rm_data_dir + '/rm_0247.xmf', rm_data_dir + '/rm_0248.xmf', rm_data_dir + '/rm_0249.xmf', rm_data_dir + '/rm_0250.xmf', rm_data_dir + '/rm_0251.xmf', rm_data_dir + '/rm_0252.xmf', rm_data_dir + '/rm_0253.xmf', rm_data_dir + '/rm_0254.xmf', rm_data_dir + '/rm_0255.xmf', rm_data_dir + '/rm_0256.xmf', rm_data_dir + '/rm_0257.xmf', rm_data_dir + '/rm_0258.xmf', rm_data_dir + '/rm_0259.xmf', rm_data_dir + '/rm_0260.xmf', rm_data_dir + '/rm_0261.xmf', rm_data_dir + '/rm_0262.xmf', rm_data_dir + '/rm_0263.xmf', rm_data_dir + '/rm_0264.xmf', rm_data_dir + '/rm_0265.xmf', rm_data_dir + '/rm_0266.xmf', rm_data_dir + '/rm_0267.xmf', rm_data_dir + '/rm_0268.xmf', rm_data_dir + '/rm_0269.xmf', rm_data_dir + '/rm_0270.xmf', rm_data_dir + '/rm_0271.xmf', rm_data_dir + '/rm_0272.xmf', rm_data_dir + '/rm_0273.xmf'])
          timesteps = reader.TimestepValues
          reader.UpdatePipeline()
          et_reader = time.time()
          tt_reader = (et_reader-st_reader)

          print("timesteps:")
          print (len(timesteps))
          AnimationScene1.EndTime = timesteps[len(timesteps)-1]
          AnimationScene1.StartTime = 0
          AnimationScene1.PlayMode = 'Snap To TimeSteps'

  if (stage != 0):
    tt_reader = 0.0

  st_filter = time.time()
  Contour1 = Contour(Input=reader)

  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'ImageFile']
  Contour1.Isosurfaces = [125.0]
  Contour1.PointMergeMethod = 'Uniform Binning'
  Contour1.ComputeNormals = 1
  Contour1.UpdatePipeline()
  et_filter = time.time()
  tt_filter = (et_filter-st_filter)
  DataRepresentation2 = Show()
  #DataRepresentation2.ScaleFactor = 25.5
  DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
  DataRepresentation2.SetRepresentationType('Surface')

  RenderView1 = GetActiveView()
  RenderView1.CameraPosition = [582.5678621725423, 464.5664327088711, 765.7235282760473]
  RenderView1.CameraFocalPoint = [127.50000000000001, 127.50000000000006, 127.50000000000001]
  RenderView1.CameraViewUp = [-0.08930979131282728, 0.9056097848422845, -0.4146018316090396]
  RenderView1.CameraParallelScale = 220.83647796503186
  RenderView1.Background = [1,1,1]
  ResetCamera()
  #cam = GetActiveCamera()
  #cam.Roll(90)
  #cam.Elevation(65)
  #cam.Azimuth(-20)

  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))

  AnimationScene1.AnimationTime = timesteps[stage]
  print "AnimationsScene1.AnimationTime %s:" %  AnimationScene1.AnimationTime
  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
  return returnVals


def svbRender():
  Render()
