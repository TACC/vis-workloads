#!/bin/bash 
#SBATCH -J dfiu_rospray_t4_n4 
#SBATCH -N 4
#SBATCH -n 4 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/dfiu_rospray_t4_n4.out
#SBATCH -t 00:40:00
set -x
date
module load qt
module load paraview/4.1.0
tacc_xrun ibrun -n 4 -o 0    /pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py  --osp -w 1920x1080   --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 4 --numruns 10 --source fiu --immediatemode 
date
