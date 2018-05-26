#!/usr/bin/python

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
#   SVBench: Scientific Visualization Benchmarking Suite is funded in part by an Intel Cooperation award
#   ======================================================================================= */


# import headers
import os
import stat
import argparse
import sys

#read in paths from the environment variables bash script generate by cmake
dir = os.path.dirname(os.path.abspath(__file__))
pathsfile = os.path.join(dir,'paths.sh')
path_vars = dict()

if(not os.path.exists(pathsfile)):
    print("Paths configuration file does not exist: {}".format(pathsfile))
    print("Please use the following command line to generate configuration file")
    print("")
    print(" mkdir build; ccmake ..")
    print("")
    exit()

with open(pathsfile) as f:
    for line in f:
        #print(line.rstrip())
        eq_index = line.find('=')
        var_name = line[:eq_index].strip()
        paths = line[eq_index + 1:].strip()
        path_vars[var_name] = paths

renders = path_vars['RENDER_BACKEND'].split()
datasets = path_vars['DATASETS'].split()

if(len(renders) ==0):
    print("Renderes are missing, please rerun ccmake to choose/configure renderes.")
    exit()


if(len(datasets) ==0):
    print("Datasets are missing, please rerun ccmake to choose/configure benchamark datasets.")
    exit()


x_parameter=""
if(path_vars['MPI_LAUNCH_X']=="ON"):
    x_parameter=" -x"

si_parameter=""
if(path_vars['GENERATE_IMAGES']=="ON"):
    x_parameter=" -si"



for render in renders:
    for dataset in datasets:
        os.system("python scripts/generate_dataset_submits.py -d {} -r {}{}".format(dataset,render,x_parameter))
