#!/bin/bash
SVB_DIR=/work/01336/carson/intelTACC/svb
output_DIR=/work/01336/carson/intelTACC/svb/benchmarks/maverick
ParaView_DIR=/work/01336/carson/ParaView/ParaView-v4.3.1-source/buildStampedeICCDebug/bin
pvOSPRay_DIR=/opt/apps/intel13/mvapich2_1_9/paraview/4.1.0/bin/../lib
pvVBO_DIR=/opt/apps/intel13/mvapich2_1_9/paraview/4.1.0/bin/../lib
GLuRay_PATH=GLURAY_FIND-NOTFOUND
WRF_PLUGIN_PATH=
GEODATA_DIR=/scratch/01891/adb/geo
MOLDATA_DIR=/work/01891/adb/molecule_benchmark
WHIPPLEDATA_DIR=WHIPPLEDATA_DIR-NOTFOUND
ENZODATA_DIR=ENZODATA_DIR_NOTFOUND
WRFDATA_DIR=WRFDATA_DIR-NOTFOUND
DNSDATA_DIR=/work/00401/pnav/workloads/dns
FIUDATA_DIR=FIUDATA_DIR-NOTFOUND
RMDATA_DIR=/work/00401/pnav/workloads/rm
ACCOUNT=Vis-Workload-Charact
SWR_LIB=libGL.so.1
USE_SWR=OFF
USE_GPU=OFF
USE_GLURAY=OFF
USE_VBO=OFF
USE_OSPRAY=OFF
USE_SWRVBO=OFF
USE_TACHYON=OFF
TACHYONBIN=
TACHYONDATA=
TACHYONDATA_DIR=
USE_FIU_ANIMATED=OFF
USE_FIU=OFF
USE_RM=OFF
USE_RM_ISOSWEEP= ON
USE_DNS=OFF
USE_DNS_CLIPSWEEP=ON
USE_MOLECULE=OFF
USE_GEO=OFF
USE_WRF=OFF
USE_WHIPPLE_TIME=OFF
USE_WHIPPLE=OFF
GENERATE_IMAGES=OFF
ROOT_IMAGE_DIR=
MPI_COMMAND=ibrun
HOSTFILE=
RANKS_PER_HOST=
