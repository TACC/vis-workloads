#!/bin/bash 
#SBATCH -J dwhipit_rswr_t1_n1 
#SBATCH -N 1
#SBATCH -n 1 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/dwhipit_rswr_t1_n1.out
#SBATCH -t 04:00:00
set -x
date
module load qt
module load paraview/4.1.0
module use /work/01336/carson/opt/modulefiles
tacc_xrun ibrun -n 1 -o 0  LD_PRELOAD=libGL.so.1  /opt/apps/intel14/mvapich2_2_0/paraview/4.1.0/bin/pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py   -w 1920x1080  --nocamera --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 1 --numruns 10 --source whipit --immediatemode 
date
