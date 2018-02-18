#!/usr/bin/python

# import headers
import os
import stat

# specify output directory for benchmark bash scripts
output_directory = '/home1/02064/ajs2987/benchmarks'
# specify output directory for images generated by bash scripts
image_directory  = '/home1/02064/ajs2987/images'

# flag to turn on/off images generated from bash scripts
generate_images = True

# string of image settings to pass to bash script if user 
# decides to generate images
image_flag = ''

# array of different triangle counts to try for different tests
triangles_count = [ 0, 1, 2, 3         ]
# array of different node counts to try for different tests
nodes_count     = [ 1, 2, 4, 8, 16, 32 ]
# array of different process counts to try for different tests
processes_count = [ 1, 8, 16           ]

# define which renderer to use for the tests
# (only using swr for now)
renderer = 'swr'

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

# if the bencmark directory does not exist, then create
# it and its associated folders
if not os.path.exists(output_directory):

    os.makedirs( output_directory )
    os.makedirs( output_directory + '/outs'        )
    os.makedirs( output_directory + '/submits'     )
    os.makedirs( output_directory + '/interactive' )

# if you choose to generate images and the image directory does
# not exist, then create it
if generate_images and not os.path.exists(image_directory):
    os.makedirs( image_directory )

# if generate images is set to true then set the image flag
# string to the correct parameters
if generate_images:
    image_flag = '--save_images -i {}/'.format( image_directory )

# main function used to process information to create bash 
# benchmark script
def process_benchmark( triangle, node, process ):
    
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
    file_obj.write( '#SBATCH -t {}\n'.format( '04:00:00' ) )
    file_obj.write( 'set -x\n\n' )

    # write default modules to load for bash file
    file_obj.write( 'module load remora\n' )
    file_obj.write( 'module load swr\n' )
    file_obj.write( 'module load qt5\n' )
    file_obj.write( 'module load paraview\n' )
    
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


