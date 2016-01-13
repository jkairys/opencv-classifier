#!/usr/bin/python3
import os
from os.path import isfile, join

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

import argparse
parser = argparse.ArgumentParser(description='Build cascade classifier from dataset.')
parser.add_argument('--images', dest="dir", type=str, help='Directory containing master dataset')
parser.add_argument('--keyword', dest="keyword", type=str, help='Keyword to select images')
args = parser.parse_args()
args = vars(args)

logger.info("Image directory: %s", args["dir"])
logger.info("Keyword: %s", args["keyword"])

import os

import struct
import imghdr

from subprocess import call

def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return {"width": width, "height": height}

def get_filepaths(directory):
  """
  This function will generate the file names in a directory 
  tree by walking the tree either top-down or bottom-up. For each 
  directory in the tree rooted at directory top (including top itself), 
  it yields a 3-tuple (dirpath, dirnames, filenames).
  """
  file_paths = []  # List which will store all of the full filepaths.
  # Walk the tree.
  for root, directories, files in os.walk(directory):
    for filename in files:
      # Join the two strings in order to form the full filepath.
      filepath = os.path.join(root, filename)
      file_paths.append(filepath)  # Add it to the list.
  return file_paths  # Self-explanatory.

allfiles = get_filepaths(args["dir"])

pos = []
neg = []

positives = open("positives.txt",'w')
negatives = open("negatives.txt",'w')
info = open("info.txt",'w')
numPos = 0
numNeg = 0
for f in allfiles:
  test = f.replace(args["dir"],"")
  if(test.find(args["keyword"]) != -1):
    positives.write(f+"\n")
    dims = get_image_size(f)
    info.write(f+"\t1\t0 0 "+str(dims["width"])+" "+str(dims["height"])+"\n")
    numPos = numPos + 1
  else:
    negatives.write(f+"\n")
    numNeg = numNeg + 1

positives.close()
negatives.close()
info.close()

logger.info("-numPos=%s -numNeg=%s", numPos, numNeg)
call("opencv_createsamples -num "+str(numPos)+" -info info.txt -w 40 -h 40 -vec output.vec", shell=True)

