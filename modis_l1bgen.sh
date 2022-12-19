#!/bin/bash

# do modis_L1B.py to get L1B_file

inpath=$1
outpath=$2
files=$3
geofiles=${files%.*}".GEO"
l1bfiles=${files%.*}".L1B_LAC"
# echo $l1bfiles

#usage: modis_L1B [options] L1AFILE [GEOFILE]
#options: -o 1km-file ----- -k 0.5km-file  -x delete 1km; -y delete 500m; -z delete 250m --log save processing log

if [ ! -e $l1bfiles ]; then
	modis_L1B.py --okm=$libfiles $files $geofiles
fi
