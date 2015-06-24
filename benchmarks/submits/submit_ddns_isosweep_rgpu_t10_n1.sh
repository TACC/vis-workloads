#!/bin/bash 
#SBATCH -J ddns_isosweep_rgpu_t10_n1 
#SBATCH -N 1
#SBATCH -n 1 
#SBATCH -p vis 
#SBATCH -A A-ccvis 
#SBATCH -o /work/00401/pnav/workloads/svb_st/benchmarks/outs/ddns_isosweep_rgpu_t10_n1.out
#SBATCH -t 04:00:00
set -x
date
module load qt
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/work/01336/carson/git/osprayGHDev/buildStampedeICCRelease
 tacc_xrun ibrun -n 1 -o 0    /work/01336/carson/ParaView/ParaView-v4.3.1-source/buildStampedeICCRelease/bin/pvbatch /work/00401/pnav/workloads/svb_st/pv_bench.py   -w 1920x1080    --geoLevel 10 --numruns 10 --source dns_isosweep --immediatemode 
date
