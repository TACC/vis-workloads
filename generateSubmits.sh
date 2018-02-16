#!/bin/bash
#
# Read the config file to set paths.
#
. ./paths.sh
DIR=$output_DIR
IMAGE_DIR=$ROOT_IMAGE_DIR

NUM_RUNS=10
mkdir $DIR
mkdir $DIR/outs
mkdir $DIR/submits
mkdir $DIR/interactive

if [ ${GENERATE_IMAGES} == "ON" ]; then
    mkdir  $IMAGE_DIR/images
fi

#rm $DIR/submits/*
#rm $DIR/interactive/*
PND="#"

function processBench {
    tri=$1
    node=$2
    proc=$3
    renderer=$4
    dataSource=$5
    account=$6
    if [ $renderer == "swr" ]; then
       NAME=d${dataSource}_r${renderer}_t${tri}_N${node}_n${proc}
    else
       NAME=d${dataSource}_r${renderer}_t${tri}_N${node}_n${proc}
    fi
    FILE=${DIR}/submits/submit_${NAME}.sh
    echo "${PND}!/bin/bash " >${FILE}
    echo "#SBATCH -J ${NAME} " >> ${FILE} #echo "#$ -q normal " >> ${FILE}
    # echo "#SBATCH -N ${node}"  >> ${FILE}
    echo "#SBATCH -N ${node}"  >> ${FILE}
    echo "#SBATCH -n $(( ${node} * ${proc} )) " >> ${FILE}
    queue="vis"

#    if [ "$dataSource" != "fiu" ]; then
#    if [ "$dataSource" != "fiu_animated" ]; then
#      if [ "$dataSource" != "molecule" ]; then
#        if [ "$dataSource" != "geo" ]; then
#          if [ "$node" -lt 2 ]; then
#            queue="largemem"
#          fi
#        fi
#      fi
#    fi
#    fi

    DL_FLAG=""

    if [ ${IMMEDIATEMODE} == "OM" ]; then
        DL_FLAG="--immediatemode"
    fi

    IMG_FLAG=""
     

    if [ ${GENERATE_IMAGES} == "ON" ]; then
          IMG_FLAG="--save_images -i ${IMAGE_DIR}/images/"
    fi
    
    #if [ $dataSource == "fiu" ]; then
    #      NUM_RUNS=10
    #elif [ $dataSource == "rm" ]; then
    #      NUM_RUNS=10
    #elif [ $dataSource == "dns" ]; then
    #      NUM_RUNS=10
    #elif [ $dataSource == "dns_vol" ]; then
    #      NUM_RUNS=10
    #elif [ $dataSource == "dns_1024" ]; then
    #      NUM_RUNS=10
    #elif [ $dataSource == "geo" ]; then
    #      NUM_RUNS=10
    #elif [ $dataSource == "molecule" ]; then
    #      NUM_RUNS=10
    #fi    

    echo "#SBATCH -p $queue " >> ${FILE}
    echo "#SBATCH -A $account " >> ${FILE}
    OUTFILE="${DIR}/outs/${NAME}.out"
    echo "#SBATCH -o ${OUTFILE}" >> ${FILE}
    echo "#SBATCH -t 04:00:00"  >> ${FILE}
    echo "set -x" >> ${FILE}
    GLURAY_CMD=""
    SWR_CMD=""
    if [ $renderer == "swr" ]; then
      # SWR_CMD=LD_PRELOAD=/scratch/01336/carson/intelTACC/SWR-OGL1.4-2417/Centos/libGL.so.1
      # SWR_CMD=LD_PRELOAD=/work/01336/carson/intelTACC/SWR-OGL1.4-2445/CentOS/libGL.so.1
      #SWR_CMD=LD_PRELOAD="$SWR_LIB swr"
      SWR_CMD="swr"
    elif [ $renderer == "gluray" ]; then
      #GLURAY_CMD=/work/01336/carson/git/GLuRay/buildOptix/gluray
      GLURAY_CMD=$GLuRay_PATH
    else
      PRELOAD=""
    fi
    PARAVIEW=$ParaView_DIR/bin/pvbatch
    PRE_CMD=$ENV_COMMAND
    ENV_FLAGS=""
    PV_PLUGIN_FLAG=""
    if [ $renderer == vbo ]; then
      PV_PLUGIN_FLAG="--vbo"
    elif [ $renderer == "ospray" ]; then
      PV_PLUGIN_FLAG="--osp"
      PARAVIEW=$ParaViewGL2_DIR/bin/pvbatch
    elif [ $renderer == "osprayao" ]; then
      PV_PLUGIN_FLAG="--osp --ao"
      PARAVIEW=$ParaViewGL2_DIR/bin/pvbatch
    elif [ $renderer == "gluray" ]; then
      PRE_CMD="DISPLAY=:0.0"
      PV_PLUGIN_FLAG="--gluray"
    elif [ $renderer == "swr" ]; then
      PARAVIEW="pvbatch"
      PV_PLUGIN_FLAG="--swr"
      PRE_CMD="DISPLAY=:0.0"
    elif [ $renderer == "gpu2" ]; then
      PARAVIEW=$ParaViewGL2_DIR/bin/pvbatch
      PV_PLUGIN_FLAG="--gpu2"
    elif [ $renderer == "gpu" ]; then
      PARAVIEW=$ParaView_DIR/bin/pvbatch
      PV_PLUGIN_FLAG="--gpu"
    fi
    if [ $renderer == "swrvbo" ]; then
      # SWR_CMD=LD_PRELOAD=/scratch/01336/carson/intelTACC/SWR-OGL1.4-2445/CentOS/libGL.so.1
	SWR_CMD=LD_PRELOAD=$SWR_LIB
      # echo "export LD_PRELOAD=\"/scratch/01336/carson/intelTACC/SWR-OGL1.4-2417/Centos/libGL.so.1\"" >> ${FILE}
      PV_PLUGIN_FLAG="--vbo"
    fi
    echo "date" >> ${FILE}
    #PARAVIEW=/work/01336/carson/ParaView/ParaView-v4.1.0/buildICC/bin/pvbatch 
    #PARAVIEW=pvbatch
    #echo "module load qt" >> ${FILE}
    #echo "module load paraview/4.3.1" >> ${FILE}
    #PARAVIEW=pvbatch

    echo 'module load remora' >> ${FILE}
    echo 'module load swr' >> ${FILE}
    echo 'module load qt5' >> ${FILE}
    echo 'module load paraview' >> ${FILE}
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$TACC_PARAVIEW_LIB' >> ${FILE}
    echo 'export REMORA_PERIOD=1' >> ${FILE} 
    if [ $renderer == "gpu2" ]; then
        echo 'module load pvospray'  >> ${FILE}
    fi

    if [ $renderer == "gpu" ]; then
        #echo "module load pvospray/1.0.2" >> ${FILE}
        #ENV_FLAGS="${ENV_FLAGS} PV_PLUGIN_PATH=$pvOSPRay_DIR"
        echo "module load pvospray/5.0.0_gl1" >> ${FILE}
        echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/work/01336/carson/opt/apps/maverick/pvospray/5.0.0_gl1/lib' >> ${FILE}
        #echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/work/01336/carson/intelTACC/opt/maverick/lib' >> ${FILE}
    fi

    if [ $renderer == "ospray" -o $renderer == "osprayao" ]; then
        #echo "module load pvospray/1.0.2" >> ${FILE}
        #ENV_FLAGS="${ENV_FLAGS} PV_PLUGIN_PATH=$pvOSPRay_DIR"
        echo "module use /work/01336/carson/opt/modulefiles/stampede" >> ${FILE}
        echo "module load pvospray" >> ${FILE}
    fi

    if [ $renderer == "swr" ]; then
        #echo "module load pvospray/1.0.2" >> ${FILE}
        #ENV_FLAGS="${ENV_FLAGS} PV_PLUGIN_PATH=$pvOSPRay_DIR"
        echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$TACC_SWR_LIB' >> ${FILE}
    fi
    
    if [ $renderer == "gluray" ]; then
      DL_FLAG=""
      PARAVIEW=pvbatch
      echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/work/01336/carson/opt/apps/gluray/1.1.0/lib' >> ${FILE}
    fi
    if [ $renderer == "vbo" ]; then
      DL_FLAG=""
      PARAVIEW=$ParaView_DIR/bin/pvbatch
      ENV_FLAGS="${ENV_FLAGS} PV_PLUGIN_PATH=$pvVBO_DIR"
    fi

    if [ $dataSource == "wrf" ]; then
         echo 'export PATH=/home/01249/gda/pvospray/pv-4.1/bin:$PATH' >> ${FILE}
         echo 'export LD_LIBRARY_PATH=/work/01249/gda/maverick/git/ospray/release:$LD_LIBRARY_PATH' >> ${FILE}
         echo 'export LD_LIBRARY_PATH=/home/01249/gda/pvospray/pv-4.1/lib/paraview-4.1:$LD_LIBRARY_PATH' >> ${FILE}
         echo 'export LD_LIBRARY_PATH=/home/01249/gda/plugins/gdal/lib:$LD_LIBRARY_PATH' >> ${FILE}
         echo 'export LD_LIBRARY_PATH=/home/01249/gda/plugins/proj-4.9.1/src/.libs:$LD_LIBRARY_PATH' >> ${FILE}
         echo 'export DISPLAY=:1' >> ${FILE}
         echo 'module load netcdf' >> ${FILE}
     fi      
    
    if [ $renderer == "swr" ]; then
    DL_FLAG=""
    #    echo "export LD_PRELOAD=${SWR_CMD}" >> ${FILE}
    fi
    if [ $MPI_COMMAND == "ibrun" ]; then
        MPI_CMD="$MPI_COMMAND -n  $(( ${node} * ${proc} )) -o 0"
    elif [ $MPI_COMMAND == "mpirun" ]; then
	PRE_CMD=""
        MPI_CMD="$MPI_COMMAND -np $[node] -hostfile ${HOSTFILE} -perhost ${RANKS_PER_HOST}"
    fi
     echo "${ENV_FLAGS} ${PRE_CMD} ${MPI_CMD}  ${SWR_CMD} ${GLURAY_CMD} ${PARAVIEW} ${SVB_DIR}/pv_bench.py  ${PV_PLUGIN_FLAG} -w 1024x1024  ${IMG_FLAG} --geoLevel $tri --numruns ${NUM_RUNS} --source ${dataSource} ${DL_FLAG} " >> ${FILE}
     #echo "$PRE_CMD ibrun -n ${node} -o 0  ${SWR_CMD} ${GLURAY_CMD} ${PARAVIEW} ${SVB_DIR}/pv_bench.py  ${PV_PLUGIN_FLAG} -w 1920x1080  ${IMG_FLAG} --geoLevel $tri --numruns ${NUM_RUNS} --source ${dataSource} ${DL_FLAG} " >> ${FILE}
    echo "date" >> ${FILE}
    chmod ug+x ${FILE}
    IFILE=${DIR}/interactive/inter_${NAME}.sh
    echo "${FILE} 2>&1 | tee ${DIR}/outs/${NAME}.out" > ${IFILE}
    chmod +x $IFILE
}

