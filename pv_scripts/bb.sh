export PATH=/home/01249/gda/pvospray/pv-4.1/bin:$PATH
export LD_LIBRARY_PATH=/work/01249/gda/maverick/git/ospray/release::$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/01249/gda/pvospray/pv-4.1/lib/paraview-4.1:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/01249/gda/plugins/gdal/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/01249/gda/plugins/proj-4.9.1/src/.libs:$LD_LIBRARY_PATH
export DISPLAY=:1

pvpython wrf.py

