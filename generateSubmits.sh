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



rm $DIR/submits/*
rm $DIR/interactive/*
PND="#"

function processBench {
    tri=$1
    node=$2
    renderer=$3
    dataSource=$4
    account=$5
    NAME=d${dataSource}_r${renderer}_t${tri}_n${node}
    FILE=${DIR}/submits/submit_${NAME}.sh
    echo "${PND}!/bin/bash " >${FILE}
    echo "#SBATCH -J ${NAME} " >> ${FILE} #echo "#$ -q normal " >> ${FILE}
    echo "#SBATCH -N ${node}"  >> ${FILE}
    echo "#SBATCH -n $(( $node * 1 )) " >> ${FILE}
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

        DL_FLAG="--immediatemode"

    CAM_FLAG=""
    if [ "$dataSource" == "fiu_animated" ]; then
       CAM_FLAG="--nocamera"
    fi

     if [ "$dataSource" == "whipit" ]; then
       CAM_FLAG="--nocamera"
    fi


     if [ "$dataSource" == "wrf" ]; then
       CAM_FLAG="--nocamera"
    fi

      if [ "$dataSource" == "rm_isosweep" ]; then
       CAM_FLAG="--nocamera"
    fi

   if [ "$dataSource" == "dns_clipsweep" ]; then
       CAM_FLAG="--nocamera"
    fi


    IMG_FLAG=""
     

    if [ ${GENERATE_IMAGES} == "ON" ]; then
          IMG_FLAG="--save_images -i ${IMAGE_DIR}/images/"
    fi

    

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
	SWR_CMD=LD_PRELOAD=$SWR_LIB
    elif [ $renderer == "gluray" ]; then
      #GLURAY_CMD=/work/01336/carson/git/GLuRay/buildOptix/gluray
      GLURAY_CMD=$GLuRay_PATH
    else
      PRELOAD=""
    fi
    PRE_CMD=tacc_xrun
    ENV_FLAGS=""
    PV_PLUGIN_FLAG=""
    if [ $renderer == vbo ]; then
      PV_PLUGIN_FLAG="--vbo"
    elif [ $renderer == "ospray" ]; then
      PV_PLUGIN_FLAG="--osp"
    elif [ $renderer == "gluray" ]; then
      PRE_CMD="DISPLAY=:0.0"
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
    PARAVIEW=$ParaView_DIR/pvbatch
    echo "module load qt" >> ${FILE}
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/work/01336/carson/git/osprayGHDev/buildStampedeICCRelease' >> ${FILE} 
    #need to determing how to handle this, for general benchmarking, carson has two pvospray modules, one looks better and one is faster...
    #echo "module use /work/01336/carson/opt/modulefiles" >> ${FILE}
    if [ $renderer == "ospray" ]; then
        #echo "module load pvospray/1.0.2" >> ${FILE}
        ENV_FLAGS="${ENV_FLAGS} PV_PLUGIN_PATH=$pvOSPRay_DIR"
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
    
    #if [ $renderer == "swr" ]; then
    #    echo "export LD_PRELOAD=${SWR_CMD}" >> ${FILE}
    #fi
    if [ $MPI_COMMAND == "ibrun" ]; then
        MPI_CMD="$MPI_COMMAND -n $[node] -o 0"
    elif [ $MPI_COMMAND == "mpirun" ]; then
	PRE_CMD=""
        MPI_CMD="$MPI_COMMAND -np $[node] -hostfile ${HOSTFILE} -perhost ${RANKS_PER_HOST}"
    fi
     echo "${ENV_FLAGS} ${PRE_CMD} ${MPI_CMD}  ${SWR_CMD} ${GLURAY_CMD} ${PARAVIEW} ${SVB_DIR}/pv_bench.py  ${PV_PLUGIN_FLAG} -w 1024x1024  ${CAM_FLAG} ${IMG_FLAG} --geoLevel $tri --numruns ${NUM_RUNS} --source ${dataSource} ${DL_FLAG} " >> ${FILE}
     #echo "$PRE_CMD ibrun -n ${node} -o 0  ${SWR_CMD} ${GLURAY_CMD} ${PARAVIEW} ${SVB_DIR}/pv_bench.py  ${PV_PLUGIN_FLAG} -w 1920x1080  ${CAM_FLAG} ${IMG_FLAG} --geoLevel $tri --numruns ${NUM_RUNS} --source ${dataSource} ${DL_FLAG} " >> ${FILE}
    echo "date" >> ${FILE}
    chmod ug+x ${FILE}
    IFILE=${DIR}/interactive/inter_${NAME}.sh
    echo "${FILE} | 2>&1 tee ${DIR}/outs/${NAME}.out" > ${IFILE}
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
# node scaling
#
tris=( 1 6 9 )
nodes=( 1 2 4 8 16 32 )
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

if [ ${USE_DNS_CLIPSWEEP} == "ON" ]; then
        dataSources[$COUNT]="dns_clipsweep"
        COUNT=$((COUNT+1))
fi



echo ${dataSources[*]}
set -x


for tri in "${tris[@]}";
do
  for node in "${nodes[@]}";
  do
    for renderer in "${renderers[@]}";
    do
      for data in "${dataSources[@]}";
      do
        processBench $tri $node $renderer $data $ACCOUNT
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
if [ ${LDAV_RUNS} == "ON" ]; then
  dataSources=("dns_isosweep" "dns_clipsweep" "rm_isosweep" "rm_clipsweep" "dns_isosweep_osp" "dns_clipsweep_osp" "rm_isosweep_osp" "rm_clipsweep_osp")
fi
set -x
#for i in "${tris[@]}"; do vglrun /work/01336/carson/git/GLuRay/buildOSPRay/gluray pvpython fiu.py  -w 1024x1024 --numStreamlines $i --numruns 100 |& tee gluray_fiu_$i.out ; done
#renderer=swr
#renderers=( "swr" "gpu" "gluray" "vbo" "ospray")
#dataSources=("fiu_animated" "fiu" "rm" "dns" "molecule" "geo")
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
        processBench $tri $node $renderer $data $ACCOUNT
      done
    done
  done
done





if [ ${USE_TACHYON} == "ON" ]; then

     nodes=( 1 2 4 8 16 32)     
     mkdir  $DIR/tachyon
      for node in "${nodes[@]}";
 	 do

     		processTachyon $node

          done
fi
