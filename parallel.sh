#!/bin/bash

thread=20
filelist=filelist.txt
inpath=/home/dell/zhujiang/
outpath=/home/dell/zhujiang/
files=$(find $inpath -name "*.L1B_LAC")

#parallel --joblog ./l2gen.log --j $thread --eta ./modis_l2gen.sh $inpath $outpath {} ::: $files
#parallel --j $thread --eta ./modis_geo.sh $inpath $outpath {} ::: $files
#parallel --j $thread --eta ./modis_l1bgen.sh $inpath $outpath {} ::: $files
#parallel --j $thread --eta ./L1B_replace_satuated_rrs2.py {} ::: $files
parallel --joblog ./l2gen.log --j $thread --eta ./modis_l2gen.sh $inpath $outpath {} ::: $files
