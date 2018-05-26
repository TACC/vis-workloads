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
# SVBench: Scientific Visualization Benchmarking Suite is funded in part by an Intel Cooperation award
#   ======================================================================================= */

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

PROJECT(svb)

SET(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/CMake)

mark_as_advanced(CMAKE_INSTALL_PREFIX)
mark_as_advanced(CMAKE_BUILD_TYPE)
mark_as_advanced(CMAKE_OSX_ARCHITECTURES)
mark_as_advanced(CMAKE_OSX_SYSROOT)
mark_as_advanced(CMAKE_OSX_DEPLOYMENT_TARGET)
#
# variables that contain the root svb directory and
# the directory that will contain all of the output
#

SET(SVB_DIR ${PROJECT_SOURCE_DIR} CACHE PATH "Root SVB directory")
SET(SVB_OUTPUT_DIR ${PROJECT_SOURCE_DIR}/benchmarks CACHE PATH "Output directory")
SET(SVB_DATA_DIR ${PROJECT_SOURCE_DIR}/data CACHE PATH "Data directory")
set(SVB_GENERATE_IMAGES OFF CACHE BOOL "generate images")
set(SVB_NUMBER_OF_RUNS "50" CACHE STRING "Number of runs after warmup")
if(SVB_GENERATE_IMAGES)
	SET(SVB_IMAGE_DIR ${SVB_OUTPUT_DIR}/images} CACHE PATH "Save images to")
endif()

# place. if not do something like module load paraview to get the paths
# correctly set. If paraview is not found nothing will run.
#
find_file(PV_FINDO NAMES pvbatch pvpython)
if(${PV_FINDO} MATCHES "PV_FINDO-NOTFOUND")
	MESSAGE("pvbatch not found, please add Paraview to PATH " )
else()
	get_filename_component(PV_FIND ${PV_FINDO} PATH)
	SET(ParaView_DIR ${PV_FIND} CACHE STRING "ParaView build directory directory")
	SET(ParaViewGL2_DIR ${PV_FIND} CACHE STRING "ParaView build directory with OpenGL2 directory")
	SET(pvOSPRay_DIR ${ParaView_DIR}/../lib CACHE STRING "root SVB directory")
	SET(pvVBO_DIR ${ParaView_DIR}/../lib CACHE STRING "root SVB directory")
endif(${PV_FINDO} MATCHES "PV_FINDO-NOTFOUND")


set(USE_TACHYON OFF CACHE BOOL "use vmd tachyon renderer")
if(USE_TACHYON)
#
#tachyon (will update this to find the tachyon binary as above)
#
SET(TACHYONBIN ${TACHYONBIN} CACHE STRING "Tachyon renderer")
SET(TACHYONDATA ${TACHYONDATA} CACHE STRING "Tachyon datafile")
SET(TACHYONDATA_DIR ${TACHYONDATAi_DIR} CACHE STRING "Tachyon directorya")
endif()


# SET(SWR_LIB libGL.so.1 CACHE STRING "root SVB directory")
#
# set the accounting info. What account do I charge this to
#
set(SUBMIT_ACCOUNT A-ccvis CACHE STRING "account to charge to")
set(SUBMIT_PARTITION skx-normal CACHE STRING "Cluster partition")
#
# set the renderer and dataSources. Setting to ON includes the
# renderer or dataSource in the batch scripts collection.
#
SET(RENDER_BACKEND "")
set(ENABLE_BACKEND_SWR OFF CACHE BOOL "use swr renderer")
if(ENABLE_BACKEND_SWR)
	set(RENDER_BACKEND "${RENDER_BACKEND} swr")
endif()
set(ENABLE_BACKEND_LLVMPIPE OFF CACHE BOOL "use llvmpipe renderer")
if(ENABLE_BACKEND_LLVMPIPE)
	set(RENDER_BACKEND "${RENDER_BACKEND} llvmpipe")
endif()
set(ENABLE_BACKEND_MESA OFF CACHE BOOL "use llvmpipe renderer")
if(ENABLE_BACKEND_MESA)
	set(RENDER_BACKEND "${RENDER_BACKEND} mesa")
endif()
set(ENABLE_BACKEND_GPU OFF CACHE BOOL "use gpu renderer")
if(ENABLE_BACKEND_GPU)
	set(RENDER_BACKEND "${RENDER_BACKEND} gpu")
endif()
set(ENABLE_BACKEND_GPU2 OFF CACHE BOOL "use gpu opengl2 renderer")
if(ENABLE_BACKEND_GPU2)
	set(RENDER_BACKEND "${RENDER_BACKEND} gpu2")
