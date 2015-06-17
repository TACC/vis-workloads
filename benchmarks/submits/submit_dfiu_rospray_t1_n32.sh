#!/bin/bash 
#SBATCH -J dfiu_rospray_t1_n32 
#SBATCH -N 32
#SBATCH -n 32 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/dfiu_rospray_t1_n32.out
#SBATCH -t 04:00:00
set -x
date
module load qt
module load paraview/4.1.0
module use /work/01336/carson/opt/modulefiles
module load pvospray/1.0.2
tacc_xrun ibrun -n 32 -o 0    /opt/apps/intel14/mvapich2_2_0/paraview/4.1.0/bin/pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py  --osp -w 1920x1080   --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 1 --numruns 10 --source fiu --immediatemode 
date