function processTachyon {
    node=$1

    NAME=dvmd_molecule_rtachyon_t1_n${node}
    FILE=${DIR}/tachyon/submit_${NAME}.sh

    echo "${PND}!/bin/bash " >${FILE}
    echo "#SBATCH -J ${NAME} " >> ${FILE}
    echo "#SBATCH -N ${node}"  >> ${FILE}
    echo "#SBATCH -n $(( ${node} )) " >> ${FILE}
    queue="vis"
    echo "#SBATCH -p $queue " >> ${FILE}
    echo "#SBATCH -A $account " >> ${FILE}
    OUTFILE="${DIR}/tachyon/${NAME}.out"
    echo "#SBATCH -o ${OUTFILE}" >> ${FILE}
    echo "#SBATCH -t 00:40:00"  >> ${FILE}
    echo "set -x" >> ${FILE}


    echo "ibrun ${TACHYONBIN}  -trans_vmd +V -fullshade -aasamples 12 -rescale_lights 0.3 -add_skylight 1.0 -res 500 500 ${TACHYONDATA} -o ${DIR}/tachyon/${NAME}.tga" >> ${FILE}
    chmod +x ${FILE}

}

PRELOAD=""
#
# single node scaling
#
tris=( $GeometryLevels )
#tris=( 0 1 2 3 5 6 )
#procs=( 1 10 20 )
procs=($NumProcs)
nodes=($NumNodes)
#renderers=( "swr" "gpu" "gluray" "vbo" "ospray" "swrvbo")
COUNT=0
if [ ${USE_SWR} == "ON" ]; then
	renderers[$COUNT]="swr"
	COUNT=$((COUNT+1))
