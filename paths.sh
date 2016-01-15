#!/bin/bash
SVB_DIR=/work/01336/carson/git/vis-workloads
output_DIR=/work/01336/carson/git/vis-workloads/benchmarks
ParaView_DIR=/work/01336/carson/git/paraview2/buildMaverickICCReleaseGL1/
ParaViewGL2_DIR=/work/01336/carson/git/paraview2/buildMaverickICCReleaseGL2
pvOSPRay_DIR=/opt/apps/intel14/mvapich2_2_0/paraview/4.1.0/bin/../lib
pvVBO_DIR=/opt/apps/intel14/mvapich2_2_0/paraview/4.1.0/bin/../lib
GLuRay_PATH=GLURAY_FIND-NOTFOUND
WRF_PLUGIN_PATH=
GEODATA_DIR=
MOLDATA_DIR=/work/01891/adb/molecule_benchmark
WHIPPLEDATA_DIR=/work/00401/pnav/workloads/Whipple300
ENZODATA_DIR=ENZODATA_DIR_NOTFOUND
WRFDATA_DIR=WRFDATA_DIR-NOTFOUND
DNSDATA_DIR=/work/00401/pnav/workloads/dns
FIUDATA_DIR=/work/00401/pnav/workloads/fiu
RMDATA_DIR=/work/01336/carson/intelTACC/data/rm/unblock
TURBULENCEDATA_DIR=/work/01336/carson/intelTACC/data
ACCOUNT=A-ccvis
SWR_LIB=libGL.so.1
USE_SWR=OFF
USE_GPU=ON
USE_GPU2=ON
IMMEDIATEMODE=OFF
USE_GLURAY=OFF
USE_VBO=OFF
USE_OSPRAY=ON
USE_OSPRAYAO=OFF
USE_SWRVBO=OFF
USE_TACHYON=OFF
LDAV_RUNS=OFF
TACHYONBIN=
TACHYONDATA=
TACHYONDATA_DIR=
USE_FIU_ANIMATED=OFF
USE_FIU=OFF
USE_RM=ON
USE_RM_TIME=OFF
USE_RM_ISOSWEEP=OFF
USE_RM_CLIPSWEEP=OFF
USE_TURBULENCE=ON
USE_DNS=ON
USE_DNS_ISOSWEEP=OFF
USE_DNS_CLIPSWEEP=OFF
USE_MOLECULE=OFF
USE_GEO=OFF
USE_WRF=OFF
USE_WHIPPLE_TIME=OFF
USE_WHIPPLE=OFF
GENERATE_IMAGES=OFF
ROOT_IMAGE_DIR=
MPI_COMMAND=ibrun
ENV_COMMAND=tacc_xrun
HOSTFILE=
RANKS_PER_HOST=
NumNodes="1 2 4 8 16 32"
NumProcs="1"
GeometryLevels=1
