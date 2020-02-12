# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:39:25 2020

@author: Wesley Davis
"""
from netCDF4 import Dataset as dt
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
#%%
June = glob('*06.grb2.nc')
July = glob('*07.grb2.nc')
Aug = glob('*08.grb2.nc')
Sep = glob('*09.grb2.nc')
JUNE_ALL = np.zeros([120,17,11,27])
JULY_ALL = np.zeros([124,17,11,27])
AUG_ALL = np.zeros([124,17,11,27])
SEP_ALL = np.zeros([120,17,11,27])
#%%
for i in range(len(June)):
    dummy = June[i]
    dummy = dt(dummy,'r')
    dummy=np.array(dummy.variables['V_GRD_L100'][:,150:167,670:681])
    JUNE_ALL[:,:,:,i] = dummy
for i in range(len(July)):
    dummy = July[i]
    dummy = dt(dummy,'r')
    dummy=np.array(dummy.variables['V_GRD_L100'][:,150:167,670:681])
    JULY_ALL[:,:,:,i] = dummy   
for i in range(len(Aug)):
    dummy = Aug[i]
    dummy = dt(dummy,'r')
    dummy=np.array(dummy.variables['V_GRD_L100'][:,150:167,670:681])
    AUG_ALL[:,:,:,i] = dummy  
for i in range(len(Sep)):
    dummy = Sep[i]
    dummy = dt(dummy,'r')
    dummy=np.array(dummy.variables['V_GRD_L100'][:,150:167,670:681])
    SEP_ALL[:,:,:,i] = dummy
#%%
