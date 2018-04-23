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



  returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False};




  numCells = 0
  numPolys = 0
  numPoints = 0

  global AnimationScene1
  global timesteps
  if stage == 0:
          print(rm_data_dir+ '-unblocked/rm_0000.raw')
          # create a new 'Image Reader'
          reader = ImageReader(FilePrefix=rm_data_dir+'-unblocked/rm_')

          # Properties modified on rm_0000raw
          reader.DataScalarType = 'unsigned char'
          reader.DataExtent = [0, 2047, 0, 2047, 0, 1919]

          # create a new 'Nrrd Reader'
          #reader = XDMFReader(FileNames=[rm_data_dir + '/rm_0000.xmf'])
          #reader = NrrdReader( FileName=rm_data_dir+ '-unblocked/rm_0263.nhdr' )
          #timesteps = reader.TimestepValues
          #timesteps = 273
          #AnimationScene1.EndTime = timesteps[len(timesteps)-1]
          AnimationScene1.NumberOfFrames = 273
          AnimationScene1.PlayMode = 'Snap To TimeSteps'
          #reader.FileRange = [0, 273]
          #reader.XMLFileName = 'Invalid result'
          #reader.FilePrefix = 'rm_data_dir+rm_0000.'
          reader.FilePattern = '%s%04i.raw'



          # Contour1 = Contour( PointMergeMethod="Uniform Binning" )
          Contour1 = Contour(Input=reader)

          Contour1.PointMergeMethod = "Uniform Binning"
          Contour1.ContourBy = ['POINTS', 'ImageFile']
          #Contour1.Isosurfaces = [val]
          Contour1.Isosurfaces = [125.0]
          Contour1.PointMergeMethod = 'Uniform Binning'
          Contour1.ComputeNormals = 1

          DataRepresentation2 = Show()
          DataRepresentation2.ScaleFactor = 25.5
          DataRepresentation2.SelectionPointFieldDataArrayName = 'Normals'
          DataRepresentation2.SetRepresentationType('Surface')


  #adj_time = (stage)
  print "START AnimationsScene1.AnimationTime %s:" %  AnimationScene1.AnimationTime
  AnimationScene1.GetAnimationScene()
  AnimationScene1.AnimationTime = stage
  # update animation scene based on data timesteps
  AnimationScene1.UpdateAnimationUsingDataTimeSteps()
  #AnimationScene1.GoToNext()
  print "END AnimationsScene1.AnimationTime %s:" %  AnimationScene1.AnimationTime
  renderView1 = GetActiveView()
  #displayProperties = GetDisplayProperties(Contour1, renderView1)
  #displayProperties.RescaleTransferFunctionToDataRange(True)
  renderView1.CameraPosition = [582.5678621725423, 464.5664327088711, 765.7235282760473]
  renderView1.CameraFocalPoint = [127.50000000000001, 127.50000000000006, 127.50000000000001]
  renderView1.CameraViewUp = [-0.08930979131282728, 0.9056097848422845, -0.4146018316090396]
  renderView1.CameraParallelScale = 220.83647796503186
  renderView1.Background = [1,1,1]
  ResetCamera()

  #numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
  #numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
  #numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

  #print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
  #print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
  #print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))

  return returnVals

def svbRender():
  Render()
