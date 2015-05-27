#/**********************************************************************************
#*                     Copyright (c) 2013-2015 Carson Brownlee
#*         Texas Advanced Computing Center, University of Texas at Austin
#*                       All rights reserved
#* 
#*       This library is free software; you can redistribute it and/or
#* modify it under the terms of the GNU Lesser General Public
#* License as published by the Free Software Foundation; either
#* version 2.1 of the License, or (at your option) any later version.
#* 
#* This library is distributed in the hope that it will be useful,
#* but WITHOUT ANY WARRANTY; without even the implied warranty of
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#* Lesser General Public License for more details.
#* 
#* You should have received a copy of the GNU Lesser General Public
#* License along with this library; if not, write to the Free Software
#* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#**********************************************************************************/

CMAKE_MINIMUM_REQUIRED(VERSION 2.6.4)

PROJECT(svb)

SET(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/CMake)

#
# variables that contain the root svb directory and
# the directory that will contain all of the output
#
SET(SVB_DIR ${PROJECT_SOURCE_DIR} CACHE STRING "root SVB directory")
SET(output_DIR ${PROJECT_SOURCE_DIR}/benchmarks CACHE STRING "output directory")

# place. if not do something like module load paraview to get the paths
# correctly set. If paraview is not found nothing will run. 
#
find_file(PV_FINDO NAMES pvbatch)
if(${PV_FINDO} MATCHES "PV_FINDO-NOTFOUND")
	MESSAGE(SEND_ERROR "pvbatch not found " )
endif(${PV_FINDO} MATCHES "PV_FINDO-NOTFOUND")
get_filename_component(PV_FIND ${PV_FINDO} PATH)
SET(ParaView_DIR ${PV_FIND} CACHE STRING "root SVB directory")
SET(pvOSPRay_DIR ${PV_FIND}/../lib CACHE STRING "root SVB directory")
SET(pvVBO_DIR ${PV_FIND}/../lib CACHE STRING "root SVB directory")



#
#tachyon (will update this to find the tachyon binary as above)
#

SET(TACHYONBIN ${TACHYONBIN} CACHE STRING "Tachyon renderer")
SET(TACHYONDATA ${TACHYONDATA} CACHE STRING "Tachyon datafile")
SET(TACHYONDATA_DIR ${TACHYONDATAi_DIR} CACHE STRING "Tachyon directorya")








#
# find the gluray stuff. 
#
find_file(GLURAY_FIND NAMES gluray)
if(${GLURAY_FIND} MATCHES "GLURAY_FIND-NOTFOUND")
	MESSAGE(SEND_ERROR "Gluray not found " )
endif(${GLURAY_FIND} MATCHES "GLURAY_FIND-NOTFOUND")
SET(GLuRay_PATH ${GLURAY_FIND} CACHE STRING "root SVB directory")
SET(SWR_LIB libGL.so.1 CACHE STRING "root SVB directory")
#
# set the accounting info. What account do I charge this to
#
set(ACCOUNT Vis-Workload-Charact CACHE STRING "account to charge to")
#
# set the renderer and dataSources. Setting to ON includes the
# renderer or dataSource in the batch scripts collection.
#
set(USE_SWR OFF CACHE BOOL "use swr renderer")
set(USE_GPU OFF CACHE BOOL "use gpu renderer")
set(USE_GLURAY OFF CACHE BOOL "use gluray renderer")
set(USE_VBO OFF CACHE BOOL "use vbo renderer")
set(USE_OSPRAY OFF CACHE BOOL "use ospray renderer")
set(USE_SWRVBO OFF CACHE BOOL "use swrvbo renderer")
set(USE_TACHYON OFF CACHE BOOL "use vmd tachyon renderer")


# DATA
set(USE_FIU_ANIMATED OFF CACHE BOOL "run fiu animated data")
set(USE_FIU OFF CACHE BOOL "run fiu data")
set(USE_RM OFF CACHE BOOL "run the rm data")
set(USE_DNS OFF CACHE BOOL "run the dns data")
set(USE_MOLECULE OFF CACHE BOOL "run the pv molecule data")
set(USE_GEO OFF CACHE BOOL "run the geo data")
set(USE_WHIPPLE OFF CACHE BOOL "run whipple shield data")
set(USE_WHIPPLE_TIME OFF CACHE BOOL "run the whipple shield time series data")


#OTHER OPTIONS
set(GENERATE_IMAGES OFF CACHE BOOL "generate images")
SET(ROOT_IMAGE_DIR ${ROOT_IMAGE_DIR} CACHE STRING "root image dir")


