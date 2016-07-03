#! /usr/bin/env python


import os
import sys

if len(sys.argv) < 3:
    print("please check your parameter")
    exit(-1)

soFile = sys.argv[1]
dmpFile = sys.argv[2]

print soFile,
print dmpFile

symFile = soFile + ".sym"

#dumple sym file
os.system("./dump_syms " + soFile  + " > " + symFile)

#get directory information
ret = os.popen("head -n1 " + symFile).read()
arry = ret.strip().split(" ")
dirName = arry[3]
symPath = "./symbols/" + soFile + "/" + dirName

#create directory
os.system("mkdir -p " + symPath)
os.system("mv " + symFile + " " + symPath)

#minidump to log file
os.system("./minidump_stackwalk " + dmpFile + " ./symbols > crashlog")

