#!/usr/bin/python

# import headers
import os
import stat
import argparse
import sys

#read in paths from the environment variables bash script generate by cmake
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pathsfile = os.path.join(dir,'paths.sh')
path_vars = dict()
with open(pathsfile) as f:
    for line in f:
        eq_index = line.find('=')
        var_name = line[:eq_index].strip()
        paths = line[eq_index + 1:].strip()
        path_vars[var_name] = paths

# geo_data_dir =  path_vars["GEODATA_DIR"]
# print "geo_data_dir:%s" %  geo_data_dir

# specify output directory for benchmark bash scripts
output_directory = path_vars['output_DIR']
# specify output directory for images generated by bash scripts
image_directory  = path_vars['ROOT_IMAGE_DIR']
# string of path to pv_bench.py
pv_bench_path = os.path.join(path_vars['SVB_DIR'], 'pv_bench.py')

# string of image settings to pass to bash script if user
# decides to generate images
image_arguments = ''

# array of different triangle counts to try for different tests
triangles_count = path_vars['GeometryLevels'].split()
# array of different node counts to try for different tests
nodes_count     = path_vars['NumNodes'].split()
# array of different process counts to try for different tests
processes_count = path_vars['NumProcs'].split()

# define which renderer to use for the tests
renderer = ''
# plugin flag sent through ibrun command based
# off which renderer is used
global pv_plugin_flag

# name of dataset used for tests
data_name = ''

# account name to use for submitting tests as jobs
account_name = path_vars['ACCOUNT']
# queue to submit jobs
queue_name   = path_vars['PARTITION']

# number of runs to perform for each job
num_runs = int(path_vars['NUMRUNS'])

# pre-arguments flag
global pre_args

# swr command to pass if using swr
# workaround where swr_cmd is not defined if global
# is not prepended since it is looking for a local scope in the
# process_benchmark function
global swr_cmd

# argument parser for command line arguments
parser = argparse.ArgumentParser()

# System queue/partition name
parser.add_argument( '-a',
                     '--account',
                     default=account_name,
                     help = 'Accounting Project',
                     type = str )

# System queue/partition name
parser.add_argument( '-p',
                     '--partition',
                     default=queue_name,
                     help = 'Queue/Partition to submit',
                     type = str )

# output directory argument
parser.add_argument( '-od',
                     '--output_directory',
                     default=output_directory,
                     help = 'set the output directory for the batch file (default is a directory named \"benchmarks\" located in the current directory location of this script)',
                     type = str )

# renderer argument
parser.add_argument( '-r',
                     '--renderer',
                     default = 'swr',
                     help = 'set renderer for tests (default is swr)',
                     type = str,
                     choices = path_vars['RENDER_BACKEND'].split())

# save images argument
parser.add_argument( '-si',
                     '--save_images',
                     help = 'set if you like to save the images from the batch jobs (default is false)',
                     action = 'store_true')

# image directory argument
parser.add_argument( '-id',
                     '--image_directory',
                     default = path_vars['ROOT_IMAGE_DIR'],
                     help = 'set the output directory for images generated (default is a directory names \"images\" located in the current directory location of this script)',
                     type = str )

# data argument
parser.add_argument( '-d',
                     '--data',
                     default = 'fiu',
                     help = 'define the data to be used for the tests(default is fiu)',
                     choices = path_vars['DATASETS'].split(),
                     type = str  )

# x server argument
parser.add_argument( '-x',
                     '--x_server',
                     default=False,
                     help = 'run x server (default is true)',
                     action = 'store_true' )

# parse arguments passed through command-line
args = parser.parse_args()

# set variables based off passed in command line arguments
print( 'setting queue to {}'.format( args.partition ) )
queue_name =  args.partition;

print( 'setting Account Name to {}'.format( args.account ) )
account_name =  args.account;

print( 'setting output directory to {}'.format( args.output_directory ) )
output_directory = args.output_directory

print( 'setting renderer to {}'.format( args.renderer ) )
renderer = args.renderer

print( 'data: {}'.format( args.data ) )
data_name = args.data

print( 'save images? : {}'.format( args.save_images ) )
save_images = args.save_images

print( 'run X server? : {}'.format( args.x_server ) )
x_server = args.x_server

