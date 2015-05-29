#!/bin/bash 
#SBATCH -J dfiu_rswr_t6_n2 
#SBATCH -N 2
#SBATCH -n 2 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/dfiu_rswr_t6_n2.out
#SBATCH -t 00:40:00
set -x
date
module load qt
module load paraview/4.1.0
tacc_xrun ibrun -n 2 -o 0  LD_PRELOAD=libGL.so.1  /opt/apps/intel14/mvapich2_2_0/paraview/4.1.0/bin/pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py   -w 1920x1080   --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 6 --numruns 10 --source fiu --immediatemode 
date
