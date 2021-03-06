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
  return 5;

def svbSetup(geometryLevel=1, stage=0):
  global Contour1
  global reader

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False};

  valRanges = [-0.03,1.26]
  # valRange = valRanges[1]-valRanges[0]
  # val = (float(stage+.5)/float(svbGetStagesSize()))*valRange+valRanges[0]
  #val = (float(stage)/float(svbGetStagesSize()))*valRange + valRanges[0]

  valRanges = [-0.03,0.8]
  valRange = valRanges[1]-valRanges[0]
  val = (float(stage+.5)/float(svbGetStagesSize()))*valRange+valRanges[0]

  if (geometryLevel == 0):
    isovals = [val]
  else:
    isovals = drange(val,val+.46,.46/float(geometryLevel))
    isovals = isovals[:geometryLevel]
  print "isosweep vals: " + str(isovals)

  if (stage != 0):
    #ResetCamera()
    Contour1.Isosurfaces = isovals
    return returnVals;

  numCells = 0
  numPolys = 0
  numPoints = 0

  #ppmt273_256_256_256_nrrd = NrrdReader( FileName='/scratch/01336/carson/data/RM/ppmt273_256_256_256.nrrd' )
  # reader = NrrdReader( FileName='/work/03108/awasim/workloads/rm-unblocked/rm_0273.nhdr')
  # reader = XdmfReader( FileName='/work/00401/pnav/workloads/dns/u_0035_pv.xmf')
  # reader = XDMFReader(FileNames=[data_dir + '/u_0032_pv.xmf'])
  reader = XDMFReader(FileNames=[data_dir + '/u_1024_pv.xmf'])
  reader.PointArrayStatus = ['dataset0']
  reader.GridStatus = ['Grid_2']

  Contour1 = Contour(Input=reader)

  Contour1.PointMergeMethod = "Uniform Binning"
  Contour1.ContourBy = ['POINTS', 'dataset0']
  #data range for smaller 32 is -.0299 to 1.268
  Contour1.Isosurfaces = isovals
  Contour1.ComputeNormals = 1
  Contour1.ComputeScalars = 1

  lut = imageFileLUT = GetColorTransferFunction('dataset0')
  lut.RescaleTransferFunction(-.03,1.26)

  rep = Show()
  rep.LookupTable = lut
  #DataRepresentation2.ScaleFactor = 25.5
  # DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
  rep.SetRepresentationType('Surface')
  rep.ColorArrayName = ['POINTS','dataset0']
  #DataRepresentation2.ColorArrayName = ['POINTS', '']

  ResetCamera()
  renderView1 = GetActiveView()
  renderView1.Background = [1,1,1]
  renderView1.CameraPosition = [5630.224162601005, -6026.47810866812, 6733.205518587123]
  renderView1.CameraFocalPoint = [336.5950056411767, 3593.3184025734727, 534.8053287858077]
  renderView1.CameraViewUp = [-0.08525959200958713, 0.5060899960109523, 0.8582562076140161]
  renderView1.CameraParallelScale = 3948.7274848994075
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

  return returnVals

def svbRender():
  Render()