endif()
set(IMMEDIATEMODE OFF CACHE BOOL "use immediatemode for gpu renderer")
set(ENABLE_BACKEND_GLURAY OFF CACHE BOOL "use gluray renderer")
if(ENABLE_BACKEND_GLURAY)
	set(RENDER_BACKEND "${RENDER_BACKEND} gluray")
	find_file(GLURAY_FIND NAMES gluray)
	if(${GLURAY_FIND} MATCHES "GLURAY_FIND-NOTFOUND")
		MESSAGE(WARNING "Gluray not found " )
	endif(${GLURAY_FIND} MATCHES "GLURAY_FIND-NOTFOUND")
	SET(GLuRay_PATH ${GLURAY_FIND} CACHE STRING "root SVB directory")
endif()
set(ENABLE_BACKEND_VBO OFF CACHE BOOL "use vbo renderer")
if(ENABLE_BACKEND_VBO)
	set(RENDER_BACKEND "${RENDER_BACKEND} vbo")
endif()
set(ENABLE_BACKEND_OSPRAY OFF CACHE BOOL "use ospray renderer")
if(ENABLE_BACKEND_OSPRAY)
	set(RENDER_BACKEND "${RENDER_BACKEND} ospray")
	set(ENABLE_BACKEND_OSPRAYAO OFF CACHE BOOL "use ospray renderer with ao")
endif()
set(ENABLE_BACKEND_SWRVBO OFF CACHE BOOL "use swrvbo renderer")
if(ENABLE_BACKEND_SWRVBO)
	set(RENDER_BACKEND "${RENDER_BACKEND} swrvbo")
endif()

#temp hide some backends
mark_as_advanced(ENABLE_BACKEND_GLURAY)
mark_as_advanced(ENABLE_BACKEND_GPU) #TODO: Hide this only if the cluster does not have gpus
mark_as_advanced(ENABLE_BACKEND_GPU2)  #TODO: Hide this only if the cluster does not have gpus

SET(DATASETS "")

# DATA
set(USE_FIU OFF CACHE BOOL "run fiu data")
if(USE_FIU)
	SET(DATASETS "${DATASETS} fiu")
	set(USE_FIU_ANIMATED OFF CACHE BOOL "run fiu animated data")
	if(USE_FIU_ANIMATED)
		SET(DATASETS "${DATASETS} fiu_animated")
	ENDIF()
	find_file(FIUDATA_DIR NAMES rho_380x380x828_frame0010.nhdr PATHS ${SVB_DATA_DIR})
	if(${FIUDATA_DIR} MATCHES "FIUDATA_DIR-NOTFOUND")
		set(FIUDATA_DIR ${SVB_DATA_DIR} CACHE PATH "FIU data directory")
		MESSAGE(WARNING "FIU data not found " )
	endif()
	set(FIUDATA_DIR ${FIUDATAD_DIR} CACHE PATH "FIU data directory")
endif()


set(USE_RM OFF CACHE BOOL "run the rm data")
if(USE_RM)
	SET(DATASETS "${DATASETS} rm")
	set(USE_RM_TIME OFF CACHE BOOL "run the rm time series data")
	IF(USE_RM_TIME)
		SET(DATASETS "${DATASETS} rm_time")
	ENDIF()
	set(USE_RM_ISOSWEEP OFF CACHE BOOL "run the rm isosweep data")
	IF(USE_RM_ISOSWEEP)
		SET(DATASETS "${DATASETS} rm_isosweep")
	ENDIF()
	set(USE_RM_CLIPSWEEP OFF CACHE BOOL "run the dns isosweep data")
	IF(USE_RM_CLIPSWEEP)
		SET(DATASETS "${DATASETS} rm_clipsweep")
	ENDIF()
	find_file(RMDATA_DIR NAMES ppmt273_256_256_256.nrrd PATHS ${SVB_DATA_DIR})
	if(${RMDATA_DIR} MATCHES "RMDATA_DIR-NOTFOUND")
		set(RMDATA_DIR ${SVB_DATA_DIR} CACHE PATH "RM data directory")
		MESSAGE(WARNING "RM data not found " )
	endif()
	set(RMDATA_DIR ${RMDATAD_DIR} CACHE PATH "RM data directory")
endif()

set(USE_TURBULENCE OFF CACHE BOOL "run the turbulence data")
if(USE_TURBULENCE)
	SET(DATASETS "${DATASETS} turbulence")
	set(TURBULENCEDATA_DIR "TURBULENCEDATA_DIR-NOTFOUND" CACHE PATH "turbulence data directory")
endif()


