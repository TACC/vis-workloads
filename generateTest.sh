#!/bin/bash
#set -x
. ./paths.sh
DIR=$output_DIR
mkdir ${DIR}/graphs



tris=( 6 )
nodes=( 1 )
renderers=( "swr" "gpu" )
dataSources=("fiu_animated")

for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
  name="dynamic_d${data}_t${tri}"
  datFile=${DIR}/dats/${name}.dat
  stages=`cat ${datFile} | grep "Stages" | awk '{print $2}' `
  echo ${stages}
  graphFile=${DIR}/graphs/${name}.gnuplot
  graphTitle=${name}

  createGraph $graphFile $graphTitle ${DIR}/graphs/${name} nodes seconds strongScale
  counter=0
  for renderer in "${renderers[@]}";
  do
       for stage in $(seq 0 $stages);
       do
        title=$renderer
        column=5
        grepString="_r${renderer}_"
        addPlot $title $datFile $graphFile $grepString $column $counter "dynamicScale"
        counter=$(( $counter + 1 ))
       done
    done
    echo "" >> ${graphFile}
  gnuplot ${graphFile}
  convert ${DIR}/graphs/${graphTitle}.svg ${DIR}/graphs/${graphTitle}.png
  done
done

