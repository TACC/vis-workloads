#!/bin/bash

module load vmd
cd /work/00401/pnav/workloads/vmd_molecule/stmvestatics
vmd -e stmv_qsurf_estatics.vmd
