# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:39:25 2020
@author: Wesley Davis
"""
from netCDF4 import Dataset as dt
import numpy as np

# There are better ways, but let's make a list of possible months for now
mon_list = ['June', 'July', 'Aug', 'Sep']
# Actually, all you use it for is the filename, so let's make a
# list of months numbered for file names
mon_list = ['06', '07', '08', '09']
# June = glob('*06.grb2.nc')
# July = glob('*07.grb2.nc')
# Aug = glob('*08.grb2.nc')
# Sep = glob('*09.grb2.nc')


def GetMonthArray(file_name, min_lat, max_lat,
                  min_lon, max_lon, var='V_GRD_L100'):
    """
    This function takes the month and the data and stacks up
    all the arrays

    SIDENOTE: anyone hiring will really like a docstring like
              this for any functions on your github.
    SIDENOTE2: Notice there are no numbers hard coded into this
               function. That way you can call it from anywhere
               with any changes you want to make, like increasing
               the latitude
    SIDENOTE3: This is a good way to open a dataset like this
               because after this function runs, the dataset
               is not left in memory

    Parameters
    ----------
    file_name : str
        A three letter string for the month
    lat and long variables: integer
        These are the min and max latitude and longitude of
        interest in grid format
    var : str
        The NETCDF 4 variable name that you want to extract
        * Optional, it will use 'V_GRD_L100' if nothing is given

    Returns
    -------
    arr : numpy array
        3 dimensional numpy array of form:
            [4 * days in month, max_lat - min_lat, max_lon - min_lon]
        example for June is [120, 17, 11]
    """
    full_data = dt(file_name, 'r')
    chopped_data = np.array(full_data.variables[var][:,
                                                     min_lat:max_lat,
                                                     min_lon:max_lon])
    return chopped_data

# Anyone hiring by looking through your github, won't like
# any hard coded numbers. I can show you how to make it figure
# all of these by itself

# set first year of data
bgn_yr = 1979

# Set how many years
yrs = 27

# Set min, max lats and longs (are these still correct? MATLAB
#                              starts at 1 and python starts at 0)
min_lat = 150
max_lat = 167
min_lon = 670
max_lon = 681

# This is to initialize the variables
# I know Scott does it all the time, but
# it's really unnesessary
JUNE_ALL = np.zeros([120, max_lat - min_lat, max_lon - min_lon])
JULY_ALL = np.zeros([124, max_lat - min_lat, max_lon - min_lon])
AUG_ALL = np.zeros([124, max_lat - min_lat, max_lon - min_lon])
SEP_ALL = np.zeros([120, max_lat - min_lat, max_lon - min_lon])
# I wouldn't initialize them, because if you make functions
# that you will want to use with different datasets they might
# be different sizes. I will show you pandas soon, which will
# make all this easier, but for now let's leave it, but without
# the number of years.

for i in range(bgn_yr, bgn_yr + yrs):  # This will cycle through the years
    for j in mon_list:  # This will cycle through the months
        file_name = "wnd700.gdas.{}{}.grb2.nc".format(i, j)
        arr = GetMonthArray(file_name, min_lat, max_lat,
                            min_lon, max_lon)
        if j == '06':
            JUNE_ALL = np.stack((JUNE_ALL, arr), axis=4)
        if j == '07':
            JULY_ALL = np.stack((JULY_ALL, arr), axis=4)
        if j == '08':
            AUG_ALL = np.stack((AUG_ALL, arr), axis=4)
        if j == '09':
            SEP_ALL = np.stack((SEP_ALL, arr), axis=4)
