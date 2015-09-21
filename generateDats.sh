#!/bin/bash
. ./paths.sh
DIR=$output_DIR
mkdir ${DIR}/dats_v1
#rm ${DIR}/dats/*
# set -x

function processDat {
    tri=$1
    node=$2
    proc=$3
    renderer=$4
    dataSource=$5
    datFile=$6
    name=d${dataSource}_r${renderer}_t${tri}_N${node}_n${proc}
    inFile=${DIR}/outs_v1/${name}.out
    echo -n $name >> ${datFile}
    echo -n "" `cat ${inFile} | grep "first frame" | awk '{print $5}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "fps" | awk '{print $2}' | awk '{print 1 / $1}' ` >> ${datFile}
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
    echo -n "" `cat ${inFile} | grep "pv_reader time" |  awk '{print $3}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "pv_filter time" |  awk '{print $3}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "reader time" | grep -v "pv_" | awk '{print $3}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "filter time" | grep -v "pv_" | awk '{print $3}' ` >> ${datFile}
    echo -n "" `cat ${inFile} | grep "Memory" | awk '{print $2}' | awk '{$0=substr($0,0,length($0)-2); print $0}' ` >> ${datFile}
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
    __node=$5
    __proc=$6

    echo -n $_name"_s"$_stage >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "first frame" | awk '{print $5}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "fps" | awk '{print $2}' | awk '{print 1 / $1}' ` >> ${datFile}
    echo -n ""  `processStage $_inp $_stage | grep "overall render time" | awk '{print $6}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "reader time" | grep -v "pv_" | awk '{print $3}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "filter time" | grep -v "pv_" | awk '{print $3}' ` >> ${__datFile}
    echo -n ""  `processStage $_inp $_stage | grep "Memory" | awk '{print $2}' | awk '{$0=substr($0,0,length($0)-2); print $0}' ` >> ${__datFile}
    echo "" >> ${_datFile}



    


}

function processDynamicDat {
    _tri=$1
    _node=$2
    _proc=$3
    _renderer=$4
    _dataSource=$5
    _datFile=$6
    name=d${_dataSource}_r${_renderer}_t${_tri}_N${_node}_n${_proc}
    inFile=${DIR}/outs_v1/${name}.out
    num_stages=`cat ${inFile} | grep "Total Stages:" | awk '{print $3}' `
    
    #this does not correctly count the stages when the job crashes
    #total=`grep "^Stage " $inFile | wc -l`
     
     
     
    total=${num_stages}
    for stage in $(seq 0 $total);
    do
       writeOutDat $_datFile $stage $name $inFile $_node $_proc
     
     done        

  }


function processDynamicDatStage {
   

  
    _tri=$1
    _node=$2
    _proc=$3
    _renderer=$4
    _dataSource=$5
    _datFile=$6
    _stage=$7
    name=d${_dataSource}_r${_renderer}_t${_tri}_N${_node}_n${_proc}
    inFile=${DIR}/outs_v1/${name}.out

    #this does not correctly count the stages when the job crashes
    #total=`grep "^Stage " $inFile | wc -l`

    writeOutDat $_datFile $_stage $name $inFile $_node $_proc

  }





#
# node scaling
#
tris=( 0 1 6 )
nodes=( 1 2 4 8 16 32 )
procs=( 1 )
renderers=("gpu" "swr" "swr14")
dataSources=("fiu")

for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    datFile=${DIR}/dats_v1/nodeScale_d${data}_t${tri}.dat
    echo "#datFile nodeScale_d${data}_t${tri}.dat" > ${datFile}
    echo "#runName first_frame, overall_frame_time, dev, overall_render_time, dev, still_zoomed_out, dev, rotate_zoomed_out, dev, zooming, dev, rotate_zoomed_in, dev, still_zoomed_in, dev, reader_time, filter_time" >> ${datFile}
    for renderer in "${renderers[@]}";
    do
      for node in "${nodes[@]}";
      do
        for proc in "${procs[@]}";
        do
           processDat $tri $node $proc $renderer $data $datFile
        done
      done
    done
    echo "" >> ${datFile}
  done
done



#
# single node scaling processor
#
tris=( 0 1 6 )
nodes=( 1 )
procs=(1 10 20)
renderers=("gpu" "swr" "swr14" "ospray" "gluray")
dataSources=("fiu" "dns_vol")

