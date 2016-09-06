#!/bin/bash
cd /opt/sharkshadows/cv/train-cascade
opencv_traincascade -data classifier -vec sharky.vec -bg negatives.txt  -numStages 20 -minHitRate 0.99 -maxFalseAlarmRate 0.4 -numPos 50 -numNeg 600 -w 40 -h 40 -mode ALL -precalcValBufSize 4096  -precalcIdxBufSize 4096

