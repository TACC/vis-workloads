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

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XDMF Reader'
u_128xmf = XDMFReader(FileNames=['/work/00401/pnav/workloads/dns/u_128.xmf'])
u_128xmf.PointArrayStatus = ['dataset0']

# Properties modified on u_128xmf
u_128xmf.GridStatus = ['Grid_2']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [981, 809]

# show data in view
u_128xmfDisplay = Show(u_128xmf, renderView1)
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

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.00657894741743803, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.02631578966975212, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.09210526198148727, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.15789474546909332, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.2763157784938812, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.32894736528396606, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.33552631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.3552631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.3815789520740509, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.43421053886413574, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5526315569877625, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.6644737124443054, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.6842105388641357, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.6907894611358643, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.6973684430122375, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.7105263471603394, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.7434210777282715, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.8092105388641357, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.8552631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.8947368264198303, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.9473684430122375, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 1.0, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.9934210777282715, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.9736841917037964, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.8684210777282715, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.8355263471603394, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.7894737124443054, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.7368420958518982, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.7236841917037964, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.7105263471603394, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.6710526347160339, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.6381579041481018, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.6118420958518982, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5986841917037964, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5921052694320679, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5855263471603394, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5723684430122375, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5592105388641357, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5263158082962036, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5065789222717285, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.4868420958518982, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.4802631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.46710526943206787, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.44736841320991516, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.42105263471603394, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.3881579041481018, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.34210526943206787, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.2763157784938812, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.2565789520740509, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.2631579041481018, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.30921053886413574, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.33552631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.34210526943206787, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.28289473056793213, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.2368421107530594, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.21052631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.15131579339504242, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.10526315867900848, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.07894737273454666, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.05921052768826485, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.04605263099074364, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.02631578966975212, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.01315789483487606, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.00657894741743803, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.0, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.00657894741743803, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.0, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.00657894741743803, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.17105263471603394, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.34210526943206787, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.45394736528396606, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.46052631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.46710526943206787, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.4934210479259491, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.6447368264198303, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.9539473652839661, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 1.0, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.9802631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.9210526347160339, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.8618420958518982, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.7302631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.6447368264198303, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5723684430122375, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5526315569877625, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5328947305679321, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5263158082962036, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.5197368264198303, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.00657894741743803, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.019736843183636665, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.032894738018512726, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.04605263099074364, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.07894737273454666, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.08552631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.09868421405553818, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.1184210553765297, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.11184210330247879, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.1381578892469406, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.33552631735801697, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.3815789520740509, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.40789473056793213, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.05184755101799965, 0.41447368264198303, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, -0.05184755101799965, 0.41447368264198303, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, -0.023257514461874962, 0.43421053886413574, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.10055491328239441, 0.46710526943206787, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.238124281167984, 0.5263158082962036, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.2725166082382202, 0.5460526347160339, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.27939507365226746, 0.5460526347160339, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.2931520342826843, 0.5592105388641357, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.27939507365226746, 0.5592105388641357, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.2725166082382202, 0.5592105388641357, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.2725166082382202, 0.5526315569877625, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.2174888700246811, 0.5197368264198303, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.2037319391965866, 0.5131579041481018, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# Properties modified on dataset0PWF
dataset0PWF.Points = [-0.9862430691719055, 0.01315789483487606, 0.5, 0.0, 0.2037319391965866, 0.5065789222717285, 0.5, 0.0, 1.2698944807052612, 1.0, 0.5, 0.0]

# rescale color and/or opacity maps used to exactly fit the current data range
u_128xmfDisplay.RescaleTransferFunctionToDataRange(False)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-6051.988379672283, 17509.711278215327, -1388.3905660065536]
renderView1.CameraFocalPoint = [63.50000000000163, 3839.5000000000027, 767.4999999999978]
renderView1.CameraViewUp = [0.11947111278233497, -0.10229783033621284, -0.9875534451962862]
renderView1.CameraParallelScale = 3915.9735379596223

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
