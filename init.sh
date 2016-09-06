#!/bin/bash
IMAGES="/opt/sharkshadows/img/samples"

rm positives.txt
rm negatives.txt
php posdims.php > info.txt
find $IMAGES -iname "*.jpg" | grep "shark/" > positives.txt
find $IMAGES -iname "*.jpg" | grep -v "shark/" > negatives.txt
wc -l info.txt
