#!/bin/bash
cd /opt/sharkshadows/cv/train-cascade
./init.sh
docker run --rm=true -it -v /opt/sharkshadows:/opt/sharkshadows elenaalexandrovna/opencv-python3 /opt/sharkshadows/cv/train-cascade/makesamples.sh
#./makesamples.sh
./merge.sh
scp sharky.vec jethro@data.sharkshadows.com:/opt/sharkshadows/cv/train-cascade
