#!/bin/bash
SVB_DIR=/work/01891/adb/svb_cga
output_DIR=/work/01891/adb/svb_cga/benchmarks
ParaView_DIR=/work/01336/carson/opt/apps/stampede/pvospray/5.0.0/bin
pvOSPRay_DIR=/work/01336/carson/opt/apps/stampede/pvospray/5.0.0/lib
pvVBO_DIR=/work/01336/carson/intelTACC/opt/stampede/lib
GLuRay_PATH=/work/01336/carson/intelTACC/opt/stampede/bin/gluray
WRF_PLUGIN_PATH=/home/01249/gda/plugins/wrf-4.1-mav/libWRFReader.so
GEODATA_DIR=/work/00401/pnav/workloads/geo
MOLDATA_DIR=/work/00401/pnav/workloads/molecule
WHIPPLEDATA_DIR=/work/00401/pnav/workloads/Whipple300
ENZODATA_DIR=ENZODATA_DIR_NOTFOUND
WRFDATA_DIR=/work/00401/pnav/workloads/wrf
DNSDATA_DIR=/work/00401/pnav/workloads/dns-subsets
FIUDATA_DIR=/work/01336/carson/intelTACC/data/fiu
RMDATA_DIR=/work/00401/pnav/workloads/rm
ACCOUNT=A-ccvis
SWR_LIB=/work/01336/carson/opt/apps/swr/3.2/lib/libGL.so.1
USE_SWR=OFF
USE_GPU=ON 
USE_GLURAY=OFF
USE_VBO=OFF
USE_OSPRAY=ON 
USE_SWRVBO=OFF
USE_TACHYON=OFF
LDAV_RUNS=OFF
TACHYONBIN=
TACHYONDATA=
TACHYONDATA_DIR=
USE_FIU_ANIMATED=OFF 
USE_FIU=ON  
USE_RM=ON 
USE_RM_TIME=OFF 
USE_RM_ISOSWEEP=OFF 
USE_RM_CLIPSWEEP=OFF 
USE_DNS=ON  
USE_DNS_VOL=ON  
USE_DNS_ISOSWEEP=ON  
USE_DNS_CLIPSWEEP=ON 
USE_MOLECULE=OFF 
USE_GEO=OFF
USE_WRF=OFF 
USE_WHIPPLE_TIME=OFF
USE_WHIPPLE=OFF
GENERATE_IMAGES=ON
ROOT_IMAGE_DIR=/work/01891/adb/svb_cga/benchmarks_st
MPI_COMMAND=ibrun
HOSTFILE=
RANKS_PER_HOST=
