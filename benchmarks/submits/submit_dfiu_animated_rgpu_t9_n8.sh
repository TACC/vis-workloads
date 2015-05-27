#!/bin/bash 
#SBATCH -J dfiu_animated_rgpu_t9_n8 
#SBATCH -N 8
#SBATCH -n 8 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/dfiu_animated_rgpu_t9_n8.out
#SBATCH -t 00:40:00
set -x
date
module load qt
module load paraview/4.1.0
tacc_xrun ibrun -n 8 -o 0    /pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py   -w 1920x1080  --nocamera --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 9 --numruns 10 --source fiu_animated --immediatemode 
date
