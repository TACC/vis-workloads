#!/bin/bash
#set -x
. ./paths.sh
DIR=$output_DIR
mkdir ${DIR}/graphs

#
# gnuplot
#
function createGraph
{
  graphFile=$1
  graphTitle=$2
  outFile=$3
  xAxis=$4
  yAxis=$5
  graphType=$6
  GP_FILE=${graphFile}
  echo "#graph ${graphTitle}" > ${graphFile}
  #echo "set terminal postscript eps enhanced" >> ${GP_FILE}
  echo "set terminal svg" >> ${GP_FILE}
  #echo "set terminal epslatex size 3.5,2.62 standalone color colortext 10" >> ${GP_FILE}
  #echo "set output '${program}_${type}_${compositer}_${source}_${num_triangles}_${threads}.eps'" >> ${GP_FILE}
  echo "set output '${outFile}.svg'" >> ${GP_FILE}
  echo "set size 0.98,1.0" >> ${GP_FILE}
  echo "set datafile missing 'none'" >> ${GP_FILE}
  if [ "${graphType}" == "triScale" ]; then
    echo "set xtics (1,2,3,4,5,6,7,8,9)" >> ${GP_FILE}
    echo "set logscale x" >> ${GP_FILE}
    echo "set logscale y" >> ${GP_FILE}
  else
    echo "set logscale x" >> ${GP_FILE}
    echo "set xtics (1,2,4,8,16,32)" >> ${GP_FILE}
  fi
  echo "set key top left" >> ${GP_FILE}
  #echo "unset key" >> ${GP_FILE} 
  # echo "set ytics 10"  >> ${GP_FILE}
  echo "set tics scale 0.5"  >> ${GP_FILE}

  COLOR0="#0060ad"
  COLOR1="#888888"
  COLOR2="#ffb428"
  COLOR3="#28b4ff"
  COLOR4="#333333"
  COLOR5="#ad6000"
  colors=("#0060ad" "#888888" "#ffb428" "#28b4ff" "#333333" "#ad6000")

  COLOR0_1="#ff2068"
  COLOR1_1="#ff8888"
  COLOR2_1="#ff8104"
  COLOR3_1="#ff81aa"
  COLOR4_1="#ff3333"
  COLOR5_1="#adff00"
  echo "set border linewidth 2" >> ${GP_FILE}
  echo "set style line 1 lc rgb '${COLOR0}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 2 lc rgb '${COLOR1}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 3 lc rgb '${COLOR2}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 4 lc rgb '${COLOR3}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 5 lc rgb '${COLOR4}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 6 lc rgb '${COLOR5}' linetype 1 linewidth 5" >> ${GP_FILE}


  echo "set style line 10 lc rgb '${COLOR0_1}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 20 lc rgb '${COLOR1_1}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 30 lc rgb '${COLOR2_1}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 40 lc rgb '${COLOR3_1}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 50 lc rgb '${COLOR4_1}' linetype 1 linewidth 5" >> ${GP_FILE}
  echo "set style line 60 lc rgb '${COLOR5_1}' linetype 1 linewidth 5" >> ${GP_FILE}

  echo "set xlabel '$xAxis'" >> ${GP_FILE}
  echo "set ylabel '$yAxis'" >> ${GP_FILE}
  echo "set title '$graphTitle'" >> ${GP_FILE}
  # echo "set xrange[1:10]" >> ${GP_FILE}
  # echo "set yrange[0.007:100]" >> ${GP_FILE}
  echo "set grid lc rgb '#aaaaaa'" >> ${GP_FILE}
  echo "set pointsize 0.5" >> ${GP_FILE}
  echo ""
  # echo "plot '${type}_manta_${source}_${num_triangles}_${threads}.dat' notitle with points pointtype 7 linecolor rgb '#0060ad', '${type}_manta_${source}_${num_triangles}_${threads}.dat' title 'Paraview-Manta' smooth csplines with lines linestyle 1,\
  echo -n "plot " >> ${GP_FILE}
} 

function addPlot
{
  title=$1
  datFile=$2
  graphFile=$3
  grepString=$4
  column=$5
  counter=$6
  scaleType=$7
  file=${graphFile}.${title}.part
  fileD=/work/01891/adb/maverick/svb_adb/debug.txt
  echo "#datpart ${file}" > ${file}
  echo "grepString: ${grepString}" > ${fileD}
  #grab the lines for each renderer  
  grep ${grepString} ${datFile} | while read -r line; do
     #strip the _n or _t and print the geoLevel _t or number of nodes _n 
    if [ "${scaleType}" == "strongScale" ]; then
      echo -n `echo -n "$line" |  awk -F "_n" '/1/ {print $2}' | awk '{print $1}'` " " >> ${fileD}
    elif [ "${scaleType}" == "triScale" ]; then
      echo -n `echo -n "$line" |  awk -F "_t" '/1/ {print $2}' | awk -F "_" '{print $1}'` " " >> ${fileD}
  fi
    # echo -n "wee" >> ${file}
    #print the values
    echo $line >> ${fileD}
done

  if [ "$counter" -gt 0 ]; then
    echo -n ", " >> ${graphFile}
  fi
  echo -n "'${file}' using 1:$(( $column + 1 )) notitle with points pointtype 7 linecolor rgb '${colors[${counter}]}', '${file}' using 1:$(( $column + 1 )) title '${title}' with lines linestyle $(( ${counter} + 1 )) " >> ${graphFile}
}


#
# strong scaling
#
tris=( 6 )
nodes=( 1 2 4 8 16 32 )
renderers=( "swr" "gpu" )
dataSources=("fiu")

for data in "${dataSources[@]}";
do
  for tri in "${tris[@]}";
  do
    name="strongScale_d${data}_t${tri}"
    datFile=${DIR}/dats/${name}.dat
  graphFile=${DIR}/graphs/${name}.gnuplot
  graphTitle=${name}
  createGraph $graphFile $graphTitle ${DIR}/graphs/${name} nodes seconds strongScale
  counter=0 
  for renderer in "${renderers[@]}";
  do
      # for node in "${nodes[@]}";
      # do
        title=$renderer
        #column specifies the column we want to plot
        column=5
        grepString="_r${renderer}_"
        addPlot $title $datFile $graphFile $grepString $column $counter "strongScale"
        counter=$(( $counter + 1 ))
      # done
    done
    echo "" >> ${graphFile}
  gnuplot ${graphFile}
  convert ${DIR}/graphs/${graphTitle}.svg ${DIR}/graphs/${graphTitle}.png
  done
done