set(USE_DNS OFF CACHE BOOL "run the dns data")
if(USE_DNS)
	SET(DATASETS "${DATASETS} dns")
	set(USE_DNS_CLIPSWEEP OFF CACHE BOOL "run the dns clipsweep data")
	IF(USE_DNS_CLIPSWEEP)
		SET(DATASETS "${DATASETS} dns_clipsweep")
	ENDIF()
	set(USE_DNS_ISOSWEEP OFF CACHE BOOL "run the dns isosweep data")
	IF(USE_DNS_ISOSWEEP)
		SET(DATASETS "${DATASETS} dns_isosweep")
	ENDIF()
	find_file(DNSDATA_DIR NAMES u_1024_pv.xmf PATHS ${SVB_DATA_DIR})
	if(${DNSDATA_DIR} MATCHES "DNSDATA_DIR-NOTFOUND")
		set(DNSDATA_DIR ${SVB_DATA_DIR} CACHE PATH "DNS data directory")
		MESSAGE(WARNING "DNS data not found " )
	endif()
	set(DNSDATA_DIR ${DNSDATA_DIR} CACHE PATH "DNS data directory")
endif()

set(USE_MOLECULE OFF CACHE BOOL "run the pv molecule data")
if(USE_MOLECULE)
	SET(DATASETS "${DATASETS} molecule")
	find_file(MOLDATA_DIR NAMES 1VRI.pdb PATHS ${SVB_DATA_DIR})
	if(${MOLDATA_DIR} MATCHES "MOLDATA_DIR-NOTFOUND")
		set(MOLDATA_DIR ${SVB_DATA_DIR} CACHE PATH "molecular data directory")
		MESSAGE(WARNING "molecule data not found " )
	endif()
	set(MOLDATA_DIR ${MOLDATA_DIR} CACHE PATH "molecular data directory")
endif()


set(USE_GEO OFF CACHE BOOL "run the geo data")
if (USE_GEO)
	SET(DATASETS "${DATASETS} geo")
	find_file(GEODATA_DIR NAMES Top_Albian.obj PATHS ${SVB_DATA_DIR})
	if(${GEODATA_DIR} MATCHES "GEODATA_DIR-NOTFOUND")
		set(GEODATA_DIR ${SVB_DATA_DIR} CACHE PATH "geo data directory")
		MESSAGE(WARNING "geo data not found " )
	endif()
	set(GEODATA_DIR ${GEODATA_DIR} CACHE PATH "geo data directory")
endif (USE_GEO)


set(USE_WRF OFF CACHE BOOL "run the wrf data")
if(USE_WRF)
	#
	#wrf plugin
	#
	SET(WRF_PLUGIN_PATH ${WRF_PLUGIN_PATH} CACHE STRING "WRF PLUGIN")
	SET(DATASETS "${DATASETS} wrf")
	find_file(WRFDATA_DIR NAMES wrfout_d01_2010-06-23_23:00:00.wrf PATHS ${SVB_DATA_DIR})
	if(${WRFDATA_DIR} MATCHES "WRFDATA-NOTFOUND")
		set(WRFDATA_DIR ${SVB_DATA_DIR} CACHE PATH "WRF data directory")
		MESSAGE(WARNING "WRF data not found " )
	endif(${WRFDATA} MATCHES "WRFDATA-NOTFOUND")
	set(WRFDATA_DIR ${WRFDATA_DIR} CACHE PATH "WRF data directory")
endif()

set(USE_WHIPPLE OFF CACHE BOOL "run whipple shield data")
if(USE_WHIPPLE)
	SET(DATASETS "${DATASETS} whipple")
	set(USE_WHIPPLE_TIME OFF CACHE BOOL "run the whipple shield time series data")
	find_file(WHIPPLEDATA_DIR NAMES Whipple_Shield.exo.300.000 PATHS ${SVB_DATA_DIR})
	if(${WHIPPLEDATA_DIR} MATCHES "WHIPPLEDATA-NOTFOUND")
		set(WHIPPLEDATA_DIR ${SVB_DATA_DIR} CACHE PATH "WHIPPLE data directory")
		MESSAGE(WARNING "WHIPPLE data not found " )
	endif(${WHIPPLEDATA} MATCHES "WHIPPLEDATA-NOTFOUND")
	set(WHIPPLEDATA_DIR ${WHIPPLEDATA_DIR} CACHE PATH "WHIPPLE data directory")
endif(USE_WHIPPLE)

