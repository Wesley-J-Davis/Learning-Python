# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from netCDF4 import Dataset as dt
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
#%%
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# lat_ts is the latitude of true scale.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='aqua')
plt.title("Mercator Projection")
plt.show()
#%%

JUNE_79 = 'wnd700.gdas.197906.grb2.nc'
JUNE_79 = dt(JUNE_79,'r')
#    JUNE_79=np.array(JUNE_79.variables['V_GRD_L100'][:]) 

JUNE_80 = 'wnd700.gdas.198006.grb2.nc'
JUNE_80 = dt(JUNE_80,'r')
#    JUNE_80=np.array(JUNE_80.variables['V_GRD_L100'][:]) 
    
JUNE_81 = 'wnd700.gdas.198106.grb2.nc'
JUNE_81 = dt(JUNE_81,'r')
#    JUNE_81=np.array(JUNE_81.variables['V_GRD_L100'][:]) 
    
JUNE_82 = 'wnd700.gdas.198206.grb2.nc'
JUNE_82 = dt(JUNE_82,'r')
#    JUNE_82=np.array(JUNE_82.variables['V_GRD_L100'][:]) 
    
JUNE_83 = 'wnd700.gdas.198306.grb2.nc'
JUNE_83 = dt(JUNE_83,'r')
#    JUNE_83=np.array(JUNE_83.variables['V_GRD_L100'][:]) 
    
JUNE_84 = 'wnd700.gdas.198406.grb2.nc'
JUNE_84 = dt(JUNE_84,'r')
#    JUNE_84=np.array(JUNE_84.variables['V_GRD_L100'][:]) 
  #%%  
    JUNE_85 = 'wnd700.gdas.198506.grb2.nc'
    JUNE_85 = dt(JUNE_85,'r')
    JUNE_85=np.array(JUNE_85.variables['V_GRD_L100'][:]) 
    
    JUNE_86 = 'wnd700.gdas.198606.grb2.nc'
    JUNE_86 = dt(JUNE_86,'r')
    JUNE_86=np.array(JUNE_86.variables['V_GRD_L100'][:]) 
    
    JUNE_87 = 'wnd700.gdas.198706.grb2.nc'
    JUNE_87 = dt(JUNE_87,'r')
    JUNE_87=np.array(JUNE_87.variables['V_GRD_L100'][:]) 
    
    JUNE_88 = 'wnd700.gdas.198806.grb2.nc'
    JUNE_88 = dt(JUNE_88,'r')
    JUNE_88=np.array(JUNE_88.variables['V_GRD_L100'][:]) 
    
    JUNE_89 = 'wnd700.gdas.198906.grb2.nc'
    JUNE_89 = dt(JUNE_89,'r')
    JUNE_89=np.array(JUNE_89.variables['V_GRD_L100'][:]) 
    
    JUNE_90 = 'wnd700.gdas.199006.grb2.nc'
    JUNE_90 = dt(JUNE_90,'r')
    JUNE_90=np.array(JUNE_90.variables['V_GRD_L100'][:]) 
    
    JUNE_91 = 'wnd700.gdas.199106.grb2.nc'
    JUNE_91 = dt(JUNE_91,'r')
    JUNE_91=np.array(JUNE_91.variables['V_GRD_L100'][:]) 
    
    JUNE_92 = 'wnd700.gdas.199206.grb2.nc'
    JUNE_92 = dt(JUNE_92,'r')
    JUNE_92=np.array(JUNE_92.variables['V_GRD_L100'][:]) 
    
    JUNE_93 = 'wnd700.gdas.199306.grb2.nc'
    JUNE_93 = dt(JUNE_93,'r')
    JUNE_93=np.array(JUNE_93.variables['V_GRD_L100'][:]) 
    
    JUNE_94 = 'wnd700.gdas.199406.grb2.nc'
    JUNE_94 = dt(JUNE_94,'r')
    JUNE_94=np.array(JUNE_94.variables['V_GRD_L100'][:]) 
    
    JUNE_95 = 'wnd700.gdas.199506.grb2.nc'
    JUNE_95 = dt(JUNE_95,'r')
    JUNE_95=np.array(JUNE_95.variables['V_GRD_L100'][:]) 
    
    JUNE_96 = 'wnd700.gdas.199606.grb2.nc'
    JUNE_96 = dt(JUNE_96,'r')
    JUNE_96=np.array(JUNE_96.variables['V_GRD_L100'][:]) 
    
    JUNE_97 = 'wnd700.gdas.199706.grb2.nc'
    JUNE_97 = dt(JUNE_97,'r')
    JUNE_97=np.array(JUNE_97.variables['V_GRD_L100'][:]) 
    
    JUNE_98 = 'wnd700.gdas.199806.grb2.nc'
    JUNE_98 = dt(JUNE_98,'r')
    JUNE_98=np.array(JUNE_98.variables['V_GRD_L100'][:]) 
    
    JUNE_99 = 'wnd700.gdas.199906.grb2.nc'
    JUNE_99 = dt(JUNE_99,'r')
    JUNE_99=np.array(JUNE_99.variables['V_GRD_L100'][:]) 
    
    JUNE_00 = 'wnd700.gdas.200006.grb2.nc'
    JUNE_00 = dt(JUNE_00,'r')
    JUNE_00=np.array(JUNE_00.variables['V_GRD_L100'][:]) 
    
    JUNE_01 = 'wnd700.gdas.200106.grb2.nc'
    JUNE_01 = dt(JUNE_01,'r')
    JUNE_01=np.array(JUNE_01.variables['V_GRD_L100'][:]) 
    
    JUNE_02 = 'wnd700.gdas.200206.grb2.nc'
    JUNE_02 = dt(JUNE_02,'r')
    JUNE_02=np.array(JUNE_02.variables['V_GRD_L100'][:]) 
    
    JUNE_03 = 'wnd700.gdas.200306.grb2.nc'
    JUNE_03 = dt(JUNE_03,'r')
    JUNE_03=np.array(JUNE_03.variables['V_GRD_L100'][:]) 
    
    JUNE_04 = 'wnd700.gdas.200406.grb2.nc'
    JUNE_04 = dt(JUNE_04,'r')
    JUNE_04=np.array(JUNE_04.variables['V_GRD_L100'][:]) 
    
    JUNE_05 = 'wnd700.gdas.200506.grb2.nc'
    JUNE_05 = dt(JUNE_05,'r')
    JUNE_05=np.array(JUNE_05.variables['V_GRD_L100'][:]) 
