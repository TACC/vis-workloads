#!/bin/bash
. ./paths.sh
DIR=$output_DIR
mkdir ${DIR}/dats
rm ${DIR}/dats/*
# set -x

function processDat {
    tri=$1
    node=$2
    renderer=$3
    dataSource=$4
    datFile=$5
    name=d${dataSource}_r${renderer}_t${tri}_n${node}
    inFile=${DIR}/outs/${name}.out
    echo -n $name >> ${datFile}
    echo -n "" `cat ${inFile} | grep "first frame" | awk '{print $5}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "overall frame time" | awk '{print $6}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "overall frame time" | awk '{print $8}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "overall render time" | awk '{print $6}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "overall render time" | awk '{print $8}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "still zoomed out" | awk '{print $6}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "still zoomed out" | awk '{print $8}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "rotate zoomed out" | awk '{print $6}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "rotate zoomed out" | awk '{print $8}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "zooming" | awk '{print $4}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "zooming" | awk '{print $6}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "rotate zoomed in" | awk '{print $6}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "rotate zoomed in" | awk '{print $8}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "still zoomed in" | awk '{print $6}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "still zoomed in" | awk '{print $8}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "reader time" | awk '{print $3}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "filter time" | awk '{print $3}' ` >> ${datFile}
    echo "" >> ${datFile}
  }



function processStage {

_inp=$1
_count=$2
sed -n "/Stage ${_count}/,/Stage $((_count+1))/p" $_inp

}


function writeOutDat {

    _datFile=$1
    _count=$2
    _name=$3
    _inp=$4

    echo -n "" $name >> ${_datFile}
    echo -n "" $count >> ${_datFile}
    echo -n ""  `processStage $_inp $_count | grep "first frame" | awk '{print $5}' ` >> ${_datFile}
    echo -n ""  `processStage $_inp $_count | grep "overall frame time" | awk '{print $6}' ` >> ${_datFile}
    echo -n ""  `processStage $_inp $_count | grep "overall frame time" | awk '{print $8}' ` >> ${_datFile}
    echo -n ""  `processStage $_inp $_count | grep "overall render time" | awk '{print $6}' ` >> ${_datFile}
    echo -n ""  `processStage $_inp $_count | grep "overall render time" | awk '{print $8}' ` >> ${_datFile}
    echo -n ""  `processStage $_inp $_count | grep "still zoomed out" | awk '{print $8}' ` >> ${_datFile}
    echo -n ""  `processStage $_inp $_count | grep "reader time" | awk '{print $3}' ` >> ${_datFile}
    echo -n ""  `processStage $_inp $_count | grep "filter time" | awk '{print $3}' ` >> ${_datFile}
    echo "" >> ${_datFile}


}

function processDynamicDat {
    tri=$1
    node=$2
    renderer=$3
    dataSource=$4
    datFile=$5
    name=d${dataSource}_r${renderer}_t${tri}_n${node}
    inFile=${DIR}/outs/${name}.out
    #stages=`cat ${inFile} | grep "Total " | awk '{print $2}' `
    total=`grep "^Stage " $inFile | wc -l`
    count=0
    
    let "total--"
    for count in $(seq 0 $total);
    do
     writeOutDat $datFile $count $name $inFile
    done

        

  }


#
# node scaling
#
tris=(  6  )
nodes=( 1 2 4 8 16 32 )
renderers=("gpu")
dataSources=("fiu")

for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    datFile=${DIR}/dats/strongScale_d${data}_t${tri}.dat
    echo "#datFile strongScale_d${data}_t${tri}.dat" > ${datFile}
    echo "#runName first frame, overall frame time, dev, overall render time, dev, still zoomed out, dev, rotate zoomed out, dev, zooming, dev, rotate zoomed in, dev, still zoomed in, dev, reader time, filter time" >> ${datFile}
    for renderer in "${renderers[@]}";
    do
      for node in "${nodes[@]}";
      do
        processDat $tri $node $renderer $data $datFile
        
      done
    done
    echo "" >> ${datFile}
  done
done












#
# single node scaling
#
tris=( 1 2 3 4 5 6 7 8 9)
nodes=( 1 )
#renderers=( "swr" "gpu" "gluray" "vbo" "ospray" )
renderers=( "gpu")
dataSources=("fiu")
set -x
PRELOAD=""

for data in "${dataSources[@]}";
do
  for node in "${nodes[@]}";
  do
  datFile=dats/triScale_d${data}_n${nodes}.dat
  echo "#datFile triScale_d${data}_t${tri}.dat" > ${datFile}
  echo "#runName first frame, overall frame time, dev, overall render time, dev, still zoomed out, dev, rotate zoomed out, dev, zooming, dev, rotate zoomed in, dev, still zoomed in, dev, reader time, filter time" >> ${datFile}
  for renderer in "${renderers[@]}";
  do
      for tri in "${tris[@]}";
      do
        processDat $tri $node $renderer $data $datFile
      done
    done
  done
  echo "" >> ${datFile}
done


#
#dynamic and timestep
#


tris=( 6 )
nodes=( 1 2 4 8 16 32 )
renderers=("gpu")
dataSources=("fiu_animated")

for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    datFile=${DIR}/dats/dynamic_d${data}_t${tri}.dat
    echo "#datFile dynamic_d${data}_t${tri}.dat" > ${datFile}
    echo "#runName, stage, first_frame, overall_frame_time, dev, overall_render_time, dev, still_zoomed_out, dev, reader time, filter time" >> ${datFile}
    for renderer in "${renderers[@]}";
    do
      for node in "${nodes[@]}";
      do
        processDynamicDat $tri $node $renderer $data $datFile
      done
    done
    #echo "" >> ${datFile}
  done
done

