#!/bin/bash 
#SBATCH -J dwrf_rgluray_t6_n8 
#SBATCH -N 8
#SBATCH -n 8 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/outs/dwrf_rgluray_t6_n8.out
#SBATCH -t 04:00:00
set -x
date
module load qt
module load paraview/4.1.0
module use /work/01336/carson/opt/modulefiles
export PATH=/home/01249/gda/pvospray/pv-4.1/bin:$PATH
export LD_LIBRARY_PATH=/work/01249/gda/maverick/git/ospray/release:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/01249/gda/pvospray/pv-4.1/lib/paraview-4.1:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/01249/gda/plugins/gdal/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/01249/gda/plugins/proj-4.9.1/src/.libs:$LD_LIBRARY_PATH
export DISPLAY=:1
module load netcdf
DISPLAY=:0.0 ibrun -n 8 -o 0    /opt/apps/intel14/mvapich2_2_0/paraview/4.1.0/bin/pvbatch /work/01891/adb/maverick/svb_adb/pv_bench.py   -w 1920x1080  --nocamera --save_images -i /work/01891/adb/maverick/svb_adb/benchmarks/images/ --geoLevel 6 --numruns 10 --source wrf --immediatemode 
date
