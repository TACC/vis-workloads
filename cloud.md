# Create cloud instance

## Single node

Create an instance using Ubuntu 16.04

### Install X and Nvidia driver

```
git clone https://github.com/agisoft-llc/cloud-scripts
sh configure.sh
```

#### Nvidia driver location
http://download.nvidia.com/XFree86/Linux-x86_64/


### Install SSHFS
https://www.hiroom2.com/2017/08/04/ubuntu-1604-sshfs-en/

### Install Paraview 5.4.1

Copy paraview 5.4.1 to the instance

```
tar xzf Paraview*.tar.gz
mv Paraview-5.4.1[...] paraview


git clone https://github.com/TACC/vis-workloads.git
cd vis-workloads
git checkout aws
sshfs -o ro <username>@data.tacc.utexas.edu:/corral-repl/tacc/vis_data/benchmarks data

```

Edit paraviewenv and change PARAVIEWPATH

```
source paraviewenv
mkdir build
ccmake ..
```

### Execute benchmark

```
./execbenchmarks -l <exec batch size>
```