set(USE_ENZO OFF CACHE BOOL "run enzo data")
if(USE_ENZO)
	SET(DATASETS "${DATASETS} enzo")
	find_file(ENZODATA_DIR NAMES DD0174.cpu0000 PATHS ${SVB_DATA_DIR})
	if(${ENZODATA_DIR} MATCHES "ENZODATA-NOTFOUND")
		set(ENZODATA_DIR ${SVB_DATA_DIR} CACHE PATH "ENZO data directory")
		MESSAGE(WARNING "ENZO data not found " )
	endif(${ENZODATA} MATCHES "ENZODATA-NOTFOUND")
	set(ENZODATA_DIR ${SVB_DATA_DIR} CACHE PATH "ENZO data directory")
endif()
#OTHER OPTIONS

# set(ENZODATA_DIR "TURBULENCEDATA_DIR-NOTFOUND" CACHE PATH "turbulence data directory")

#
# set how mpi programs are launched. default is ibrun
# Note: mpirun and ibrun should be in your path or this wont work.
#
if(NOT MPI_COMMAND)
	set(MPI_COMMAND "ibrun" CACHE STRING "Command used to launch mpi jobs: ibrun, mpirun")
endif(NOT MPI_COMMAND)
set(MPI_LAUNCH_X ON CACHE BOOL "Job must launch X server")
if(MPI_LAUNCH_X)
	set(MPI_X_PROLOGUE "${SVB_DIR}/X/mpi_x_prologue" CACHE FILE "Prologue script to start X")
	set(MPI_X_EPILOGUE "${SVB_DIR}/X/mpi_x_epilogue" CACHE FILE "Epilogue to close X")
endif()
set(MPI_ENV_COMMAND "module load remora swr ospray qt5 paraview-osmesa/5.4.1" CACHE STRING "Command used to settup env for each run, ie DISPLAY=:0.0")
#
# if mpi uses mpirun look for a hostfile, set the ranks per node. -hostfile  <hosts >  -perhost <ranks-per-host>
# look in the directory where this file is for the hosts file used with mpi
#
if(${MPI_COMMAND} MATCHES "mpirun")
	set(RANKS_PER_HOST "1" CACHE STRING "number of mpi ranks to start per node")
endif(${MPI_COMMAND} MATCHES "mpirun")

set(MaxNumNodes "32" CACHE STRING "The max number of nodes to use")
set(MaxNumProcs "16" CACHE STRING "The max number of mpi processes per nodes to use")
set(MaxGeometryLevels "3" CACHE STRING "The geometry levels to use, ie 1 2 4 8.  Up to 10.  Dataset script specific.")

set (index 0)
math(EXPR nodes "1")
set (NumNodes "")
while( (MaxNumNodes GREATER ${nodes}) OR (MaxNumNodes EQUAL ${nodes}) )
	set(NumNodes "${NumNodes} ${nodes}")
	math(EXPR index "${index}+1")
	math(EXPR nodes "1 << ${index}")
endwhile()

set (index 0)
set (NumProcs "")
math(EXPR nodes "1")
while( (MaxNumProcs GREATER ${nodes}) OR (MaxNumProcs EQUAL ${nodes}) )
	set(NumProcs "${NumProcs} ${nodes}")
	math(EXPR index "${index}+1")
	math(EXPR nodes "1 << ${index}")
endwhile()
set (index 0)
set (GeometryLevels "")
while( (MaxGeometryLevels GREATER ${index}) OR (MaxGeometryLevels EQUAL ${index}) )
	set(GeometryLevels "${GeometryLevels} ${index}")
	math(EXPR index "${index}+1")
endwhile()

