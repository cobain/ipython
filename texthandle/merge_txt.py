#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import csv

source_dir = "gtfs"
output_dir = "output"


def delete_file_folder(src):
    '''delete files and folders'''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src,item)
            delete_file_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass


delete_file_folder(output_dir)
os.mkdir(output_dir)

sub_dirs = os.listdir(source_dir)
for subdir in sub_dirs:

    if subdir.startswith(".DS_Store"):
        continue

    googledir = source_dir + "/" + subdir + "/google_transit"
    files = os.listdir(googledir)

    print files

    for txt_file in files:
        f = open(googledir + "/" + txt_file)
        content = f.read()

        merge = open(output_dir + "/" + txt_file, "a")
        merge.write(content + "\n")

        f.close()
        merge.close()




