#!/bin/bash 
#SBATCH -J dfiu_rgluray_t4_n2 
#SBATCH -N 2
#SBATCH -n 2 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/dfiu_rgluray_t4_n2.out
#SBATCH -t 00:40:00
set -x
date
module load qt
module load paraview/4.1.0
DISPLAY=:0.0 ibrun -n 2 -o 0   GLURAY_FIND-NOTFOUND /opt/apps/intel14/mvapich2_2_0/paraview/4.1.0/bin/pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py   -w 1920x1080   --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 4 --numruns 10 --source fiu --immediatemode 
date
