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

    __datFile=$1
    _stage=$2
    _name=$3
    _inp=$4

    echo -n ""  $_name"_s"$_stage >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "first frame" | awk '{print $5}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "overall frame time" | awk '{print $6}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "overall frame time" | awk '{print $8}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "overall render time" | awk '{print $6}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "overall render time" | awk '{print $8}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "still zoomed out" | awk '{print $6}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "still zoomed out" | awk '{print $8}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "reader time" | awk '{print $3}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "filter time" | awk '{print $3}' ` >> ${__datFile}
    echo "" >> ${_datFile}


}

function processDynamicDat {
    _tri=$1
    _node=$2
    _renderer=$3
    _dataSource=$4
    _datFile=$5
    name=d${_dataSource}_r${_renderer}_t${_tri}_n${_node}
    inFile=${DIR}/outs/${name}.out
    #stages=`cat ${inFile} | grep "Total " | awk '{print $2}' `
    total=`grep "^Stage " $inFile | wc -l`
    
    let "total--"
    for stage in $(seq 0 $total);
    do
     writeOutDat $_datFile $stage $name $inFile
    done

        

  }


#
# node scaling
#
tris=( 1 6 )
nodes=( 1 2 4 8 16 32 )
renderers=("gpu" "swr")
dataSources=("fiu" "dns")

for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    datFile=${DIR}/dats/strongScale_d${data}_t${tri}.dat
    echo "#datFile strongScale_d${data}_t${tri}.dat" > ${datFile}
    echo "#runName first_frame, overall_frame_time, dev, overall_render_time, dev, still_zoomed_out, dev, rotate_zoomed_out, dev, zooming, dev, rotate_zoomed_in, dev, still_zoomed_in, dev, reader_time, filter_time" >> ${datFile}
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
#renderers=( "swr" "gpu" )
renderers=( "gpu" "swr")
dataSources=("fiu" "dns")

for data in "${dataSources[@]}";
do
  for node in "${nodes[@]}";
  do
  datFile=${DIR}/dats/triScale_d${data}_n${nodes}.dat
  echo "#datFile triScale_d${data}_t${tri}.dat" > ${datFile}
  echo "#runName first_frame, overall_frame_time, dev, overall_render_time, dev, still_zoomed_out, dev, rotate_zoomed_out, dev, zooming, dev, rotate_zoomed_in, dev, still_zoomed_in, dev, reader_time, filter_time" >> ${datFile}
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
#dynamic and timestep scaling
#


tris=( 6 )
nodes=( 1 )
renderers=("gpu" "swr") 
dataSources=("fiu_animated")

for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    datFile=${DIR}/dats/dynamic_d${data}_t${tri}.dat
    echo "#datFile dynamic_d${data}_t${tri}.dat" > ${datFile}
    echo "#runName, first_frame, overall_frame_time, dev, overall_render_time, dev, still_zoomed_out, dev, reader_time, filter_time" >> ${datFile}
    for renderer in "${renderers[@]}";
    do
      for node in "${nodes[@]}";
      do
        processDynamicDat $tri $node $renderer $data $datFile
      done
    done
    echo "" >> ${datFile}
  done
done

