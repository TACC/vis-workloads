#graph strongScale_dgeo_t6
set terminal svg
set output '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.svg'
set size 0.98,1.0
set datafile missing 'none'
set logscale x
set xtics (1,2,4,8,16,32)
set key top left
set tics scale 0.5
set border linewidth 2
set style line 1 lc rgb '#0060ad' linetype 1 linewidth 5
set style line 2 lc rgb '#888888' linetype 1 linewidth 5
set style line 3 lc rgb '#ffb428' linetype 1 linewidth 5
set style line 4 lc rgb '#28b4ff' linetype 1 linewidth 5
set style line 5 lc rgb '#333333' linetype 1 linewidth 5
set style line 6 lc rgb '#ad6000' linetype 1 linewidth 5
set style line 10 lc rgb '#ff2068' linetype 1 linewidth 5
set style line 20 lc rgb '#ff8888' linetype 1 linewidth 5
set style line 30 lc rgb '#ff8104' linetype 1 linewidth 5
set style line 40 lc rgb '#ff81aa' linetype 1 linewidth 5
set style line 50 lc rgb '#ff3333' linetype 1 linewidth 5
set style line 60 lc rgb '#adff00' linetype 1 linewidth 5
set xlabel 'nodes'
set ylabel 'seconds'
set title 'strongScale_dgeo_t6'
set grid lc rgb '#aaaaaa'
set pointsize 0.5
plot '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.swr.part' using 1:6 notitle with points pointtype 7 linecolor rgb '#0060ad', '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.swr.part' using 1:6 title 'swr' with lines linestyle 1 , '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.gpu.part' using 1:6 notitle with points pointtype 7 linecolor rgb '#888888', '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.gpu.part' using 1:6 title 'gpu' with lines linestyle 2 , '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.gluray.part' using 1:6 notitle with points pointtype 7 linecolor rgb '#ffb428', '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.gluray.part' using 1:6 title 'gluray' with lines linestyle 3 , '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.ospray.part' using 1:6 notitle with points pointtype 7 linecolor rgb '#28b4ff', '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.ospray.part' using 1:6 title 'ospray' with lines linestyle 4 , '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.vbo.part' using 1:6 notitle with points pointtype 7 linecolor rgb '#333333', '/work/01891/adb/maverick/svb_checkmerge3/benchmarks/graphs/strongScale_dgeo_t6.gnuplot.vbo.part' using 1:6 title 'vbo' with lines linestyle 5 
