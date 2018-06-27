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

geo_data_dir =  path_vars["GEODATA_DIR"]
print "geo_data_dir:%s" %  geo_data_dir





def svbSetup(geometryLevel=1, stage=0):
	numCells = 0
	numPolys = 0
	numPoints = 0
        returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':True, 'tt_reader':0, 'tt_filter':0};
	paraview.simple._DisableFirstRenderCameraReset()

        st_reader = time.time()
        fname1 = geo_data_dir+"/Top_Albian.obj"
	Top_Albian_obj = WavefrontOBJReader( FileName=fname1 )
	RenderView1 = GetRenderView()

	DataRepresentation2 = Show()
	DataRepresentation2.ScaleFactor = 4038.859375
	DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	RenderView1.CameraFocalPoint = [311041.546875, 3514944.25, 4050.0]
	#RenderView1.CameraClippingRange = [66132.27016710148, 154040.97004230513]
	RenderView1.CameraPosition = [328631.4299478206, 3427661.9289184036, 59588.36001851113]
	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()


        fname2 = geo_data_dir+"/Basement.obj"
	Basement_obj = WavefrontOBJReader( FileName=fname2 )

	DataRepresentation3 = Show()
	DataRepresentation3.ScaleFactor = 3493.5687500000004
	DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	#RenderView1.CameraClippingRange = [64530.62887441108, 155259.5969791027]
	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()


        fname3 = geo_data_dir+"/Base_MTC.obj"
	Base_MTC_obj = WavefrontOBJReader( FileName=fname3 )

	DataRepresentation4 = Show()
	DataRepresentation4.ScaleFactor = 4129.846875
	DataRepresentation4.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	#RenderView1.CameraClippingRange = [64410.7310588127, 155587.59056582034]
	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()
 	fname4 = geo_data_dir+"/Seafloor_zap.asc.obj"
	Seafloor_zap_asc_obj = WavefrontOBJReader( FileName=fname4 )

	DataRepresentation5 = Show()
	DataRepresentation5.ScaleFactor = 5525.181250000001
	DataRepresentation5.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	#RenderView1.CameraClippingRange = [51508.49633040225, 163055.0999913982]
	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

        fname5 = geo_data_dir+"/Basement.obj"
	Top_MTC_obj = WavefrontOBJReader( FileName=fname5 )
        et_reader = time.time()
        tt_reader = (et_reader-st_reader)

	DataRepresentation6 = Show()
	DataRepresentation6.ScaleFactor = 4129.846875
	DataRepresentation6.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	DataRepresentation3.DiffuseColor = [0.6666666666666666, 0.0, 0.0]

	DataRepresentation4.DiffuseColor = [0.47058823529411764, 0.6666666666666666, 0.5803921568627451]

	DataRepresentation2.Visibility = 0

	DataRepresentation6.DiffuseColor = [0.47058823529411764, 0.7372549019607844, 1.0]

	numCells += GetActiveSource().GetDataInformation().GetNumberOfCells()
	numPoints += GetActiveSource().GetDataInformation().GetNumberOfPoints()
	numPolys += GetActiveSource().GetDataInformation().GetPolygonCount()

	SetActiveSource(Seafloor_zap_asc_obj)
        st_filter = time.time()
	Transform1 = Transform( Transform="Transform" )

	Transform1.Transform = "Transform"

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
	Transform1.Transform.Translate = [0.0, 0.0, -4000.0]
        Transform1.UpdatePipeline()

	DataRepresentation7 = Show()
	DataRepresentation7.ScaleFactor = 5525.181250000001
	DataRepresentation7.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation7.DiffuseColor = [1.0, 1.0, 1.0]

	DataRepresentation5.Visibility = 0

	#RenderView1.CameraClippingRange = [50450.00418731889, 166780.99233505165]

	DataRepresentation7.DiffuseColor = [1.0, 0.7843137254901961, 0.5372549019607843]

	SetActiveSource(Top_MTC_obj)
	Transform2 = Transform( Transform="Transform" )

	Transform2.Transform = "Transform"

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
	Transform2.Transform.Translate = [0.0, 0.0, -2000.0]
        Transform2.UpdatePipeline()

	DataRepresentation8 = Show()
	DataRepresentation8.ScaleFactor = 4129.846875
	DataRepresentation8.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation8.DiffuseColor = [1.0, 1.0, 1.0]

	DataRepresentation6.Visibility = 0

	DataRepresentation8.DiffuseColor = [0.47058823529411764, 0.7372549019607844, 1.0]

	DataRepresentation2.Visibility = 1

	SetActiveSource(Basement_obj)
	Transform3 = Transform( Transform="Transform" )

	Transform3.Transform = "Transform"

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
	#RenderView1.CameraClippingRange = [46507.12095433405, 168752.43395154408]

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
	Transform3.Transform.Translate = [0.0, 0.0, 5000.0]
        Transform3.UpdatePipeline()
	DataRepresentation9 = Show()
	DataRepresentation9.ScaleFactor = 3493.5687500000004
	DataRepresentation9.EdgeColor = [0.0, 0.0, 0.5000076295109483]
	DataRepresentation9.DiffuseColor = [1.0, 1.0, 1.0]

	DataRepresentation3.Visibility = 0

	DataRepresentation9.DiffuseColor = [0.592156862745098, 0.0, 0.0]

	SetActiveSource(Top_Albian_obj)
	Transform4 = Transform( Transform="Transform" )

	Transform4.Transform = "Transform"

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
	Transform4.Transform.Translate = [0.0, 0.0, 4000.0]
        Transform4.UpdatePipeline()
        et_filter = time.time()
        tt_filter = (et_filter-st_filter)
	DataRepresentation10 = Show()
	DataRepresentation10.ScaleFactor = 4038.859375
	DataRepresentation10.EdgeColor = [0.0, 0.0, 0.5000076295109483]

	DataRepresentation2.Visibility = 0

	# toggle the 3D widget visibility.
	active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
	Transform3.Transform.Translate = [0.0, 0.0, 2000.0]

	#RenderView1.CameraClippingRange = [48758.99243982868, 167626.49820879675]

	Transform4.Transform.Translate = [0.0, 0.0, 6000.0]

	#RenderView1.CameraClippingRange = [47181.83914663448, 168415.07485539385]

	Transform3.Transform.Translate = [0.0, 0.0, 3000.0]

	Transform4.Transform.Translate = [0.0, 0.0, 9000.0]

	#RenderView1.CameraClippingRange = [44816.109206843845, 169597.93982528918]

	Transform2.Transform.Translate = [0.0, 0.0, -6000.0]

	#RenderView1.CameraClippingRange = [44577.90163585609, 170436.43047516607]

	Transform2.Transform.Translate = [0.0, 0.0, -8000.0]

	RenderView1.CameraViewUp = [0.0, 0.0, 1.0]
	RenderView1.CameraPosition = [317777.46875, 3369926.9481848134, 4338.0]
	#RenderView1.CameraClippingRange = [96496.28879703477, 198458.75384241441]
	RenderView1.InteractionMode = 3
	RenderView1.CameraFocalPoint = [317777.46875, 3511412.375, 4338.0]
	RenderView1.CameraParallelScale = 36619.123064229214
	RenderView1.CenterOfRotation = [317777.46875, 3511412.375, 4338.0]

	Transform1.Transform.Translate = [0.0, 0.0, -8000.0]

	Transform1.Transform.Translate = [0.0, 0.0, -9000.0]

	Transform2.Transform.Translate = [0.0, 0.0, -6000.0]

	Transform2.Transform.Translate = [0.0, 0.0, -4500.0]

	Transform2.Transform.Translate = [0.0, 0.0, -5000.0]

	Transform4.Transform.Translate = [0.0, 0.0, 10000.0]

	RenderView1.CameraViewUp = [0.3401946549046027, 0.2820674051694079, 0.8970538310019835]
	RenderView1.CameraPosition = [256948.26399729348, 3429270.222812952, 50494.51975791374]
	#RenderView1.CameraClippingRange = [40247.273637994265, 203394.3616118409]
	RenderView1.InteractionMode = '3D'
	RenderView1.CameraFocalPoint = [318063.7046413446, 3510067.578090641, 1911.6531775491044]
	RenderView1.CameraParallelScale = 37058.23649598536
	RenderView1.CenterOfRotation = [318063.7046413446, 3510067.578090641, 1911.6531775491044]

	print "numPoints: %.2f million " % (float(numPoints)/(1000*1000.0))
	print "numCells: %.2f million " % (float(numCells)/(1000*1000.0))
	print "numPolys: %.2f million " % (float(numPolys)/(1000*1000.0))

        returnVals = {'azimuth':90, 'dolly':2, 'animateCamera':True, 'tt_reader':tt_reader, 'tt_filter':tt_filter};
        return returnVals

def svbGetStagesSize():
	return 1;


def svbRender():
	Render()