#%%
JUNE_ALL = [
    JUNE_79,
    JUNE_80,
    JUNE_81,
    JUNE_82,
    JUNE_83,
    JUNE_84,
 ] 
#%%   
    JUNE_85, 
    JUNE_86,
    JUNE_87,
    JUNE_88,
    JUNE_89,
    JUNE_90,
    JUNE_91,
    JUNE_92,
    JUNE_93,
    JUNE_94,
    JUNE_95,
    JUNE_96,
    JUNE_97,
    JUNE_98,
    JUNE_99,
    JUNE_00,
    JUNE_01,
    JUNE_02,
    JUNE_03,
    JUNE_04,
    JUNE_05,
    ]
#%%
V_JUNE_ALL = np.zeros([120,17,11,5])
#%%
i=[0,1,2,3,4,5]
for i in JUNE_ALL:
        dummy = JUNE_ALL[i]
        dummy=np.array(dummy.variables['V_GRD_L100'][:,150:167,670:681])
        V_JUNE_ALL[:,:,:,:] = dummy
    
#%%
ncfile=dt(JUNE_79,'r')
print (ncfile.variables)
#%%

lon=np.array(ncfile.variables['lon'][:],dtype=np.float32) 
# .5 degree resolution [0 359.5] East longitude [:]= ALL OBJECTS dtype = datatype
lat=np.array(ncfile.variables['lat'][:],dtype=np.float32) 
# .5 degree resolution [90  -90] north to south
time=np.array(ncfile.variables['time'][:],dtype=np.float32) 
# 30 days, 4 times per day 
validtime=np.array(ncfile.variables['valid_date_time'][:]) 
# 
referencetime=np.array(ncfile.variables['ref_date_time'][:]) 
#
fcsthour=np.array(ncfile.variables['forecast_hour'][:]) 
#
V_GRD_L100=np.array(ncfile.variables['V_GRD_L100'][:]) 
# v wind 4 times a day for 30 days at each .5 degree interval (lat/long) globally
