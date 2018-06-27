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
paraview.simple._DisableFirstRenderCameraReset()
import os

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



wrf_plugin_path =  path_vars["WRF_PLUGIN_PATH"]
print "wrf_plugin_path:%s" %  wrf_plugin_path
LoadPlugin(wrf_plugin_path, True, globals())
print "Happy"

AnimationScene1 = GetAnimationScene()
timesteps = []
def svbSetup(geometryLevel=1,stage=0):

    wrfdata=path_vars['WRFDATA_DIR']
    ## Previous location : /work/01891/adb/wrf/
    wrfout_d01_20100623_2300 = WRFReader( FileNames=[
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:00.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:03.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:06.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:09.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:12.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:15.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:18.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:21.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:24.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:27.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:30.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:33.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:36.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:39.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:42.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:45.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:48.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:51.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:54.wrf'),
    os.path.join(wrfdata,'wrfout_d01_2010-06-23_23:00:57.wrf')] )

    global AnimationScene1
    global timestep
    if stage == 0: #pipeline setup
        #timesteps = wrfout_d01_2010-06-23_23:00:00.TimestepValues
        timestep = 0
        AnimationScene1 = GetAnimationScene()
	AnimationScene1.EndTime = 19.0
        #AnimationScene1.EndTime = timesteps[len(timesteps)-1]
        AnimationScene1.PlayMode = 'Snap To TimeSteps'


	RenderView1 = GetRenderView()
	RenderView1.CenterOfRotation = [920107.625, 4659676.5, 10687.688659667969]

	DataRepresentation1 = Show()
	DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation1.SelectionPointFieldDataArrayName = 'LatLon'
	DataRepresentation1.DiffuseColor = [0.0, 0.0, 0.0]
	DataRepresentation1.ScalarOpacityUnitDistance = 451.08230132663226
	DataRepresentation1.AllowSpecularHighlightingWithScalarColoring = 1
	DataRepresentation1.BackfaceDiffuseColor = [0.0, 0.0, 0.0]
	DataRepresentation1.ScaleFactor = 23847.95
	DataRepresentation1.Representation = 'Outline'

	RenderView1.CameraPosition = [920107.625, 4659676.5, 780890.2297729854]
	RenderView1.CameraFocalPoint = [920107.625, 4659676.5, 10687.688659667969]
	#RenderView1.CameraClippingRange = [741560.4942599236, 808114.7519500491]
	RenderView1.CameraParallelScale = 201364.0638101263

	Contour1 = Contour( PointMergeMethod="Uniform Binning" )

	Contour1.PointMergeMethod = "Uniform Binning"
	Contour1.ContourBy = ['POINTS', 'QRAIN']
	Contour1.Isosurfaces = [0.011957924805756193]

	Contour1.Isosurfaces = [0.0001, 0.0012000000000000001, 0.0023, 0.0034, 0.0045, 0.0056, 0.006699999999999999, 0.0078000000000000005, 0.0089, 0.01]
	Contour1.ComputeScalars = 1

	DataRepresentation2 = Show()
	DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation2.SelectionPointFieldDataArrayName = 'QRAIN'
	DataRepresentation2.DiffuseColor = [0.0, 0.0, 0.0]
	DataRepresentation2.ColorArrayName = ('POINT_DATA', 'QRAIN')
	DataRepresentation2.AllowSpecularHighlightingWithScalarColoring = 1
	DataRepresentation2.BackfaceDiffuseColor = [0.0, 0.0, 0.0]
	DataRepresentation2.ScaleFactor = 22330.112500000003

	a1_QRAIN_PVLookupTable = GetLookupTableForArray( "QRAIN", 1, RGBPoints=[9.999999747378752e-05, 0.23, 0.299, 0.754, 0.005049999886978185, 0.865, 0.865, 0.865, 0.009999999776482582, 0.706, 0.016, 0.15], VectorMode='Magnitude', NanColor=[0.25, 0.0, 0.0], ColorSpace='Diverging', ScalarRangeInitialized=1.0 )

	a1_QRAIN_PiecewiseFunction = CreatePiecewiseFunction( Points=[9.999999747378752e-05, 0.0, 0.5, 0.0, 0.009999999776482582, 1.0, 0.5, 0.0] )

	DataRepresentation2.LookupTable = a1_QRAIN_PVLookupTable

	a1_QRAIN_PVLookupTable.RGBPoints = [0.0001, 0.0, 0.0, 0.0, 0.005050000000000001, 0.0, 1.0, 0.0, 0.01, 1.0, 0.0, 0.0]
	a1_QRAIN_PVLookupTable.NanColor = [0.498039, 0.0, 0.0]
	a1_QRAIN_PVLookupTable.NumberOfTableValues = 10
	a1_QRAIN_PVLookupTable.ScalarOpacityFunction = a1_QRAIN_PiecewiseFunction
	a1_QRAIN_PVLookupTable.ColorSpace = 'RGB'
	a1_QRAIN_PVLookupTable.LockScalarRange = 1

	#RenderView1.CameraClippingRange = [741560.3076220452, 808115.408915381]

	a1_QRAIN_PiecewiseFunction.Points = [0.0001, 0.0, 0.5, 0.0, 0.01, 1.0, 0.5, 0.0]

	Clip1 = Clip( ClipType="Plane" )

	Clip1.Scalars = ['POINTS', 'QRAIN']
	Clip1.ClipType.Origin = [921181.4375, 4641210.0, 5268.193428039551]
	Clip1.ClipType = "Plane"
	Clip1.Value = 0.005049999886978185

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
	#RenderView1.CameraClippingRange = [546767.8552096306, 1065573.1512273927]

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
	#RenderView1.CameraClippingRange = [741560.3076220452, 808115.408915381]

	Clip1.ClipType.Origin = [921181.4375, 4641210.0, 1980.0]
	Clip1.ClipType.Normal = [0.0, 0.0, -1.0]

	DataRepresentation3 = Show()
	DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation3.SelectionPointFieldDataArrayName = 'QRAIN'
	DataRepresentation3.DiffuseColor = [0.0, 0.0, 0.0]
	DataRepresentation3.ScalarOpacityFunction = a1_QRAIN_PiecewiseFunction
	DataRepresentation3.ColorArrayName = ('POINT_DATA', 'QRAIN')
	DataRepresentation3.ScalarOpacityUnitDistance = 2033.6069985150987
	DataRepresentation3.AllowSpecularHighlightingWithScalarColoring = 1
	DataRepresentation3.LookupTable = a1_QRAIN_PVLookupTable
	DataRepresentation3.BackfaceDiffuseColor = [0.0, 0.0, 0.0]
	DataRepresentation3.ScaleFactor = 22311.725000000002

	DataRepresentation2.Visibility = 0

	PeoriaMuskegon_vts = XMLStructuredGridReader( FileName=['/work/02029/foss/maverick/PARAVIEW/WRF/new/Peoria-Muskegon.vts'] )

	PeoriaMuskegon_vts.PointArrayStatus = ['TextureCoordinates', 'LatLon']

	DataRepresentation4 = Show()
	DataRepresentation4.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation4.SelectionPointFieldDataArrayName = 'LatLon'
	DataRepresentation4.DiffuseColor = [0.0, 0.0, 0.0]
	DataRepresentation4.ScalarOpacityUnitDistance = 19757.126626479872
	DataRepresentation4.AllowSpecularHighlightingWithScalarColoring = 1
	DataRepresentation4.BackfaceDiffuseColor = [0.0, 0.0, 0.0]
	DataRepresentation4.ScaleFactor = 31734.362500000003

	#RenderView1.CameraClippingRange = [741477.9618502556, 808405.2660320802]

	DataRepresentation4.Position = [500000.0, 0.0, 0.0]
	DataRepresentation4.Texture = []

    AnimationScene1.AnimationTime = timesteps[stage]
    AnimationScene1.AnimationTime = stage
    RenderView1 = GetRenderView()
    RenderView1.CameraPosition = [922139.625, 4643921.75, 977019.3275101203]
    RenderView1.CameraFocalPoint = [922139.625, 4643921.75, 10605.15625]
    #RenderView1.CameraClippingRange = [935645.7686100191, 1007476.3002352722]
    RenderView1.CenterOfRotation = [922139.625, 4643921.75, 10605.15625]
    RenderView1.CameraParallelScale = 252662.22124811474

# what timestep to render.
def svbGetStagesSize():
    global timesteps
    return 1

def svbRender():
    Render()
