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
  return 5;


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
  print(rm_data_dir+ '-unblocked/rm_0000.xmf')
  global AnimationScene1
  global timesteps
  if stage == 0:
          st_reader = time.time()
          reader= XDMFReader(FileNames=['/work/00401/pnav/workloads/rm-unblocked/rm_0000.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0001.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0002.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0003.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0004.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0005.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0006.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0007.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0008.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0009.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0010.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0011.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0012.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0013.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0014.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0015.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0016.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0017.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0018.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0019.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0020.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0021.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0022.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0023.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0024.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0025.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0026.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0027.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0028.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0029.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0030.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0031.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0032.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0033.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0034.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0035.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0036.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0037.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0038.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0039.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0040.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0041.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0042.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0043.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0044.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0045.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0046.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0047.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0048.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0049.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0050.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0051.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0052.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0053.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0054.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0055.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0056.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0057.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0058.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0059.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0060.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0061.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0062.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0063.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0064.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0065.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0066.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0067.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0068.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0069.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0070.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0071.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0072.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0073.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0074.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0075.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0076.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0077.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0078.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0079.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0080.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0081.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0082.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0083.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0084.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0085.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0086.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0087.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0088.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0089.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0090.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0091.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0092.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0093.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0094.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0095.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0096.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0097.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0098.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0099.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0100.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0101.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0102.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0103.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0104.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0105.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0106.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0107.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0108.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0109.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0110.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0111.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0112.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0113.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0114.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0115.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0116.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0117.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0118.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0119.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0120.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0121.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0122.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0123.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0124.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0125.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0126.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0127.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0128.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0129.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0130.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0131.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0132.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0133.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0134.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0135.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0136.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0137.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0138.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0139.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0140.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0141.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0142.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0143.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0144.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0145.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0146.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0147.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0148.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0149.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0150.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0151.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0152.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0153.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0154.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0155.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0156.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0157.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0158.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0159.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0160.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0161.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0162.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0163.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0164.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0165.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0166.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0167.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0168.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0169.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0170.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0171.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0172.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0173.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0174.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0175.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0176.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0177.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0178.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0179.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0180.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0181.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0182.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0183.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0184.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0185.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0186.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0187.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0188.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0189.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0190.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0191.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0192.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0193.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0194.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0195.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0196.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0197.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0198.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0199.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0200.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0201.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0202.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0203.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0204.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0205.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0206.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0207.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0208.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0209.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0210.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0211.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0212.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0213.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0214.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0215.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0216.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0217.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0218.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0219.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0220.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0221.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0222.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0223.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0224.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0225.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0226.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0227.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0228.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0229.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0230.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0231.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0232.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0233.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0234.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0235.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0236.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0237.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0238.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0239.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0240.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0241.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0242.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0243.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0244.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0245.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0246.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0247.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0248.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0249.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0250.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0251.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0252.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0253.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0254.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0255.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0256.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0257.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0258.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0259.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0260.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0261.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0262.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0263.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0264.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0265.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0266.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0267.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0268.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0269.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0270.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0271.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0272.xmf', '/work/00401/pnav/workloads/rm-unblocked/rm_0273.xmf'])
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
