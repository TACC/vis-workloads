#!/bin/bash 
#SBATCH -J drm_rgluray_t1_n4 
#SBATCH -N 4
#SBATCH -n 4 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/drm_rgluray_t1_n4.out
#SBATCH -t 04:00:00
set -x
date
module load qt
module load paraview/4.1.0
module use /work/01336/carson/opt/modulefiles
DISPLAY=:0.0 ibrun -n 4 -o 0    /opt/apps/intel14/mvapich2_2_0/paraview/4.1.0/bin/pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py   -w 1920x1080   --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 1 --numruns 10 --source rm --immediatemode 
date