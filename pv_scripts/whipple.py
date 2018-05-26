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

import os
import sys
import time
try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

# WHIPple ITeration script
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

whipple_data_dir =  path_vars["WHIPPLEDATA_DIR"]
print "whipple_data_dir:%s" %  whipple_data_dir


AnimationScene1 = GetAnimationScene()
timesteps = []

numCells = 0
numPoints = 0
numPolys = 0

def svbSetup(geometryLevel=1,stage=0):

	""" Specify the dataset here. Check to see if it exists
	 (these things have a way of changing places) Check to
	 see if we have access and open it with the Exodus
	 reader if we do.

	 If all is well do the initial file open read and setup.
	 All the svbSetup should do is set the AnimationTime
	 that corresponds to the particular stage/timestep and render
	"""
	print "CALL svbSETUP"
        returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':0.0, 'tt_filter':0.0};
#	datasetpath = whipple_data_dir+"//Whipple_Shield.exo.300.000"
	datasetpath = os.path.join(whipple_data_dir,"Whipple_Shield.exo.300.000")
        print "datasetpath:%s" % datasetpath
        st_reader = time.time()
	if os.path.exists(datasetpath):
		if os.access(datasetpath,os.R_OK):
			Whipple_Shield_exo_300_010 = ExodusIIReader(FileName=[datasetpath])
		else:
			print "Read Permission Denied for: %s\n" % datasetpath
			sys.exit()
	else:
		print "Dataset %s does not exist\n" % datasetpath
		sys.exit()

        et_reader = time.time()
        tt_reader = time.time()
	global AnimationScene1
	global timesteps
        global tt_filter
        returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':0.0, 'tt_filter':0.0};

        numCells = 0
        numPoints = 0
        numPolys = 0

	if stage == 0: #pipeline setup
		timesteps = Whipple_Shield_exo_300_010.TimestepValues
		AnimationScene1.EndTime = timesteps[len(timesteps)-1]
		AnimationScene1.PlayMode = 'Snap To TimeSteps'

		Whipple_Shield_exo_300_010.FileRange = [0, 299]
		Whipple_Shield_exo_300_010.XMLFileName = 'Invalid result'
		#Whipple_Shield_exo_300_010.FilePrefix = whipple_data_dir+'Whipple_Shield.exo.300.'
		Whipple_Shield_exo_300_010.FilePrefix = os.path.join(whipple_data_dir,'Whipple_Shield.exo.300.')
		Whipple_Shield_exo_300_010.ModeShape = 20
		Whipple_Shield_exo_300_010.FilePattern = '%s%03i'


		Whipple_Shield_exo_300_010.NodeSetArrayStatus = []
		Whipple_Shield_exo_300_010.ElementVariables = ['VOID_FRC', 'VOLFRC1', 'VOLFRC2', 'DENSITY']
		Whipple_Shield_exo_300_010.ElementBlocks = ['Unnamed block ID: 1 Type: HEX']

		CellDatatoPointData1 = CellDatatoPointData()

                st_filter1 = time.time()
		Contour1 = Contour(Input=Whipple_Shield_exo_300_010)

		Contour1.PointMergeMethod = "Uniform Binning"
		Contour1.ContourBy = ['POINTS', 'DENSITY']
		Contour1.Isosurfaces = [3943.054656982422]

		Contour1.Isosurfaces = [0.5]
		Contour1.ContourBy = ['POINTS', 'VOLFRC2']
                Contour1.UpdatePipeline()
                et_filter1 = time.time()
                tt_filter1 = (et_filter1 - st_filter1)


		DataRepresentation3 = Show()
		#DataRepresentation3.ScaleFactor = 0.005079999938607216
		DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
		DataRepresentation3.SelectionPointFieldDataArrayName = 'DENSITY'
		DataRepresentation3.SelectionCellFieldDataArrayName = 'DENSITY'

		SetActiveSource(CellDatatoPointData1)

		#Contour2 = Contour( PointMergeMethod="Uniform Binning" )
                st_filter2 = time.time()
		Contour2 = Contour(Input=Whipple_Shield_exo_300_010 )

                Contour2.PointMergeMethod = "Uniform Binning"
                Contour2.ContourBy = ['POINTS', 'DENSITY']
                Contour2.Isosurfaces = [3943.054656982422]

                Contour2.Isosurfaces = [0.5]
                Contour2.ContourBy = ['POINTS', 'VOLFRC1']

                Contour2.UpdatePipeline()
                et_filter2 = time.time()
                tt_filter2 = (et_filter2 - st_filter2)

                tt_filter = tt_filter1 + tt_filter2
		DataRepresentation4 = Show()
		#DataRepresentation4.ScaleFactor = 0.005079999938607216
		DataRepresentation4.EdgeColor = [0.0, 0.0, 0.5000076295109483]
		DataRepresentation4.SelectionPointFieldDataArrayName = 'DENSITY'
		DataRepresentation4.SelectionCellFieldDataArrayName = 'DENSITY'
#		DataRepresentation2.Visibility = 0


	AnimationScene1.AnimationTime = timesteps[stage]
	RenderView1 = GetRenderView()
	RenderView1.CenterOfRotation = [0.0, 0.0, 0.018435800448060036]
	RenderView1.CameraViewUp = [-0.041981806193924054, -0.6484761172246292, -0.7600764786111757]
	RenderView1.CameraPosition = [-0.012931246084195372, 0.05071249414152018, -0.04261877853747655]
	#RenderView1.CameraClippingRange = [0.007083748934846819, 0.1534122165178119]
	RenderView1.CameraFocalPoint = [0.0006400393297762241, -0.008990028403178798, 0.0075681618661409275]
	RenderView1.CameraParallelScale = 0.043921579808790676
        ResetCamera()

        numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
        numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
        numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

        print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
        print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
        print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))
        returnVals = {'azimuth':0, 'dolly':0, 'animateCamera':False, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
        return returnVals


# this function returns the number of time steps.
# Stages are used for time steps in this script.
# The svbSetup function uses the stage to indicate
# what timestep to render.
def svbGetStagesSize():
	global timesteps
	return 5
	#uncomment next line to do the whole time series
	#return len(timesteps);

#def svbSetup(geometryLevel=1, stage=0):
#	global AnimationScene1
#	global timesteps
#	AnimationScene1.AnimationTime = timesteps[stage]
#	Render()
def svbRender():
	Render()
