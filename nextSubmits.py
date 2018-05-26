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
#
#   SVBench: Scientific Visualization Benchmarking Suite is funded in part by an Intel Cooperation award
#   ======================================================================================= */


import os
import stat
import argparse
import sys
import fnmatch
import subprocess

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

# argument parser for command line arguments
parser = argparse.ArgumentParser()

# System queue/partition name
parser.add_argument( '-l',
                     '--limit',
                     default=3,
                     help = 'Max number processes to submit',
                     type = int )

# System queue/partition name
parser.add_argument( '-r',
                     '--reset',
                     default=False,
                     help = 'run x server (default is true)',
                     action = 'store_true' )
parser.add_argument( '-R',
                     '--reservation',
                     default='none',
                     help = 'run x server (default is true)',
                     action = 'store' )

# parse arguments passed through command-line
args = parser.parse_args()

reservation = args.reservation;

submission_limit = args.limit;
start_submission = 0;
end_submission = submission_limit;
total_submits = -1;

if( (not args.reset) and (os.path.exists('submit_range.txt'))):
    with open('submit_range.txt','r') as f:
        start_submission, end_submission, submission_limit, total_submits = [int(x) for x in next(f).split()]

print("Submit queue linit: {}".format(submission_limit))
print("Start submit : {}".format(start_submission))
print("End submit : {}".format(end_submission))

if(start_submission == end_submission and start_submission != 0):
    print("All jobs submitted")
    exit()

matches = []
for root, dirnames, filenames in os.walk(path_vars['output_DIR']):
    for filename in fnmatch.filter(filenames, 'submit_*.sh'):
        matches.append(os.path.join(root, filename))

if(total_submits !=-1 and total_submits != len(matches)):
        print("Number of submission script to execute changed")
        print("Maube you should rerun all by using the option -r/--reset")
        parser.print_help()
        exit()

end_submission = min(end_submission,len(matches))

sub_reservation = ""
if(reservation != "none"):
    sub_reservation = "--reservation {} ".format(reservation)


for i in range(start_submission,end_submission):
    print("Submitting : {}".format(matches[i]))

    print("sbatch {}{}".format(sub_reservation,matches[i]))
    p = subprocess.Popen("sbatch {}{}".format(sub_reservation,matches[i]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if(len(stdout) > 0):
        print("Out: {}".format(stdout))
    if(len(stderr) > 0):
        print("Err: {}".format(stderr))
        exit()

    #result_call = os.popen(.read()

if( len(matches) <= submission_limit):
    exit()

start_submission = min(start_submission+submission_limit,len(matches))
end_submission = min(end_submission+submission_limit,len(matches))

with open('submit_range.txt','w') as f:
    f.write('{} {} {} {}'.format(start_submission,end_submission,submission_limit,len(matches)))

print("Total scripts to submit : {}".format(len(matches)))
print("Remaining scripts to submit : {}".format(len(matches)-start_submission))