#
# Where the data is
#
find_file(GEODATA NAMES Top_Albian_large_normals_fixed.obj PATHS /scratch/01891/adb/geo)
if(${GEODATA} MATCHES "GEODATA-NOTFOUND")
	set(GEODATA_DIR "GEODATA_DIR-NOTFOUND" CACHE PATH "geo data directory")
	MESSAGE(SEND_ERROR "geo data not found " )
endif(${GEODATA} MATCHES "GEODATA-NOTFOUND")
get_filename_component(GEODATAD ${GEODATA} PATH)
set(GEODATA_DIR ${GEODATAD} CACHE PATH "geo data directory")

find_file(MOLDATA NAMES 1VRI.pdb PATHS /work/01891/adb/molecule_benchmark)
if(${MOLDATA} MATCHES "MOLDATA-NOTFOUND")
	set(MOLDATA_DIR "MOLDATA_DIR-NOTFOUND" CACHE PATH "molecular data directory")
	MESSAGE(SEND_ERROR "molecule data not found " )
endif(${MOLDATA} MATCHES "MOLDATA-NOTFOUND")
get_filename_component(MOLDATAD ${MOLDATA} PATH)
set(MOLDATA_DIR ${MOLDATAD} CACHE PATH "molecular data directory")

find_file(DNSDATA NAMES u_yz_128.xmf PATHS /scratch/01336/carson/intelTACC/dns)
if(${DNSDATA} MATCHES "DNSDATA-NOTFOUND")
	set(DNSDATA_DIR "DNSDATA_DIR-NOTFOUND" CACHE PATH "DNS data directory")
	MESSAGE(SEND_ERROR "DNS data not found " )
endif(${DNSDATA} MATCHES "DNSDATA-NOTFOUND")
get_filename_component(DNSDATAD ${DNSDATA} PATH)
set(DNSDATA_DIR ${DNSDATAD} CACHE PATH "DNS data directory")

find_file(RMDATA NAMES ppmt273_256_256_256.nrrd PATHS /scratch/01336/carson/intelTACC/rm)
if(${RMDATA} MATCHES "RMDATA-NOTFOUND")
	set(RMDATA_DIR "RMDATA_DIR-NOTFOUND" CACHE PATH "RM data directory")
	MESSAGE(SEND_ERROR "RM data not found " )
endif(${RMDATA} MATCHES "RMDATA-NOTFOUND")
get_filename_component(RMDATAD ${RMDATA} PATH)
set(RMDATA_DIR ${RMDATAD} CACHE PATH "RM data directory")

find_file(FIUDATA NAMES rho_380x380x828_frame0010_subs00.nhdr PATHS /scratch/01336/carson/intelTACC/fiu)
if(${FIUDATA} MATCHES "FIUDATA-NOTFOUND")
	set(FIUDATA_DIR "FIUDATA_DIR-NOTFOUND" CACHE PATH "FIU data directory")
	MESSAGE(SEND_ERROR "FIU data not found " )
endif(${FIUDATA} MATCHES "FIUDATA-NOTFOUND")
get_filename_component(FIUDATAD ${FIUDATA} PATH)
set(FIUDATA_DIR ${FIUDATAD} CACHE PATH "FIU data directory")

find_file(WHIPPLEDATA NAMES Whipple_Shield.exo.300.000 PATHS /scratch/01336/carson/intelTACC/data/Whipple300)
if(${WHIPPLEDATA} MATCHES "WHIPPLEDATA-NOTFOUND")
	set(WHIPPLEDATA_DIR "WHIPPLEDATA_DIR-NOTFOUND" CACHE PATH "WHIPPLE data directory")
	MESSAGE(SEND_ERROR "WHIPPLE data not found " )
endif(${WHIPPLEDATA} MATCHES "WHIPPLEDATA-NOTFOUND")
get_filename_component(WHIPPLEDATAD ${WHIPPLEDATA} PATH)
set(WHIPPLEDATA_DIR ${WHIPPLEDATAD} CACHE PATH "WHIPPLE data directory")

find_file(ENZODATA NAMES DD0174.cpu0000 PATHS /work/01891/adb/maverick/DD0174)
if(${ENZODATA} MATCHES "ENZODATA-NOTFOUND")
	set(ENZODATA_DIR "ENZODATA_DIR_NOTFOUND" CACHE PATH "ENZO data directory")
	MESSAGE(SEND_ERROR "ENZO data not found " )
endif(${ENZODATA} MATCHES "ENZODATA-NOTFOUND")
get_filename_component(ENZODATAD ${ENZODATA} PATH)
set(ENZODATA_DIR ${ENZODATAD} CACHE PATH "ENZO data directory")

