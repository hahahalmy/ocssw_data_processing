#!/bin/bash

# do modis_geo.py to get GEO_file

inpath=$1
outpath=$2
files=$3
geofiles=${files%.*}".GEO"

#echo $geofiles
if [ ! -e $geofiles ]; then
	modis_GEO.py -o $geofiles $files
fi
