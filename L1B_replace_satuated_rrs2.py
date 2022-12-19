#!/usr/bin/python

import sys
import numpy as np
from pyhdf.SD import SD,SDC

fname=sys.argv[1]
#open hdf file, and find the data id
tag_name = 'EV_1KM_RefSB'
sdID=SD(fname,SDC.WRITE|SDC.READ)
#try:
	#sdsID=sdID.select(tag_name)
#except:
	#print(fname)
sdsID=sdID.select(tag_name)
kmdata=sdsID.get()
#change the sateratued pixel values in the old data
kmjunk=np.where(kmdata>65500)
kmjunk_count=np.size(kmjunk)
if kmjunk_count>0:
	kmdata[kmjunk]=317
sdsID[:,:]=kmdata
sdsID.endaccess()
sdID.end()