fi
if [ $USE_GPU == "ON" ]; then
	renderers[$COUNT]="gpu"
	COUNT=$((COUNT+1))
fi
if [ $USE_GPU2 == "ON" ]; then
	renderers[$COUNT]="gpu2"
	COUNT=$((COUNT+1))
fi
if [ $USE_GLURAY == "ON" ]; then
	renderers[$COUNT]="gluray"
	COUNT=$((COUNT+1))
fi
if [ $USE_VBO == "ON" ]; then
	renderers[$COUNT]="vbo"
	COUNT=$((COUNT+1))
fi
if [ $USE_OSPRAY == "ON" ]; then
	renderers[$COUNT]="ospray"
	COUNT=$((COUNT+1))
fi
if [ $USE_OSPRAYAO == "ON" ]; then
	renderers[$COUNT]="osprayao"
	COUNT=$((COUNT+1))
fi
if [ $USE_SWRVBO == "ON" ]; then
	renderers[$COUNT]="swrvbo"
	COUNT=$((COUNT+1))
fi
echo ${renderers[*]}
#dataSources=("fiu_animated" "fiu" "rm" "dns" "molecule" "geo")
dataSources=()
COUNT=0
if [ ${USE_FIU_ANIMATED} == "ON" ]; then
	dataSources[$COUNT]="fiu_animated"
	COUNT=$((COUNT+1))
