# Create cloud instance

## Single node

Create an instance using Ubuntu 16.04

#### Nvidia driver location
The previous script should install NVidia drivers, use it if you want to update the driver

http://download.nvidia.com/XFree86/Linux-x86_64/

### Install X and Nvidia driver

Edit configure.sh if you need to update the nvidia driver, (chaeck the previous url for the latest driver)

Or remove the driver install by commenting all lines with references to the driver.

```
git clone https://github.com/agisoft-llc/cloud-scripts
sh configure.sh
```

### Install SSHFS
https://www.hiroom2.com/2017/08/04/ubuntu-1604-sshfs-en/

### Install other required packages

```
sudo apt-get install mesa-utils cmake-curses-gui libxext-dev libx11-xcb-dev libxcb-dri2-0-dev libxcb-xfixes0-dev libexpat1-dev
```

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
source ~/vis-workloads/scripts/paraviewenv
mkdir build
ccmake ..
```
### Build OpenSWR/LLVMPIPE

```
cd $HOME
mkdir swr
cd swr
cp ~/vis-workload/scripts/buildswr .
```

Edit buildswr to match instance architecture. Search line:
```
   --with-swr-archs=avx,avx2,knl,skx \
```

```
./buildswr -ls

cd local/bin
cp ~/vis-workloads/scripts/llvmpipe .
cp ~/vis-workloads/scripts/swr .
chmod 755 llvmpipe
chmod 755 swr
```

### Enable swr
Edit vis-workloads/script/swrenv to match SWRPATH

```
source ~/vis-workloads/script/swrenv
```

### Execute benchmark

```
./execbenchmarks -l <exec batch size>
```
