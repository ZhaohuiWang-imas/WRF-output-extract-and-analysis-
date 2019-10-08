#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:54:39 2019

@author: Zhaohui Wang
"""

from __future__ import print_function
from netCDF4 import Dataset
from wrf import getvar, ALL_TIMES
import scipy.io as sio  
import os
import numpy as np
import pandas as pd

    
from datetime import datetime
def datelist(beginDate, endDate):
    # beginDate, endDate是形如‘20160601’的字符串或datetime格式
    date_l=[datetime.strftime(x,'%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l

timeperiod1=['20180217','20180929','20180502','20181213','20180902']
timeperiod2=['20180227','20181009','20180512','20181223','20180912']
for tp in range(5):

    timeneed=datelist(timeperiod1[tp],timeperiod2[tp])
    
    os.chdir("/scratch/zhaohuiw/PWRF_non_staticseaice_ib/WRFV3/test/em_real")
    x = np.zeros((264,699,699))
    
    i=0
    for date in timeneed:
        filename='wrfout_d01_' + date + '_00:00:00' 
        ncfile = Dataset(filename)
    # Get the Sea Level Pressure
        slp = getvar(ncfile, "slp",timeidx=ALL_TIMES,meta=False)  #change the variable to what we need
        x[24*i:24*(i+1),:,:] = slp
        i=i+1
    del i 
    os.chdir("/scratch/zhaohuiw/wrf_variable")    
    sio.savemat('SLP_non_staticseaice_'+filename[11:21]+'.mat', {'slp': x}) # give x the variable name
    
    ###################################
    os.chdir("/scratch/zhaohuiw/PWRF_staticseaice_ib/WRFV3/test/em_real")
    x = np.zeros((264,699,699))
    
    i=0
    for date in timeneed:
        filename='wrfout_d01_' + date + '_00:00:00' 
        ncfile = Dataset(filename)
    # Get the Sea Level Pressure
        slp = getvar(ncfile, "slp",timeidx=ALL_TIMES,meta=False)
        x[24*i:24*(i+1),:,:] = slp
        i=i+1
    del i 
    os.chdir("/scratch/zhaohuiw/wrf_variable")    
    sio.savemat('SLP_staticseaice_'+filename[11:21]+'.mat', {'slp': x}) 
    
    ###################################
    os.chdir("/scratch/zhaohuiw/PWRF_staticseaice_sstupdate_ib/WRFV3/test/em_real")
    x = np.zeros((264,699,699))
    
    i=0
    for date in timeneed:
        filename='wrfout_d01_' + date + '_00:00:00' 
        ncfile = Dataset(filename)
    # Get the Sea Level Pressure
        slp = getvar(ncfile, "slp",timeidx=ALL_TIMES,meta=False)
        x[24*i:24*(i+1),:,:] = slp
        i=i+1
    del i 
    os.chdir("/scratch/zhaohuiw/wrf_variable")    
    sio.savemat('SLP_staticseaice_sstupdate_'+filename[11:21]+'.mat', {'slp': x}) 
    
    
    
