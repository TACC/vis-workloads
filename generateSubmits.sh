#!/bin/bash
#tris=( 1 100 1000 2000 4000 8000 )
#DIR=/scratch/01336/carson/intelTACC/benchmarks
DIR=/work/01336/carson/intelTACC/benchmarks/maverick
SVB_DIR=/work/01336/carson/intelTACC/svb
NUM_RUNS=10
mkdir $DIR
mkdir $DIR/outs
mkdir $DIR/submits
mkdir $DIR/interactive
rm $DIR/submits/*
rm $DIR/interactive/*
PND="#"

function processBench {
    tri=$1
    node=$2
    renderer=$3
    dataSource=$4
    NAME=d${dataSource}_r${renderer}_t${tri}_n${node}
    FILE=${DIR}/submits/submit_${NAME}.sh
    echo "${PND}!/bin/bash " >${FILE}
    echo "#SBATCH -J ${NAME} " >> ${FILE} #echo "#$ -q normal " >> ${FILE}
    echo "#SBATCH -N ${node}"  >> ${FILE}
    echo "#SBATCH -n $(( $node * 1 )) " >> ${FILE}
    queue="vis"
    if [ "$dataSource" != "fiu" ]; then
    if [ "$dataSource" != "fiu_animated" ]; then
      if [ "$dataSource" != "molecule" ]; then
        if [ "$dataSource" != "geo" ]; then
          if [ "$node" -lt 2 ]; then
            queue="largemem"
          fi
        fi
      fi
    fi
    fi
    DL_FLAG=""
    if [ "$dataSource" == "dns" ]; then
      if [ "$renderer" == "gpu" ]; then
        DL_FLAG="--immediatemode"
      fi
    fi

    echo "#SBATCH -p $queue " >> ${FILE}
    echo "#SBATCH -A Vis-Workload-Charact" >> ${FILE}
    #echo "#SBATCH -A OSPRay" >> ${FILE}
    OUTFILE="${DIR}/outs/${NAME}.out"
    echo "#SBATCH -o ${OUTFILE}" >> ${FILE}
    echo "#SBATCH -t 00:40:00"  >> ${FILE}
    echo "set -x" >> ${FILE}
    GLURAY_CMD=""
    SWR_CMD=""
    if [ $renderer == "swr" ]; then
      # SWR_CMD=LD_PRELOAD=/scratch/01336/carson/intelTACC/SWR-OGL1.4-2417/Centos/libGL.so.1
      SWR_CMD=LD_PRELOAD=/work/01336/carson/intelTACC/SWR-OGL1.4-2445/CentOS/libGL.so.1
    elif [ $renderer == "gluray" ]; then
      GLURAY_CMD=/work/01336/carson/git/GLuRay/buildOptix/gluray
    else
      PRELOAD=""
    fi
    PRE_CMD=tacc_xrun
    PV_PLUGIN_FLAG=""
    if [ $renderer == vbo ]; then
      PV_PLUGIN_FLAG="--vbo"
    elif [ $renderer == "ospray" ]; then
      PV_PLUGIN_FLAG="--osp"
    elif [ $renderer == "gluray" ]; then
      PRE_CMD="DISPLAY=:0.0"
    fi
    if [ $renderer == "swrvbo" ]; then
      SWR_CMD=LD_PRELOAD=/scratch/01336/carson/intelTACC/SWR-OGL1.4-2445/CentOS/libGL.so.1
      # echo "export LD_PRELOAD=\"/scratch/01336/carson/intelTACC/SWR-OGL1.4-2417/Centos/libGL.so.1\"" >> ${FILE}
      PV_PLUGIN_FLAG="--vbo"
    fi
    echo "date" >> ${FILE}
    PARAVIEW=/work/01336/carson/ParaView/ParaView-v4.1.0/buildICC/bin/pvbatch 
    PARAVIEW=pvbatch
    echo "module load qt" >> ${FILE}
    echo "module load paraview/4.1.0" >> ${FILE}
    echo "$PRE_CMD ${SWR_CMD} ${GLURAY_CMD} ${PARAVIEW} ${SVB_DIR}/pv_bench.py  ${PV_PLUGIN_FLAG} -w 1920x1080  --geoLevel $tri --numruns ${NUM_RUNS} --source ${dataSource} ${DL_FLAG} " >> ${FILE}
    #echo "$PRE_CMD ibrun -n ${node} -o 0  ${SWR_CMD} ${GLURAY_CMD} ${PARAVIEW} /work/01336/carson/intelTACC/pv_bench.py  ${PV_PLUGIN_FLAG} -w 1920x1080  --geoLevel $tri --numruns 100 --source ${dataSource} ${DL_FLAG} " >> ${FILE}
    # echo "export LD_PRELOAD=\"\"" >> ${FILE}
    echo "date" >> ${FILE}
    chmod ug+x ${FILE}
    IFILE=${DIR}/interactive/inter_${NAME}.sh
    echo "${FILE} | 2>&1 tee ${DIR}/outs/${NAME}.out" > ${IFILE}
    chmod +x $IFILE
}

PRELOAD=""
#
# node scaling
#
tris=( )
nodes=( 1 2 4 8 16 32 )
renderers=( "swr" "gpu" "gluray" "vbo" "ospray" "swrvbo")
dataSources=("fiu_animated" "fiu" "rm" "dns" "molecule" "geo")
set -x


for tri in "${tris[@]}";
do
  for node in "${nodes[@]}";
  do
    for renderer in "${renderers[@]}";
    do
      for data in "${dataSources[@]}";
      do
        processBench $tri $node $renderer $data
      done
    done
  done
done

#
# single node scaling
#
tris=( 1 5 10)
nodes=( 1 )
renderer=swr
renderers=( "gpu" "vbo" "ospray")
dataSources=("dns_isosweep" "dns_clipsweep" "rm_isosweep" "rm_clipsweep")
set -x
#for i in "${tris[@]}"; do vglrun /work/01336/carson/git/GLuRay/buildOSPRay/gluray pvpython fiu.py  -w 1024x1024 --numStreamlines $i --numruns 100 |& tee gluray_fiu_$i.out ; done
#for i in "${tris[@]}"; do tacc_xrun pvpython fiu.py  -w 1024x1024 --numStreamlines $i --numruns 200 |& tee gpu_fiu_$i.out ; done
PRELOAD=""
#PRELOAD=""


for tri in "${tris[@]}";
do
  for node in "${nodes[@]}";
  do
    for renderer in "${renderers[@]}";
    do
      for data in "${dataSources[@]}";
      do
        processBench $tri $node $renderer $data
      done
    done
  done
done
