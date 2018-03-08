#!/usr/bin/python

# import headers
from paraview.simple import *

import os
import resource
import argparse
'''
from optparse import OptionParser

import time
import math
import sys 
'''

# Disable the first render camera reset.  Normally a ResetCamera is called
# automatically when Render is called for the first time after importing
# this module.
paraview.simple._DisableFirstRenderCameraReset()

# path to pv_scripts folder. Used to append files to systems path to import.
pv_scripts_folder = os.getcwd() + '/pv_scripts'

print 'pv_scripts folder path: {}'.format( pv_scripts_folder )

# append pv_scripts path to systems path
sys.path.append( pv_scripts_folder )

# import benchmark from pv_scripts
import benchmark

benchmark.maximize_logs()

# function to print out memory usage information
def PrintMemoryUsage():

   result = resource.getrusage( resource.RUSAGE_SELF ).ru_maxrss
   
   print 'Memory: ' + str( float( result ) / float( 1024 * 1024 ) ) + 'GB\n'
   print 'Page size: ' + str( resource.getpagesize() ) + '\n'

# function that tests the time it takes to create the 
# first 3 frames to render
def WarmupRender():

    print '#'
    print 'Warmup...'
    print '#'

    for i in range(0,3):

      if (i == 0):

        print 'time to first frame: ' + str( time.time() - start_time )

      warmup_st = time.time()

      print 'rendering warmup frame'

      svbRender()

      warmup_et = time.time()
      warmup_tt = ( warmup_et - warmup_st )

      print 'warmup frame Render: ' + str( warmup_tt )

# argument parser for command line arguments
parser = argparse.ArgumentParser()

# OSPRay argument
parser.add_option( '--osp', 
                   action = 'store_true', 
                   help = 'Use OSPRay (default is false)' )

# SWR argument
parser.add_option( '--swr', 
                   action = 'store_true', 
                   help = 'Use SWR (default is false)' )

# save images argument
parser.add_option( '-i', 
                   '--save_images', 
                   type ='string', 
                   default='', 
                   help= 'Save\'s images to <string> when set')
