#!/bin/bash 
#SBATCH -J dwhipit_rospray_t6_n2 
#SBATCH -N 2
#SBATCH -n 2 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/dwhipit_rospray_t6_n2.out
#SBATCH -t 04:00:00
set -x
date
module load qt
module load paraview/4.1.0
module use /work/01336/carson/opt/modulefiles
module load pvospray/1.0.2
tacc_xrun ibrun -n 2 -o 0    /opt/apps/intel14/mvapich2_2_0/paraview/4.1.0/bin/pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py  --osp -w 1920x1080  --nocamera --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 6 --numruns 10 --source whipit --immediatemode 
date