# if the bencmark directory does not exist, then create
# it and its associated folders
if not os.path.exists(output_directory):
    os.makedirs( output_directory )


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
def process_benchmark(triangle, node, process ):

    subfolder = os.path.join(data_name,renderer)

    outputdir = os.path.join(output_directory,os.path.join(subfolder,"outs"))
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    submitsdir = os.path.join(output_directory,os.path.join(subfolder,"submits"))
    if not os.path.exists(submitsdir):
        os.makedirs(submitsdir)

    interactivedir = os.path.join(output_directory,os.path.join(subfolder,"interactive"))
    if not os.path.exists(interactivedir):
        os.makedirs(interactivedir)

                # workaround for now
    swr_cmd = ''
    pv_plugin_flag = ''
    pre_args = ''

    # name of job to be used in bash script and file name
    job_name = 'd{0}_r{1}_t{2}_N{3}_n{4}'.format( data_name, renderer, triangle, node, process )
    # file name for bash job
    file_name = 'submit_' + job_name + '.sh'
    # path to output file for bash job
    output_name = os.path.join(outputdir,"{}.out".format(job_name))
    # create and open bash file
    file_obj = open(os.path.join(submitsdir,file_name), 'w' )

    # write the appropriate header information
    file_obj.write( '#!/bin/bash\n' )
    file_obj.write( '#SBATCH -J {}\n'.format( job_name ) )
    file_obj.write( '#SBATCH -N {}\n'.format( node ) )
    file_obj.write( '#SBATCH -n {}\n'.format( int(node) * int(process) ) )
    file_obj.write( '#SBATCH -p {}\n'.format( queue_name ) )
    file_obj.write( '#SBATCH -A {}\n'.format( account_name ) )
    file_obj.write( '#SBATCH -o {}\n'.format( output_name ) )
    file_obj.write( '#SBATCH -t {}\n\n'.format( '02:00:00' ) )

    # file_obj.write( 'set -x\n' )
    file_obj.write( 'date\n\n' )

    # write default modules to load for bash file
    #file_obj.write( 'module load remora\n' )
    #file_obj.write( 'module use /work/01206/jbarbosa/stampede2/rpminstall/modulefiles\n' )
    #file_obj.write( 'module load swr\n' )
    #file_obj.write( 'module load qt5\n' )
    #file_obj.write( 'module load paraview-omesa\n\n' )
    file_obj.write(path_vars['MPI_ENV_COMMAND'])

    # set LD_LIBRARY_PATH and REMORA_PERIOD
    # file_obj.write( 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$TACC_PARAVIEW_LIB\n' )
    file_obj.write( '\nREMORA_PERIOD=1\n\n' )

    threads_pp = 48 / int(process)
    # set parameters based off renderer
    if renderer == 'swr':

        # file_obj.write( 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$TACC_SWR_LIB\n\n' )

        # if x server is not set, then set display environment variable
        if not x_server:

            pre_args = 'DISPLAY=:1.0'

        swr_cmd  = 'swr -t {}'.format( threads_pp )
        pv_plugin_flag = '--swr'

    elif renderer == 'llvmpipe':

        # file_obj.write( 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$TACC_SWR_LIB\n\n' )

        # if x server is not set, then set display environment variable
        if not x_server:

            pre_args = 'DISPLAY=:1.0'

        swr_cmd  = '{}/llvmpipe -t {}'.format( os.path.join(os.path.join(path_vars['SVB_DIR'],"scritps"),"llvmpipe"), threads_pp  )
        pv_plugin_flag = '--swr'

    elif renderer == 'ospray':

        file_obj.write( 'module load ospray\n\n' )
        pre_args = 'remora'
        pv_plugin_flag = '--osp'

    # append x server code to bath file
    if x_server:
        x_file = open( path_vars['MPI_X_PROLOGUE'], 'r' )
        x_file_data = x_file.read()
        x_file.close()
        file_obj.write( x_file_data + '\n' )

    # write out command to file to execute test
    file_obj.write( '{} ibrun -n {} -o 0 {} pvbatch {} {} -w 1024x1024 {} --geoLevel {} --numruns {} --source {} \n\n'.format( pre_args, (int(node) * int(process)), swr_cmd, pv_bench_path , pv_plugin_flag, image_arguments, triangle, num_runs, data_name ) )
    file_obj.write( 'date\n\n' )

    # if server is running, be sure to print out commands to kill vnc server
    if x_server:
        x_file = open(path_vars['MPI_X_EPILOGUE'], 'r' )
        x_file_data = x_file.read()
        x_file.close()
        file_obj.write( x_file_data + '\n' )

    file_obj.close()

    # change permissions of bash file
    os.chmod(os.path.join(submitsdir,file_name), stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | stat.S_IWUSR | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH )

# iterate through different triangles, nodes, and processes
# to generate their corresponding bash script by passing
# the parameters to process_benchmark

for triangle in triangles_count:
    for node in nodes_count:
        for process in processes_count:
            process_benchmark( triangle, node, process )
