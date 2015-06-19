import visit
import os
import sys
#launchArguments = ("-par", "-np", "32","-l","ibrun")
launchArguments = ("-par","-np","1","-nn","1","-p","vis","-la","-V -cwd", "-l", "ibrun","-t","60")#,"-machinefile","longhorn")
batchHost = "localhost"
OpenComputeEngine("%s"%batchHost,launchArguments)
Source("/scratch/01336/carson/intelTACC/benchmarks/visit_scripts/visit_run.py")
