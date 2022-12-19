#!/bin/bash

Nproc=4
Pfifo="/tmp/$$.fifo"
mkfifo $Pfifo
exec 6<>$Pfifo

rm -f $Pfifo

for((i=1; i<=$Nproc; i++));do
	echo
done >&6

for file in /home/dell/taihu/*.L1B_LAC
do
	read -u6
	{
		temp_file=`basename $file`
		temp_file_name=${temp_file:0:14}
		GEOFILE=$temp_file_name.GEO
		L1AFILE=$temp_file_name.L1A_LAC
		#modis_GEO.py -o ${GEOFILE} ${L1AFILE}
		L1BFILE=$temp_file_name.L1B_LAC
		L2AFILE=$temp_file_name.L2A_std_500M
		#modis_L1B.py -o $L1BFILE $L1AFILE $GEOFILE
		#./L1B_replace_satuated_rrs2.py $L1BFILE
		l2gen ifile=$L1BFILE geofile=$GEOFILE ofile=$L2AFILE aer_opt=-9 aer_swir_short=1240 aer_swir_long=2130 cloud_thresh=0.037 cloud_wave=2130 resolution=500
		sleep 2
		echo >&6
	} &
	
done
wait
exec 6>&-
echo "done!"