#SET(PND \# CACHE INTERNAL STRING )
#FILE(REMOVE ${SVB_DIR}/paths.sh)
FILE(WRITE ${SVB_DIR}/paths.sh
	"${PND}!/bin/bash"  \n
	"################## BASE CONFIG #######################" \n
	"SVB_DIR=" ${SVB_DIR}  \n
	"output_DIR=" ${SVB_OUTPUT_DIR}  \n
	"data_DIR=" ${SVB_DATA_DIR}  \n
	"GENERATE_IMAGES=" ${GENERATE_IMAGES} \n
	"ROOT_IMAGE_DIR=" ${SVB_IMAGE_DIR} \n
	"RENDER_BACKEND=" ${RENDER_BACKEND} \n
	"DATASETS=" ${DATASETS} \n
	"NUMRUNS="${SVB_NUMBER_OF_RUNS} \n
	"################## PARAVIEW CONFIG #######################" \n
	"ParaView_DIR=" ${ParaView_DIR}  \n
	"ParaViewGL2_DIR=" ${ParaViewGL2_DIR}  \n
	"pvOSPRay_DIR=" ${pvOSPRay_DIR}  \n
	"pvVBO_DIR=" ${pvVBO_DIR}  \n
	"GLuRay_PATH=" ${GLuRay_PATH}  \n
	"WRF_PLUGIN_PATH=" ${WRF_PLUGIN_PATH} \n
	"################## MPI CONFIG #######################" \n
	"ACCOUNT=" ${SUBMIT_ACCOUNT} \n
	"PARTITION=" ${SUBMIT_PARTITION} \n
	"MPI_COMMAND=" ${MPI_COMMAND} \n
	"MPI_ENV_COMMAND=" ${MPI_ENV_COMMAND} \n
	"MPI_LAUNCH_X=" ${MPI_LAUNCH_X} \n
	"MPI_X_PROLOGUE=" ${MPI_X_PROLOGUE} \n
	"MPI_X_EPILOGUE=" ${MPI_X_EPILOGUE} \n
	"NumNodes="${NumNodes}\n
	"NumProcs="${NumProcs}\n
	"GeometryLevels="${GeometryLevels}\n
	"################## renderer CONFIG #######################" \n
	"ENABLE_BACKEND_SWR=" ${ENABLE_BACKEND_SWR} \n
	"ENABLE_BACKEND_GPU=" ${ENABLE_BACKEND_GPU} \n
	"ENABLE_BACKEND_GPU2=" ${ENABLE_BACKEND_GPU} \n
	"ENABLE_BACKEND_GLURAY=" ${ENABLE_BACKEND_GLURAY} \n
	"ENABLE_BACKEND_VBO=" ${ENABLE_BACKEND_VBO} \n
	"ENABLE_BACKEND_OSPRAY=" ${ENABLE_BACKEND_OSPRAY} \n
	"ENABLE_BACKEND_OSPRAYAO=" ${ENABLE_BACKEND_OSPRAYAO} \n
	"ENABLE_BACKEND_SWRVBO=" ${ENABLE_BACKEND_SWRVBO} \n
	"IMMEDIATEMODE=" ${IMMEDIATEMODE} \n
	"################## FIU CONFIG #######################" \n
	"USE_FIU=" ${USE_FIU} \n
	"USE_FIU_ANIMATED=" ${USE_FIU_ANIMATED} \n
	"FIUDATA_DIR=" ${FIUDATA_DIR} \n
	"################## RM CONFIG #######################" \n
	"USE_RM=" ${USE_RM} \n
	"RMDATA_DIR=" ${RMDATA_DIR} \n
	"USE_RM_TIME=" ${USE_RM_TIME} \n
	"USE_RM_ISOSWEEP="  ${USE_RM_ISOSWEEP} \n
	"USE_RM_CLIPSWEEP="  ${USE_RM_CLIPSWEEP} \n
	"################## TURBULENCE CONFIG #######################" \n
	"USE_TURBULENCE="  ${USE_TURBULENCE} \n
	"TURBULENCEDATA_DIR=" ${TURBULENCEDATA_DIR} \n
	"################## DNS CONFIG #######################" \n
	"USE_DNS=" ${USE_DNS} \n
	"DNSDATA_DIR=" ${DNSDATA_DIR} \n
	"USE_DNS_ISOSWEEP=" ${USE_DNS_ISOSWEEP} \n
	"USE_DNS_CLIPSWEEP=" ${USE_DNS_CLIPSWEEP} \n
	"################## GEO CONFIG #######################" \n
	"USE_GEO=" ${USE_GEO} \n
	"GEODATA_DIR=" ${GEODATA_DIR} \n
	"################## WRF CONFIG #######################" \n
	"USE_WRF=" ${USE_WRF} \n
	"WRFDATA_DIR=" ${WRFDATA_DIR} \n
	"################## WHIPPLE CONFIG #######################" \n
	"USE_WHIPPLE=" ${USE_WHIPPLE} \n
	"USE_WHIPPLE_TIME=" ${USE_WHIPPLE_TIME} \n
	"WHIPPLEDATA_DIR=" ${WHIPPLEDATA_DIR} \n
	"################## ENZO CONFIG #######################" \n
	"ENZODATA_DIR=" ${ENZODATA_DIR} \n
	"################## MOL CONFIG #######################" \n
	"USE_MOLECULE=" ${USE_MOLECULE} \n
	"MOLDATA_DIR=" ${MOLDATA_DIR} \n
	"################## FIU CONFIG #######################" \n
	"USE_TACHYON=" ${USE_TACHYON} \n
	"TACHYONBIN=" ${TACHYONBIN} \n
	"TACHYONDATA=" ${TACHYONDATA} \n
	"TACHYONDATA_DIR=" ${TACHYONDATA_DIR} \n
)
