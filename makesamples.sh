#!/bin/bash
cd /opt/sharkshadows/cv/train-cascade
perl bin/createsamples.pl positives.txt negatives.txt samples 1500\
  "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
  -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 40 -h 40"
#python3 mergevec.py -v samples/ -o sharky.vec

