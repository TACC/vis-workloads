#!/bin/python

import os
import sys
import re
import collections
import csv

from collections import namedtuple
from operator import itemgetter, attrgetter
from functools import cmp_to_key
from optparse import OptionParser


def parsefile(key, filename,searchlist):
    reglist = [];


    avg = [key] + [ "n/a" for i in range(0,len(searchlist)-1)]
    dev = [key] + [ "n/a" for i in range(0,len(searchlist)-1)]


    for exp in searchlist:
        reglist.append(re.compile(exp))

    with open(filename,'r') as file:

        for line in file:
            # print("{}\n".format(line))
            for i in range(0,len(reglist)):
                if(reglist[i].search(line)):
                    # print("Found {}".format(searchlist[i]))
                    values = re.findall(r"[-+]?\d*\.\d+|\d+",line)
                    avg[i] = values[0]
                    if(len(values) > 1):
                        dev[i] = values[1]

    return avg
    # print(" {},".format(len(avg)), end='')
    # for v in avg:
    #     print(" {},".format(v), end='')
    # print("\n", end='',flush=True)


def sortkeyfiles(item1, item2):
    key1 = item1[0]
    key2 = item2[0]
    if((key1.p) < (key2.p)):
        return -1
    if((key1.p) > (key2.p)):
        return 1
    if((key1.n) < (key2.n)):
        return -1
    if((key1.n) > (key2.n)):
        return 1
    if((key1.t) < (key2.t)):
        return -1
    if((key1.t) > (key2.t)):
        return 1
    return 0

def checkValid(key, n,p, t):
    if(n == -1 and p == -1 and t == -1):
        return True

    if(n != -1 and key.n != n) or ( p != -1 and key.p != p) or ( t != -1 and key.t != t):
        return False

    return True


def filterFiles(Files, n,p,t):
    return { k: v for k,v in Files if(checkValid(k,n,p,t))  }


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--directory",action="store",type="string", dest="directory", help="Directory to search")
    parser.add_option("-s", "--dataset",action="store",type="string", dest="dataset", help="Dataset name",default="fiu")

    (options, args) = parser.parse_args()
    searchlist = ["Run name ","numPoints:" , "numCells:", "numPolys:", "Memory:", "Page size:", "time to first frame:", "overall render time","still zoomed out","rotate zoomed out","zooming results","still zoomed in","rotate zoomed in","pv_reader time","pv_filter time"]

    FileData = namedtuple("FileData",["t","n","p"])

    Files = {}

    for file in os.listdir(options.directory):
        if file.find(options.dataset) != -1:
            tnp = re.findall(r"\d\d*",file)
            Files[FileData(t=int(tnp[0]),n=int(tnp[1]),p=int(tnp[2]))] = file;
            #print("Triangles: {} Nodes: {} Processes per node: {}".format(triangles_nodes_ppn[0],triangles_nodes_ppn[1],triangles_nodes_ppn[2]));

    Files = sorted(Files.items(),key=cmp_to_key(sortkeyfiles))

    NodesCounts = sorted({ k.n for k,v in Files })
    PerNodeCounts = sorted({ k.p for k,v in Files })
    TriangleCounts = sorted({ k.t for k,v in Files })

    #NODE NodeScaling
    searchlist[0] = "Node count"
    for tri in TriangleCounts:
        for ppn in PerNodeCounts:
            filterfiles = filterFiles(Files,-1,ppn,tri)
            filename = options.dataset + "_NS_PPN_"+str(ppn)+"_T_"+str(tri)+".csv"
            with open(filename,"w",newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(searchlist)
                for k,file in filterfiles.items():
                    writer.writerow(parsefile(k.n, os.path.join(options.directory,file),searchlist))

    #NODE Process Scaling
    searchlist[0] = "Per node process"
    for tri in TriangleCounts:
        for nodes in NodesCounts:
            filterfiles = filterFiles(Files,nodes,-1,tri)
            filename = options.dataset + "_PS_N_"+str(nodes)+"_T_"+str(tri)+".csv"
            with open(filename,"w",newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(searchlist)
                for k,file in filterfiles.items():
                    writer.writerow(parsefile(k.p,os.path.join(options.directory,file),searchlist))

    #NODE Triangles Scaling
    searchlist[0] = "Triangle count"
    for ppn in PerNodeCounts:
        for nodes in NodesCounts:
            filterfiles = filterFiles(Files,nodes,ppn,-1)
            filename = options.dataset + "_TS_N_"+str(nodes)+"_PPN_"+str(ppn)+".csv"
            with open(filename,"w",newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(searchlist)
                for k,file in filterfiles.items():
                    writer.writerow( parsefile(k.t, os.path.join(options.directory,file),searchlist))
