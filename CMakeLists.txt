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

SET(SVB_DIR ${PROJECT_SOURCE_DIR} CACHE STRING "root SVB directory")
SET(output_DIR ${PROJECT_SOURCE_DIR}/benchmarks CACHE STRING "root SVB directory")
find_file(PV_FINDO 
  NAMES pvbatch)
MESSAGE(${PV_FINDO})
get_filename_component(PV_FIND ${PV_FINDO} PATH)
MESSAGE(${PV_FIND})
SET(ParaView_DIR ${PV_FIND} CACHE STRING "root SVB directory")
SET(pvOSPRay_DIR ${PV_FIND}/../lib CACHE STRING "root SVB directory")
SET(pvVBO_DIR ${PV_FIND}/../lib CACHE STRING "root SVB directory")
find_file(GLURAY_FIND 
  NAMES gluray)
SET(GLuRay_PATH ${GLURAY_FIND} CACHE STRING "root SVB directory")
SET(SWR_LIB libGL.so.1 CACHE STRING "root SVB directory")

FILE(REMOVE ${PROJECT_BINARY_DIR}/paths.txt)
FILE(WRITE ${PROJECT_BINARY_DIR}/paths.txt
  "SVB_DIR "${SVB_DIR}\n
  "output_DIR "${output_DIR}\n
  "ParaView_DIR "${ParaView_DIR}\n
  "pvOSPRay_DIR "${pvOSPRay_DIR}\n
  "pvVBO_DIR "${pvVBO_DIR}\n
  "GLuRay_PATH "${GLuRay_PATH}\n
  "SWR_LIB "${SWR_LIB}\n
  )


