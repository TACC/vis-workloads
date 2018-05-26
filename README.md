# SVBench: Scientific Visualization Benchmarking Suite

## Website

[SVBench: Scientific Visualization Benchmarking Suite websites](https://tacc.github.io/vis-workloads/)

## Overview

The SVBench benchmark suite is designed to examine visualization processes on a diverse set of system configurations and has the flexibility to evaluate and steer the evolution of system configurations. The front-end to the benchmark suite is a set of scripts that generate batch job submission scripts, parsing scripts, and graph generation scripts. The benchmark suite is straightforward to update as it consists of a set of bash and python scripts which interact with python modules that either directly uses system timing information or application logs to extract the pertinent information. Paraview was selected as the primary benchmark applications as it can analyze extremely large datasets using distributed memory computing resources across scientific disciplines. Some scientific disciplines use specialized software for visualization, and the benchmark suite can be extended to also include these applications where appropriate. For example, molecular science research accounts for a quarter of TACC research projects, but ParaView and VisIt do not have tools to represent protein secondary structure, and are therefore not typically used for molecular visualization of proteins. To meet the needs of this research community, the benchmark suite also includes the most commonly used application for molecular science visualization, VMD.

## Dependencies

SVBench benchmark suite depends on Paraview. You can download the latest version from [Paraview download page](https://www.paraview.org/download/) or [build from source](https://www.paraview.org/Wiki/ParaView:Build_And_Install)

For the OpenSWR benchmark, you will need [Paraview with the SWR enabled](https://www.paraview.org/Wiki/ParaView/ParaView_And_Mesa_3D)

OSPRay rendering backend is embedded in Paraview 5.x, so you will only need [OSPray installed](http://www.ospray.org/downloads.html)

## Datasets

The datasets are described [SVBench: Scientific Visualization Benchmarking Suite websites](https://tacc.github.io/vis-workloads/) and can be downloaded from here (http://web.corral.tacc.utexas.edu/SVBench/)

## Downloading and configure test suite

SVBench configuration is done through CMake. You will be able to define the location of the several required binaries and the location of the datasets. We will also be able to define the test parameters (which benchmarks to run, number of nodes, number of task per node, Geometry size, etc...)


```
git clone https://github.com/TACC/vis-workloads.git svb
cd svb
mkdir build; cd build
ccmake ..
```

## Generating submissions scripts

SVBench was designed to be executed on cluster systems with SLURM. To generate the submission scripts for all the specific benchmark configurations run:

```
cd SVBench_root_path
./genAllBenchmarks.py
```

This script will generate the submission scripts under a benchmark folder.
```
benchmarks
└───fiu
│   └───swr
│   |   └───interactive
│   |   └───outs
│   |   └───submits
│   └───ospray
│   |   └───interactive
│   |   └───outs
│   |   └───submits
└───dns
│   └───swr
│   |   └───interactive
│   |   └───outs
│   |   └───submits
│   └───ospray
│   |   └───interactive
│   |   └───outs
│   |   └───submits
(...)
```

## Submitting indivual benchmark / configuration

Example to submit the fiu OpenSWR benchmark, with geometry level 1 in 32 Nodes with one task per node. (Actual configuration defined using the CMake procedure described above)

```
sbatch -A MY_PROJECT_ACCOUNT benchmarks/fiu/swr/submits/submit_dfiu_rswr_t1_N32_n1.sh
```

## Submitting multiple benchmarks

The python script nextSubmits.py will allow you to submit a collection of an individual benchmark. The scripts sorts all submission scripts found inside benchmarks and submits groups of them to the select SLURM queue. It memorizes the last job submitted and when called again submits the next N jobs in the list.

| option | description |
|--------|-------------|
| -l     | Limit of the SLURM submission queue (N) |
| -r     | Reset the submission sequence           |
| -R     | SLURM reservation name if available     |


Example submitting the 1st 25 jobs

```
./nextSubmits.py -r -l 25
```
Submitting the next 25 jobs

```
./nextSubmits.py
```

## TODO:
A few things are missing:
[ ] Make the submission job description less dependent on specific LMOD used by TACC
[ ] Adjust VMD test cases
