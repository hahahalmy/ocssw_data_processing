#!/bin/bash

# do l2gen to get L1A_file

inpath=$1
outpath=$2
files=$3
geofiles=${files%.*}".GEO"
l1bfiles=${files%.*}".L1B_LAC"
l2afiles=${files%.*}".L2A_LAC_ZD"
#l2afiles=${files%.*}".L2A_LAC_STD"

if [ ! -e $l2afiles ]; then
	/home/dell/ocssw/build/src/l2gen/l2gen ifile=$l1bfiles geofile=$geofiles ofile=$l2afiles aer_opt=-9 aer_swir_short=1240 aer_swir_long=2130 cloud_thresh=0.037 cloud_wave=2130 resolution=500
	#/home/dell/ocssw/bin/l2gen ifile=$l1bfiles geofile=$geofiles ofile=$l2afiles aer_opt=-9 aer_swir_short=1240 aer_swir_long=2130 cloud_thresh=0.037 cloud_wave=2130 resolution=500
fi
