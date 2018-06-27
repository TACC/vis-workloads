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
    print f
    next(f)
    for line in f:
        print line
        eq_index = line.find('=')
        var_name = line[:eq_index].strip()
        paths = line[eq_index + 1:].strip()
        path_vars[var_name] = paths


mol_data_dir =  path_vars["MOLDATA_DIR"]

def svbSetup(geometryLevel=1, stage=0):
  print "in svbSetup"
  numCells = 0
  numPolys = 0
  numPoints = 0
  paraview.simple._DisableFirstRenderCameraReset()

  returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':True, 'tt_reader':0, 'tt_filter':0};
  print "about to load OBJ"
  st_obj_reader = time.time()
  fname = mol_data_dir+"/bacteriaphage_ribbons.obj"
  #a4RHV_ribbons_obj = WavefrontOBJReader( FileName=fname )
  a4RHV_ribbons_obj = WavefrontOBJReader( FileName=mol_data_dir+'/bacteriaphage_ribbons.obj')
  et_obj_reader = time.time()
  tt_obj_reader = (et_obj_reader-st_obj_reader)

  RenderView1 = GetRenderView()
  RenderView1.CenterOfRotation = [77.85100555419922, 193.92295455932617, 40.27460050582886]

  DataRepresentation1 = Show()
  DataRepresentation1.ScaleFactor = 45.73679962158204
  DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]

  RenderView1.CameraPosition = [77.85100555419922, 193.92295455932617, 1045.196735251777]
  RenderView1.CameraFocalPoint = [77.85100555419922, 193.92295455932617, 40.27460050582886]
  #RenderView1.CameraClippingRange = [888.7225317046486, 1153.617427140539]
  RenderView1.CameraParallelScale = 260.092987317333
  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  print "about to load PDB"
  st_pdb_reader = time.time()
  fname = mol_data_dir+"/1VRI.pdb"
  #a4RHV_pdb = PDBReader( FileName=fname )
  a4RHV_pdb = PDBReader( FileName=mol_data_dir+'/molecule/1VRI.pdb')

  a4RHV_pdb.UpdatePipeline()
  et_pdb_reader = time.time()
  tt_pdb_reader = (et_pdb_reader-st_pdb_reader)

  tt_reader = (tt_pdb_reader+tt_obj_reader)

  DataRepresentation6 = Show()
  DataRepresentation6.EdgeColor = [0.0, 0.0, 0.5000076295109483]
  DataRepresentation6.SelectionPointFieldDataArrayName = 'rgb_colors'
  DataRepresentation6.ColorArrayName = ('POINT_DATA', 'rgb_colors')
  DataRepresentation6.MapScalars = 0
  DataRepresentation6.ScaleFactor = 8.8759998321533
  numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  a3_rgb_colors_PVLookupTable = GetLookupTableForArray( "rgb_colors", 3, RGBPoints=[255.0, 0.23, 0.299, 0.754, 307.8122292025696, 0.865, 0.865, 0.865, 360.62445840513925, 0.706, 0.016, 0.15], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

  a3_rgb_colors_PiecewiseFunction = CreatePiecewiseFunction( Points=[255.0, 0.0, 0.5, 0.0, 360.62445840513925, 1.0, 0.5, 0.0] )

  DataRepresentation7 = Show()

  DataRepresentation6.Opacity = 0.62
  DataRepresentation6.LookupTable = a3_rgb_colors_PVLookupTable

  a3_rgb_colors_PVLookupTable.ScalarOpacityFunction = a3_rgb_colors_PiecewiseFunction
  print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))
  returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':True, 'tt_reader':tt_reader, 'tt_filter':0};
  return returnVals

def svbGetStagesSize():
  return 5;


def svbRender():
  Render()
