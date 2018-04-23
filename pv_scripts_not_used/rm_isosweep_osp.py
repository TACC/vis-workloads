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
  global ospIso
  global reader

  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':0, 'tt_filter':0};

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
    st_filter = time.time()
    ospIso.Isosurfaces = isovals
    et_filter = time.time()
    tt_filter = et_filter-st_filter
    returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':0, 'tt_filter':tt_filter};
    return returnVals;

  print "h"
  print(rm_data_dir+"/rm_0273.nhdr")

  if (geometryLevel == 0):
    st_reader = time.time()
    reader = NrrdReader( FileName=rm_data_dir+ '/ppmt273_256_256_256.nrrd' )
    reader.UpdatePipeline()
    et_reader = time.time()
    tt_reader = time.time()
  else:
    st_reader = time.time()
    reader = XDMFReader(FileNames=[rm_data_dir + '/rm_0273.xmf'])
    reader.UpdatePipeline()
    et_reader = time.time()
    tt_reader = (et_reader-st_reader)
    #reader = NrrdReader( FileName=rm_data_dir+ '/rm_0273.nhdr' )
  lut = imageFileLUT = GetColorTransferFunction('ImageFile')

  st_filter = time.time()
  ospIso = ospIsosurface(Input=reader)
  ospIso.Isosurfaces = isovals
  ospIso.UpdatePipeline()
  et_filter = time.time()
  tt_filter = (et_filter-st_filter)

  rep = Show()
  rep.ColorArrayName = ['POINTS','ImageFile']
  rep.LookupTable = lut
  imageFilePWF = GetOpacityTransferFunction('ImageFile')
  rep.SetRepresentationType('Volume')

  renderView1 = GetActiveView()
  renderView1.CameraPosition = [582.5678621725423, 464.5664327088711, 765.7235282760473]
  renderView1.CameraFocalPoint = [127.50000000000001, 127.50000000000006, 127.50000000000001]
  renderView1.CameraViewUp = [-0.08930979131282728, 0.9056097848422845, -0.4146018316090396]
  renderView1.CameraParallelScale = 220.83647796503186
  renderView1.Background = [1,1,1]
  ResetCamera()
  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
  return returnVals

def svbRender():
  Render()
