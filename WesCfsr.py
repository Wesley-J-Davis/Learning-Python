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

# This is a dictionary. It's one of the data types in python.
#  I am going to set a few definitions so it will be able
#  to loop through everything all at once.

#  Each month will be associated with a list of it's month
#  number and how many days it has
month_dict = {'Jan': ['01', 31],
              'Feb': ['02', 28],
              'Mar': ['03', 31],
              'Apr': ['04', 30],
              'May': ['05', 31],
              'Jun': ['06', 30],
              'Jul': ['07', 31],
              'Aug': ['08', 31],
              'Sep': ['09', 30],
              'Oct': ['10', 31],
              'Nov': ['11', 30],
              'Dec': ['12', 31]}
file_list = glob('./data/*.nc')

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