for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    datFile=${DIR}/dats_v1/procScale_d${data}_t${tri}.dat
    echo "#datFile procScale_d${data}_t${tri}.dat" > ${datFile}
    echo "#runName first_frame, overall_frame_time, dev, overall_render_time, dev, still_zoomed_out, dev, rotate_zoomed_out, dev, zooming, dev, rotate_zoomed_in, dev, still_zoomed_in, dev, reader_time, filter_time, memory" >> ${datFile}
    for renderer in "${renderers[@]}";
    do
      for node in "${nodes[@]}";
      do
        for proc in "${procs[@]}";
        do
           processDat $tri $node $proc $renderer $data $datFile
        done
      done
    done
    echo "" >> ${datFile}
  done
done












#
# single node triangle scaling
#
tris=( 1 2 3 4 5 6 7 8 9)
nodes=( 1 )
procs=(1)
renderers=("gpu" "swr" "swr14" "ospray" "gluray")
dataSources=("fiu")

for data in "${dataSources[@]}";
do
  for node in "${nodes[@]}";
  do
  datFile=${DIR}/dats_v1/triScale_d${data}_n${nodes}.dat
  echo "#datFile triScale_d${data}_t${tri}.dat" > ${datFile}
  echo "#runName first_frame, overall_frame_time, dev, overall_render_time, dev, still_zoomed_out, dev, rotate_zoomed_out, dev, zooming, dev, rotate_zoomed_in, dev, still_zoomed_in, dev, reader_time, filter_time, memory" >> ${datFile}
  for renderer in "${renderers[@]}";
  do
      for tri in "${tris[@]}";
      do
        for node in "${nodes[@]}";
        do
          for proc in "${procs[@]}";
          do
            processDat $tri $node $proc $renderer $data $datFile
          done
        done
      done
    done
  done
  echo "" >> ${datFile}
done




#
#dynamic and timestep scaling
#


tris=( 0 1 2 3 4 6)
nodes=(1 )
procs=( 1 )
renderers=("gpu" "swr" "swr14" "ospray" "gluray")
dataSources=("whipit" "fiu_animated" "dns_isosweep" "dns_clipsweep" "rm_isosweep" "rm_clipsweep" "dns_isosweep_512")
num_stages=0
for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    datFile=${DIR}/dats_v1/dynamic_d${data}_t${tri}.dat
    echo "#datFile dynamic_d${data}_t${tri}.dat" > ${datFile}
    echo "#runName, first_frame, overall_frame_time, overall_render_time, reader_time, filter_time, memory" >> ${datFile}
    for renderer in "${renderers[@]}";
    do
      for node in "${nodes[@]}";
      do
        for proc in "${procs[@]}";
        do
          processDynamicDat $tri $node $proc $renderer $data $datFile
        done
      done
    done
    echo "" >> ${datFile}
    sed -i "1iStages: ${num_stages}" ${datFile}
  done
done



#
#dynamic and timestep scaling: singleStage proc scaling
#


stage=(1)
tris=( 0 1 2 3 4)
nodes=( 1 )
procs=( 1 10 20)
renderers=("gpu" "swr" "swr14" "ospray" "gluray")
dataSources=("whipit" "fiu_animated" "dns_isosweep" "dns_clipsweep" "rm_isosweep" "rm_clipsweep" "dns_isosweep_512")
for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    datFile=${DIR}/dats_v1/dyProc_d${data}_t${tri}_s${stage}.dat
    echo "#datFile dyProc_d${data}_t${tri}.dat" > ${datFile}
    echo "#runName, first_frame, overall_time, overall_render_time, reader_time, filter_time, memory" >> ${datFile}
    for renderer in "${renderers[@]}";
    do
      for node in "${nodes[@]}";
      do
        for proc in "${procs[@]}";
        do
          processDynamicDatStage $tri $node $proc $renderer $data $datFile $stage
        done
      done
    done
    echo "" >> ${datFile}
  done
done

#
#dynamic and timestep scaling: singleStage node scaling
#


tris=( 0 1 2 3 4 6)
nodes=( 1 2 4 8 16 32 )
procs=( 1 )
renderers=("gpu" "swr" "swr14" "ospray" "gluray")
dataSources=("whipit" "fiu_animated" "dns_isosweep" "dns_clipsweep" "rm_isosweep" "rm_clipsweep" "dns_isosweep_512")
stage=1
for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    datFile=${DIR}/dats_v1/dyNode_d${data}_t${tri}_s${stage}.dat
    echo "#datFile dyNode_d${data}_t${tri}.dat" > ${datFile}
    echo "#runName, first_frame, overall_time, overall_render_time, reader_time, filter_time, memory" >> ${datFile}
    for renderer in "${renderers[@]}";
    do
      for node in "${nodes[@]}";
      do
        for proc in "${procs[@]}";
        do
          processDynamicDatStage $tri $node $proc $renderer $data $datFile $stage
        done
      done
    done
    echo "" >> ${datFile}
  done
done
