#!/bin/bash
export OCSSWROOT=/home/software/SeaDAS_9_1/ocssw
source $OCSSWROOT/OCSSW_bash.env

year=2024
for i in $(1 1 365) 
do
	ddd=$(echo $i | awk '{printf "%03d\n", $0 }')
	for j in $(seq 0 1 23)
       	do
		hh=$(echo $j|awk '{printf("%02d\n",$0)}')
		ehh=$(echo $((j+1))|awk '{printf("%02d\n",$0)}')
		modis_atteph -m aqua -s $year$ddd$hh'0000' -e $year$ddd$ehh'0000' --ancdir=./modisa_anc/ --verbose 
	done
done