find_file(WRFDATA NAMES file.wrf PATHS /work/01891/adb/maverick)
if(${WRFDATA} MATCHES "WRFDATA-NOTFOUND")
	set(WRFDATA_DIR "WRFDATA_DIR-NOTFOUND" CACHE PATH "WRF data directory")
	MESSAGE(SEND_ERROR "WRF data not found " )
endif(${WRFDATA} MATCHES "WRFDATA-NOTFOUND")
get_filename_component(WRFDATAD ${WRFDATA} PATH)
set(WRFDATA_DIR ${WRFDATAD} CACHE PATH "WRF data directory")

#
# set how mpi programs are launched. default is ibrun
# Note: mpirun and ibrun should be in your path or this wont work. 
#
if(NOT MPI_COMMAND)
	set(MPI_COMMAND "ibrun" CACHE STRING "Command used to launch mpi jobs: ibrun, mpirun")
endif(NOT MPI_COMMAND)

#
# if mpi uses mpirun look for a hostfile, set the ranks per node. -hostfile  <hosts >  -perhost <ranks-per-host>
# look in the directory where this file is for the hosts file used with mpi
#
if(${MPI_COMMAND} MATCHES "mpirun")
	find_file(HOSTFILE NAMES hosts PATHS $CMAKE_CURRENT_LIST_DIR )
	set(RANKS_PER_HOST "1" CACHE STRING "number of mpi ranks to start per node")
endif(${MPI_COMMAND} MATCHES "mpirun")

SET(PND \# CACHE INTERNAL STRING )
FILE(REMOVE ${PROJECT_BINARY_DIR}/paths.sh)
FILE(WRITE ${PROJECT_BINARY_DIR}/paths.sh
  ${PND}!/bin/bash\n
  "SVB_DIR=" ${SVB_DIR}\n
  "output_DIR=" ${output_DIR}\n
  "ParaView_DIR=" ${ParaView_DIR}\n
  "pvOSPRay_DIR=" ${pvOSPRay_DIR}\n
  "pvVBO_DIR=" ${pvVBO_DIR}\n
  "GLuRay_PATH=" ${GLuRay_PATH}\n
  "GEODATA_DIR=" ${GEODATA_DIR}\n
  "MOLDATA_DIR=" ${MOLDATA_DIR}\n
  "WHIPPLEDATA_DIR=" ${WHIPPLEDATA_DIR}\n
  "ENZODATA_DIR=" ${ENZODATA_DIR}\n
  "WRFDATA_DIR=" ${WRFDATA_DIR}\n
  "DNSDATA_DIR=" ${DNSDATA_DIR}\n
  "FIUDATA_DIR=" ${FIUDATA_DIR}\n
  "RMDATA_DIR=" ${RMDATA_DIR}\n
  "ACCOUNT=" ${ACCOUNT}\n
  "SWR_LIB=" ${SWR_LIB}\n
  "USE_SWR=" ${USE_SWR}\n
  "USE_GPU=" ${USE_GPU}\n
  "USE_GLURAY=" ${USE_GLURAY}\n
  "USE_VBO=" ${USE_VBO}\n
  "USE_OSPRAY=" ${USE_OSPRAY}\n
  "USE_SWRVBO=" ${USE_SWRVBO}\n
  "USE_TACHYON=" ${USE_TACHYON}\n
  "TACHYONBIN=" ${TACHYONBIN}\n
  "TACHYONDATA=" ${TACHYONDATA}\n
  "TACHYONDATA_DIR=" ${TACHYONDATA_DIR}\n
  "USE_FIU_ANIMATED=" ${USE_FIU_ANIMATED}\n
  "USE_FIU=" ${USE_FIU}\n
  "USE_RM=" ${USE_RM}\n
  "USE_DNS=" ${USE_DNS}\n
  "USE_MOLECULE=" ${USE_MOLECULE}\n
  "USE_GEO=" ${USE_GEO}\n
  "USE_WHIPPLE_TIME=" ${USE_WHIPPLE_TIME}\n
  "USE_WHIPPLE=" ${USE_WHIPPLE}\n
  "GENERATE_IMAGES=" ${GENERATE_IMAGES}\n
  "ROOT_IMAGE_DIR=" ${ROOT_IMAGE_DIR}\n
  "MPI_COMMAND=" ${MPI_COMMAND}\n
  "HOSTFILE=" ${HOSTFILE}\n
  "RANKS_PER_HOST=" ${RANKS_PER_HOST}\n
  )
