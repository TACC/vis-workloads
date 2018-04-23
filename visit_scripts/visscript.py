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

import visit
import os
import sys
#launchArguments = ("-par", "-np", "32","-l","ibrun")
launchArguments = ("-par","-np","1","-nn","1","-p","vis","-la","-V -cwd", "-l", "ibrun","-t","60")#,"-machinefile","longhorn")
batchHost = "localhost"
OpenComputeEngine("%s"%batchHost,launchArguments)
Source("/scratch/01336/carson/intelTACC/benchmarks/visit_scripts/visit_run.py")