fi
if [ ${USE_FIU} == "ON" ]; then
	dataSources[$COUNT]="fiu"
	COUNT=$((COUNT+1))
fi
if [ ${USE_RM} == "ON" ]; then
	dataSources[$COUNT]="rm"
	COUNT=$((COUNT+1))
fi
if [ ${USE_TURBULENCE} == "ON" ]; then
	dataSources[$COUNT]="turbulence"
	COUNT=$((COUNT+1))
fi
if [ ${USE_RM_TIME} == "ON" ]; then
        dataSources[$COUNT]="rm_time"
        COUNT=$((COUNT+1))
fi


if [ ${USE_DNS} == "ON" ]; then
	dataSources[$COUNT]="dns"
	COUNT=$((COUNT+1))
fi
if [ ${USE_MOLECULE} == "ON" ]; then
	dataSources[$COUNT]="molecule"
	COUNT=$((COUNT+1))
fi
if [ ${USE_GEO} == "ON" ]; then
	dataSources[$COUNT]="geo"
	COUNT=$((COUNT+1))
fi

if [ ${USE_WRF} == "ON" ]; then
        dataSources[$COUNT]="wrf"
        COUNT=$((COUNT+1))
fi

if [ ${USE_WHIPPLE} == "ON" ]; then
        dataSources[$COUNT]="moreland"
        COUNT=$((COUNT+1))
fi

if [ ${USE_WHIPPLE_TIME} == "ON" ]; then
        dataSources[$COUNT]="whipit"
        COUNT=$((COUNT+1))
fi


if [ ${USE_RM_ISOSWEEP} == "ON" ]; then
        dataSources[$COUNT]="rm_isosweep"
        COUNT=$((COUNT+1))
fi

if [ ${USE_RM_CLIPSWEEP} == "ON" ]; then
        dataSources[$COUNT]="rm_clipsweep"
        COUNT=$((COUNT+1))
fi

if [ ${USE_DNS_ISOSWEEP} == "ON" ]; then
        dataSources[$COUNT]="dns_isosweep"
        COUNT=$((COUNT+1))
fi


if [ ${USE_DNS_CLIPSWEEP} == "ON" ]; then
        dataSources[$COUNT]="dns_clipsweep"
        COUNT=$((COUNT+1))
fi

if [ ${USE_DNS_VOL} == "ON" ]; then
        dataSources[$COUNT]="dns_vol"
        COUNT=$((COUNT+1))
fi

echo ${dataSources[*]}
set -x


for tri in "${tris[@]}";
do
  for node in "${nodes[@]}";
  do
    for proc in "${procs[@]}";
    do 
      for renderer in "${renderers[@]}";
      do
        for data in "${dataSources[@]}";
        do
          processBench $tri $node $proc $renderer $data $ACCOUNT
        done
      done
    done
  done
done

#
# single node scaling
#
#tris=( 1 2 3)
#nodes=( 1 )
#renderer=swr
#renderers=( "gpu" "vbo" "ospray" "gluray")
#dataSources=("dns_isosweep" "dns_clipsweep" "rm_isosweep" "rm_clipsweep")
#if [ ${LDAV_RUNS} == "ON" ]; then
#  dataSources=("dns_isosweep" "dns_clipsweep" "rm_isosweep" "rm_clipsweep" "dns_isosweep_osp" "dns_clipsweep_osp" "rm_isosweep_osp" "rm_clipsweep_osp")
#fi
#set -x
#for i in "${tris[@]}"; do vglrun /work/01336/carson/git/GLuRay/buildOSPRay/gluray pvpython fiu.py  -w 1024x1024 --numStreamlines $i --numruns 100 |& tee gluray_fiu_$i.out ; done
#renderer=swr
#renderers=( "swr" "gpu" "gluray" "vbo" "ospray")
#dataSources=("fiu_animated" "fiu" "rm" "dns" "molecule" "geo")
#for i in "${tris[@]}"; do tacc_xrun pvpython fiu.py  -w 1024x1024 --numStreamlines $i --numruns 200 |& tee gpu_fiu_$i.out ; done
#PRELOAD=""
#PRELOAD=""

#for tri in "${tris[@]}";
#do
#  for node in "${nodes[@]}";
#  do
#    for renderer in "${renderers[@]}";
#    do
#      for data in "${dataSources[@]}";
#      do
#        processBench $tri $node $renderer $data $ACCOUNT
#      done
#    done
#  done
#done

if [ ${USE_TACHYON} == "ON" ]; then

     nodes=( 1 2 4 8 16 32)     
     mkdir  $DIR/tachyon
      for node in "${nodes[@]}";
 	 do
     		processTachyon $node
          done
fi
