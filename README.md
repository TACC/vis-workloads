 Instructions for Running Benchmarks (Beta, v2):

2) You can set up the environment by editing the path.sh file directly or by using cmake:
This will allow the specification of the paths for the datasets, applications, libraries and output directories as well as options such as which renderer to use.
for more info on cmake: www.cmake.org/runningcmake 
bashshell$ ccmake .
"c" to configure 
Specify the paths manually if cmake does not automatically find them, you will need to enter paths to the data files, for TACC/Intel use for now  /work/00401/pnav/workloads/ contains the data or links to the data 
"g" to generate, if there are some paths that are not specified then cmake will give and error, but just hit "q" and the paths.sh will be updated (will change this behavior later so cmake will only give an error if critical things aren't found)
cmake will output the variables to a file path.sh that is used by pv_bench.py, generateSubmits.sh, generateGraphs.sh and  generateGraphs.sh 


3) Test running the benchmark interactively, the benchmark output will go to stdout:
to test the benchmarks try:
bashshell$ module load qt paraview
bashshell$ (for TACC systems to ensure env is set up properly) module use /work/01336/carson/opt/modulefiles/
bashshell$ vglrun pvpython pv_bench.py --source fiu

4) Generate submit scripts:
There is a file called generateSubmits.sh, running this file will generate a folder "benchmarks"  with subfolders "submits", "interactive", and "outs" files in the "submits" folder corresponding to different runs. "submits" contains submission scripts for each run, and "outs" will contain the outputs from the jobs once they are run.
"interactive" contains scripts to run those submission scripts interactively, this just runs the same script as batch but on the current node and pipes output to the correct place  

5) Run benchmark:
example:
for i in `ls submits/submit_dfiu_rgpu_t6_n*.sh`; do sbatch $i; done
this will run all submission scripts using basic gpu render in paraview from 1 to 32 nodes.
the t# indicates the level of geometry scaling (only enabled for fiu and dns currently)
and the n# is the number of nodes

 
6) Parse/Process Results:
Results are stored in outs. The generateDats.sh script is a bash script that will parse the raw output files to create a number of different data files for plotting in excel or with the generateGraphs.sh to provide basic gnuplot plots of node scaling, processor scaling, triangle scaling and dynamic scaling (parameters as they change per stage) are supported currently. 
For static data-sets:
Timings are done over portions of the animation as well as the whole run. For example "still zoomed out" gives the average fps, average time, and deviation of the frames spent in the initial zoomed out view. There is an initial warmup period for all results not currently timed for loading and setup. Memory use and the total number of triangles is also reported.
For dynamic data-sets:
Timings are tracked "per stage" that correspond to an attribute being changes (e.g. position of a clipping plane, isosurface value or timestep).  For the node and processor scaling options, one Stage is selected 

The generateDats.sh file can be edited directly to change the parameters for 1)nodes 2) processors 3)data-sets 3)renderers 4)stage selection (for dynamic data)
 

7) Adding new scripts:
to add a new source script you just need to implement two functions , svbSetup and svbRender, which you can see examples of in pv_scripts/fiu.py. Then just add x from "x.py" that you added to the pv_scripts directory to the list of sources in generateScripts. GeometryLevel is an indication of a script-specific level of geometry. For example, the fiu has 10 geometry levels from 0-9 which it interprets to generate different amounts of streamlines for each of those levels. Whether or not you need to add this depends on the run you want to do.



# VIS Workloads

Scripting library used to benchmark and test different rendering engines across supercluster resources.

## Getting Started

These instructions will explain the different files contained inside the repository, their uses, and how to generate and submit benchmarking scripts. 

### Prerequisites

Clone the repository into a location located inside your home directory in a supercluster location

```
$ git clone https://github.com/TACC/vis-workloads.git
```

### File Descriptions

* CmakeLists.txt
* generateDats.sh - script to parse the and put results into a more easily readable format
* generateGraphs.sh - script used to generate graphs for the triangle and node scaling across all the renderers
* generateSubmits.sh - supplementary script to generate slurm scripts to launch all of the data-sets with varying geometry scaling using all the renderers
* graphsDebug.sh
* paths.sh - this is written out by cmake to set paths for libaries/applications/paths required for the bencmark. You can also edit this file manually if you wish. This is read by a few files for loading certain libraries and placing results in their proper folders.
* pv_bench.py - the primary python script for running benchmark tests
* README.md - this file
* pv_scripts/ - contains python scripts for each datafile (as well as core modules in the benchmark.py file) 
    * fiu.py - static groundwater flow data-set with streamlines and contours "interactive" camera motion
    * molecule.py - static molecule data-set with pdb spheres and an obj of ribbons"interactive" camera motion
    * geo.py - static OBJ seismic horizons with "interactive" camerea motion
    * dns.py - static isosurfaces with "interactive" camera motion
    * rm.py - static isosurfaces with "interactive" camera motion
    * rm-time.py - time series rm data with isosurfaces without camera motion
    * wrf.py - streamlines and contours of climate data over chicago
    * whipit.py - for TACC/Intel use only time series whipple shield data without camera motion
    * moreland.py - for TACC/Intel use only, time series/dynamic whipple shield data with "interactive" camera motion
    * fiu_animated - fiu dataset with incrementally increasing streamlines
* visit_scripts visit python scripts for creating desirec visualization (under development)
* vmd_scripts - python scripts to generate tachyon files from pdb or dcd files (under development)

### Paths.sh setup

You can set up the environment by editing the path.sh file directly. This will allow the specification of the paths for the datasets, applications, libraries and output directories as well as options such as which renderer to use. You will need to enter paths to the data files TACC/Intel use for now. `/work/00401/pnav/workloads` contains the data or links to the data. path.sh that is used by pv_bench.py, generateSubmits.sh, generateGraphs.sh and generateGraphs.sh


### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

