#!/bin/bash 
#SBATCH -J dfiu_animated_rospray_t3_n1 
#SBATCH -N 1
#SBATCH -n 1 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/dfiu_animated_rospray_t3_n1.out
#SBATCH -t 00:40:00
set -x
date
module load qt
module load paraview/4.1.0
tacc_xrun ibrun -n 1 -o 0    /pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py  --osp -w 1920x1080  --nocamera --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 3 --numruns 10 --source fiu_animated --immediatemode 
date
