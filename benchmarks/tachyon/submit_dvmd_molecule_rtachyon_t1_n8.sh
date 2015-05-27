#!/bin/bash 
#SBATCH -J dvmd_molecule_rtachyon_t1_n8 
#SBATCH -N 8
#SBATCH -n 8 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/01891/adb/maverick/svb_adb/benchmarks/tachyon/dvmd_molecule_rtachyon_t1_n8.out
#SBATCH -t 00:40:00
set -x
ibrun /home/01891/adb/tachyon/compile/linux-mpi/tachyon  -trans_vmd +V -fullshade -aasamples 12 -rescale_lights 0.3 -add_skylight 1.0 -res 500 500 /work/00401/pnav/workloads/vmd_molecule/balls.dat -o /work/00401/pnav/workloads/vmd_molecule/dvmd_molecule_rtachyon_t1_n8.tga
