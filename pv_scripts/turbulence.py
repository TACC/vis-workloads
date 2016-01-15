
#### import the simple module from the paraview
from paraview.simple import *
import os
import time 

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


data_dir =  path_vars["TURBULENCEDATA_DIR"]
#rm_data_dir =  path_vars["RMDATA_DIR"]
#print "rm_data_dir:%s" %  rm_data_dir

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

def svbGetStagesSize():
  return 1;

def svbSetup(geometryLevel=1, stage=0):
  # find source
  #enstrophy_0016raw = FindSource('Enstrophy_0016.raw')
  filename = data_dir + '/Enstrophy_0016.raw'
  print "turbulence file:%s" % filename
  enstrophy_0016raw = ImageReader(FilePrefix=filename)

  # Properties modified on enstrophy_0016raw
  enstrophy_0016raw.DataScalarType = 'float'
  enstrophy_0016raw.DataByteOrder = 'LittleEndian'
  enstrophy_0016raw.DataExtent = [0, 511, 0, 511, 0, 511]

  # set active source
  SetActiveSource(enstrophy_0016raw)

  # find source
  #contour1 = FindSource('Contour1')
  contour1 = Contour()

  contour1.PointMergeMethod = "Uniform Binning"
  contour1.ContourBy = ['POINTS', 'ImageFile']
  #contour1.Isosurfaces = isovals
  # Contour1.Isosurfaces = [125.0]
  contour1.PointMergeMethod = 'Uniform Binning'
  contour1.ComputeNormals = 1
  contour1.ComputeScalars = 0
    
  #just checking if Update will work here
  contour1.UpdatePipeline()

  # get active view
  #oSPRayRendered3DView1 = GetActiveView()
  # uncomment following to set a specific view size
  # oSPRayRendered3DView1.ViewSize = [854, 812]

  # hide data in view
  #Hide(contour1, oSPRayRendered3DView1)

  # get color transfer function/color map for 'ImageFile'
  imageFileLUT = GetColorTransferFunction('ImageFile')
  imageFileLUT.LockDataRange = 1
  imageFileLUT.RGBPoints = [2.8211e-07, 0.2549019607843137, 0.30980392156862746, 0.4627450980392157, 0.27272751927375793, 0.0, 0.0, 0.0, 1.727272868156433, 0.03137254901960784, 0.10980392156862745, 0.18823529411764706, 3.5, 0.2, 0.6235294117647059, 0.8509803921568627, 5.045454978942871, 0.13725490196078433, 0.3058823529411765, 0.5098039215686274, 7.636363506317139, 1.0, 0.8588235294117647, 0.0392156862745098, 10.710000080683459, 0.9137254901960784, 0.5882352941176471, 0.058823529411764705, 12.85500004034173, 0.4196078431372549, 0.25882352941176473, 0.0392156862745098, 15.0, 0.878431372549, 0.301960784314, 0.301960784314]
  imageFileLUT.ColorSpace = 'RGB'
  imageFileLUT.ScalarRangeInitialized = 1.0

  # show data in view
  enstrophy_0016rawDisplay = Show()
  # trace defaults for the display properties.
  #enstrophy_0016rawDisplay.Representation = 'Volume'
  enstrophy_0016rawDisplay.ColorArrayName = ['POINTS', 'ImageFile']
  enstrophy_0016rawDisplay.LookupTable = imageFileLUT
  #enstrophy_0016rawDisplay.ScalarOpacityUnitDistance = 1.7320508075688772
  #enstrophy_0016rawDisplay.SamplingRate = 0.125

  enstrophy_0016rawDisplay.Representation = 'Surface'

  # show color bar/color legend
  #enstrophy_0016rawDisplay.SetScalarBarVisibility(oSPRayRendered3DView1, True)

  # destroy contour1
  Delete(contour1)
  del contour1

  # get opacity transfer function/opacity map for 'ImageFile'
  imageFilePWF = GetOpacityTransferFunction('ImageFile')
  imageFilePWF.Points = [2.8211e-07, 0.0, 0.5, 0.0, 1.8181819915771484, 0.0, 0.5, 0.0, 2.909090995788574, 1.0, 0.5, 0.0, 9.590909004211426, 1.0, 0.5, 0.0, 15.0, 1.0, 0.5, 0.0]
  imageFilePWF.ScalarRangeInitialized = 1

  # create a new 'Contour'
  contour1 = Contour(Input=enstrophy_0016raw)
  contour1.ContourBy = ['POINTS', 'ImageFile']
  contour1.Isosurfaces = [117.46282973089858]
  contour1.PointMergeMethod = 'Uniform Binning'

  # Properties modified on contour1
  contour1.Isosurfaces = [6.0]

  # show data in view
  contour1Display = Show()
  # trace defaults for the display properties.
  contour1Display.ColorArrayName = [None, '']
  #contour1Display.ScalarOpacityUnitDistance = 5.202965579094911

  # hide data in view
  #Hide(enstrophy_0016raw, oSPRayRendered3DView1)

  # Properties modified on contour1
  contour1.Isosurfaces = [2.0]

  # set scalar coloring
  ColorBy(contour1Display, ('POINTS', 'Normals'))

  # rescale color and/or opacity maps used to include current data range
  contour1Display.RescaleTransferFunctionToDataRange(True)

  # show color bar/color legend
  #contour1Display.SetScalarBarVisibility(oSPRayRendered3DView1, True)

  # get color transfer function/color map for 'Normals'
  normalsLUT = GetColorTransferFunction('Normals')
  normalsLUT.RGBPoints = [0.999999948778767, 0.231373, 0.298039, 0.752941, 1.000004948828511, 0.865003, 0.865003, 0.865003, 1.0000099488782548, 0.705882, 0.0156863, 0.14902]
  normalsLUT.ScalarRangeInitialized = 1.0
  normalsLUT.RGBPoints = [-0.9999988675117493, 0.10588235294117647, 0.1411764705882353, 0.35294117647058826, -0.36969637870788574, 0.2823529411764706, 0.37254901960784315, 0.8156862745098039, 0.06060626357793808, 0.5607843137254902, 0.6941176470588235, 0.996078431372549, 0.3575757145881653, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.9999993443489075, 0.5372549019607843, 0.1450980392156863, 0.09019607843137255]

  # get opacity transfer function/opacity map for 'Normals'
  normalsPWF = GetOpacityTransferFunction('Normals')
  #normalsPWF.Points = [-0.9999988675117493, 0.0, 0.5, 0.0, -0.9999988675117493, 1.0, 0.5, 0.0, -0.6121204451836184, 1.0, 0.5, 0.0, 0.2787878428269277, 1.0, 0.5, 0.0, 0.9999993443489075, 1.0, 0.5, 0.0]
  normalsPWF.ScalarRangeInitialized = 1
  normalsPWF.Points = [         -0.99999886751174905,         0,         0.5,         0,         -0.99999886751174905,         1,         0.5,         0,         -0.61212044518361797,         1,         0.5,         0,         0.27878784282692798,         1,         0.5,         0,         0.99999934434890703,         1,         0.5,         0]

  #change array component used for coloring
  #normalsLUT.RGBPoints = [-0.9999996423721313, 0.231373, 0.298039, 0.752941, 1.4903381617692446e-07, 0.865003, 0.865003, 0.865003, 0.9999999403953552, 0.705882, 0.0156863, 0.14902]
  normalsLUT.RGBPoints = [         -0.99999886751174905,         0.105882352941176,         0.14117647058823499,         0.35294117647058798,         -0.36969637870788602,         0.28235294117647097,         0.37254901960784298,         0.81568627450980402,         0.060606263577938101,         0.56078431372548998,         0.69411764705882395,         0.99607843137254903,         0.35757571458816501,         0.86666666666666703,         0.86666666666666703,         0.86666666666666703,         0.99999934434890703,         0.53725490196078396,         0.14509803921568601,         0.090196078431372506]
  normalsLUT.VectorMode = 'Component'

  contour1.Isosurfaces = [2.0]

  # current camera placement for oSPRayRendered3DView1
  oSPRayRendered3DView1 = GetActiveView()
  oSPRayRendered3DView1.CameraPosition = [1212.7637365483026, -880.3243683495439, -591.3173709381022]
  oSPRayRendered3DView1.CameraFocalPoint = [255.49999999999997, 255.49999999999997, 255.49999999999997]
  oSPRayRendered3DView1.CameraViewUp = [-0.05097951808799604, 0.5689682866029447, -0.8207777881836381]
  oSPRayRendered3DView1.CameraParallelScale = 442.53898133384814

def svbRender():
  Render()
