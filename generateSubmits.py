#!/usr/bin/python

import os
import stat

output_directory = '/home1/02064/ajs2987/benchmarks' 
image_directory  = '/home1/02064/ajs2987/images'

generate_images = True

image_flag = ''

triangles_count = [ 0, 1, 2, 3         ]
nodes_count     = [ 1, 2, 4, 8, 16, 32 ]
processes_count = [ 1, 8, 16           ]

renderer = 'swr'

data_path = '/work/00401/pnav/workloads/fiu'
data_name = 'fiu'

account_name = 'A-ccvis'
queue_name   = 'normal'

if not os.path.exists(output_directory):

    os.makedirs( output_directory )
    os.makedirs( output_directory + '/outs'        )
    os.makedirs( output_directory + '/submits'     )
    os.makedirs( output_directory + '/interactive' )

if generate_images and not os.path.exists(image_directory):
    os.makedirs( image_directory )


def process_benchmark( triangle, node, process ):
    
    job_name = 'd{0}_r{1}_t{2}_N{3}_n{4}'.format( data_name, renderer, triangle, node, process )
    file_name = 'submit_' + job_name + '.sh'
    output_name = '{0}/outs/{1}.out'.format(output_directory, job_name )

    file_obj = open( output_directory + '/submits/' + file_name, 'w' )

    file_obj.write( '#!/bin/bash' )
    file_obj.write( '#SBATCH -J {}\n'.format( job_name ) )
    file_obj.write( '#SBATCH -N {}\n'.format( node ) )
    file_obj.write( '#SBATCH -n {}\n'.format( node * process ) )
    file_obj.write( '#SBATCH -p {}\n'.format( queue_name ) )
    file_obj.write( '#SBATCH -A {}\n'.format( account_name ) )
    file_obj.write( '#SBATCH -o {}\n'.format( output_name ) )
    file_obj.write( '#SBATCH -t {}\n'.format( '04:00:00' ) )
    
    file_obj.close()

    os.chmod('{0}/submits/{1}'.format( output_directory, file_name ), stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH )
    os.chmod('{0}/submits/{1}'.format( output_directory, file_name ), stat.S_IWUSR                               )
    os.chmod('{0}/submits/{1}'.format( output_directory, file_name ), stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH )


for triangle in triangles_count:

    for node in nodes_count:

        for process in processes_count:

            process_benchmark( triangle, node, process )

