#!/usr/bin/python

# import headers
import os
import stat
import argparse

# specify output directory for benchmark bash scripts
output_directory = ''
# specify output directory for images generated by bash scripts
image_directory  = ''
# string path of current directory
current_directory = os.getcwd()
# string of path to pv_bench.py
pv_bench_path = current_directory + '/pv_bench.py'

# string of image settings to pass to bash script if user 
# decides to generate images
image_arguments = ''

# array of different triangle counts to try for different tests
triangles_count = [ 0, 1, 2, 3         ]
# array of different node counts to try for different tests
nodes_count     = [ 1, 2, 4, 8, 16, 32 ]
# array of different process counts to try for different tests
processes_count = [ 1, 8, 16           ]

# define which renderer to use for the tests
renderer = ''
# plugin flag sent through ibrun command based
# off which renderer is used
pv_plugin_flag = '--swr'

# path to data directory
# (using fiu for now)
data_path = '/work/00401/pnav/workloads/fiu'
# name of dataset used for tests
# (using fiu for now)
data_name = 'fiu'

# account name to use for submitting tests as jobs
account_name = 'A-ccvis'
# queue to submit jobs
queue_name   = 'normal'

# number of runs to perform for each job
num_runs = 10

# pre-arguments flag
pre_args = ''

# swr command to pass if using swr
# workaround where swr_cmd is not defined if global
# is not prepended since it is looking for a local scope in the
# process_benchmark function
global swr_cmd

# argument parser for command line arguments
parser = argparse.ArgumentParser()

# output directory argument
parser.add_argument( '-od', '--output_directory', default=os.getcwd() + '/benchmarks', help='set the output directory for the batch file (default is a directory named \"benchmarks\" located in the current directory location of this script)', type = str )
# renderer argument
parser.add_argument( '-r', '--renderer', default = 'swr', help = 'set renderer for tests (default is swr)', type = str, choices = [ 'swr', 'llvmpipe', 'ospray' ] )
# save images argument
parser.add_argument( '-si', '--save_images', help = 'set if you like to save the images from the batch jobs (defaults to false)', action = 'store_true')
# image directory argument
parser.add_argument( '-id', '--image_directory', default = os.getcwd() + '/images', help = 'set the output directory for images generated (default is a directory names \"images\" located in the current directory location of this script)', type = str )

# parse arguments passed through command-line
args = parser.parse_args()

# set variables based off passed in command line arguments
print( 'setting output directory to {0}'.format( args.output_directory ) )
output_directory = args.output_directory

print( 'setting renderer to {0}'.format( args.renderer ) )
renderer = args.renderer

print( 'save images? : {0}'.format( args.save_images ) )
save_images = args.save_images

# if the bencmark directory does not exist, then create
# it and its associated folders
if not os.path.exists(output_directory):

    os.makedirs( output_directory )

os.makedirs( output_directory + '/outs'        )
os.makedirs( output_directory + '/submits'     )
os.makedirs( output_directory + '/interactive' )

# if you choose to save images then create the images folder
# if it does not exist, and set image_arguments
if save_images:

    print( 'setting image output directory to {0}'.format( args.image_directory ) )
    image_directory = args.image_directory

    if not os.path.exists( image_directory ):

        os.makedirs( image_directory )

    image_arguments = '--save_images -i {}/'.format( image_directory )
    

# main function used to process information to create bash 
# benchmark script
def process_benchmark( triangle, node, process ):
   
    # workaround for now
    swr_cmd = ''
 
    # name of job to be used in bash script and file name
    job_name = 'd{0}_r{1}_t{2}_N{3}_n{4}'.format( data_name, renderer, triangle, node, process )
    # file name for bash job
    file_name = 'submit_' + job_name + '.sh'
    # path to output file for bash job
    output_name = '{0}/outs/{1}.out'.format(output_directory, job_name )

    # create and open bash file
    file_obj = open( output_directory + '/submits/' + file_name, 'w' )

    # write the appropriate header information
    file_obj.write( '#!/bin/bash\n' )
    file_obj.write( '#SBATCH -J {}\n'.format( job_name ) )
    file_obj.write( '#SBATCH -N {}\n'.format( node ) )
    file_obj.write( '#SBATCH -n {}\n'.format( node * process ) )
    file_obj.write( '#SBATCH -p {}\n'.format( queue_name ) )
    file_obj.write( '#SBATCH -A {}\n'.format( account_name ) )
    file_obj.write( '#SBATCH -o {}\n'.format( output_name ) )
    file_obj.write( '#SBATCH -t {}\n\n'.format( '04:00:00' ) )
    
    file_obj.write( 'set -x\n' )
    file_obj.write( 'date\n\n' )
    

    # write default modules to load for bash file
    file_obj.write( 'module load remora\n' )
    file_obj.write( 'module load swr\n' )
    file_obj.write( 'module load qt5\n' )
    file_obj.write( 'module load paraview\n\n' )
   
    # set LD_LIBRARY_PATH and REMORA_PERIOD 
    file_obj.write( 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$TACC_PARAVIEW_LIB\n' )
    file_obj.write( 'REMORA_PERIOD=1\n\n' )

    # set parameters based off renderer 
    if renderer == 'swr':

        file_obj.write( 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$TACC_SWR_LIB\n\n' )
        pre_args = 'DISPLAY=:1.0'
        swr_cmd  = 'swr'
        pv_plugin_flag = '--swr'
    
    elif renderer == 'llvmpipe':
        
        file_obj.write( 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$TACC_SWR_LIB\n\n' )
        pre_args = 'DISPLAY=:1.0'
        swr_cmd  = '{}/llvmpipe'.format( os.getcwd() )
        pv_plugin_flag = '--swr'

    elif renderer == 'ospray':

        file_obj.write( 'module load ospray\n\n' )
        pre_args = 'remora'
        pv_plugin_flag = '--osp'

    # write out command to file to execute test 
    file_obj.write( '{} ibrun -n {} -o 0 {} pvbatch {} {} -w 1024x1024 {} --geoLevel {} --numruns {} --source {} \n\n'.format( pre_args, node, swr_cmd, pv_bench_path , pv_plugin_flag, image_arguments, triangle, num_runs, data_name ) )

    file_obj.write( 'date\n' )

    file_obj.close()

    # change permissions of bash file
    os.chmod('{0}/submits/{1}'.format( output_directory, file_name ), stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | stat.S_IWUSR | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH )

# iterate through different triangles, nodes, and processes 
# to generate their corresponding bash script by passing
# the parameters to process_benchmark

for triangle in triangles_count:

    for node in nodes_count:

        for process in processes_count:

            process_benchmark( triangle, node, process )


