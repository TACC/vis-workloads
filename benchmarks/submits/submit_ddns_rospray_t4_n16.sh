#!/bin/bash 
#SBATCH -J ddns_rospray_t4_n16 
#SBATCH -N 16
#SBATCH -n 16 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/ddns_rospray_t4_n16.out
#SBATCH -t 00:40:00
set -x
date
module load qt
module load paraview/4.1.0
tacc_xrun ibrun -n 16 -o 0    /pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py  --osp -w 1920x1080   --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 4 --numruns 10 --source dns --immediatemode 
date
