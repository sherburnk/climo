#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:12:02 2022

@file: climoplots_config.py
@author: Keith Sherburn
"""

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib.colors
import pytz

wfoloc = 'Rapid City, SD'
wfocty = 'Rapid City'
wfourl = 'weather.gov/unr'

fontfam = 'Nimbus Sans'
# Options (at least on UNR's server): 
# ['URW Bookman', 'Cantarell', 'Nimbus Sans', 'Nimbus Mono PS', 'Nimbus Sans Narrow', 'Nimbus Roman', 'P052', 'C059', 'DejaVu Sans Mono', 'URW Gothic', 'Z003']
#    see examples on Google Drive

## Time Zone
## uncomment appropriate line
#tz = pytz.timezone('America/New_York') # Eastern
#tz = pytz.timezone('America/Chicago') # Central
tz = pytz.timezone('America/Denver') # Mountain
#tz = pytz.timezone'America/Phoenix') # MST always, like AZ
#tz = pytz.timezone('America/Los_Angeles') # Pacific
#tz = pytz.timezone('America/Anchorage') # Alaska
#tz = pytz.timezone('Pacific/Honolulu') # Hawaii

# Years (for previous year graphics; otherwise ignored)
years = [2022, 2023]

#logo = plt.imread('nwslogo.png')
#maxtim = plt.imread('maxt.png')
#mintim = plt.imread('mint.png')
#pcpnim = plt.imread('pcpn.png')
#snowim = plt.imread('snow.png')
#noaaim = plt.imread('noaa.png')
#nwsim = plt.imread('nws.png')

spectcmap = plt.cm.nipy_spectral
spectcmap.set_bad(color='w')

bugncmap = plt.cm.BuGn
brbgcmap = plt.cm.BrBG
pubucmap = plt.cm.PuBu
ylorbrcmap = plt.cm.YlOrBr
puorcmap = plt.cm.PuOr
rdburcmap = plt.cm.RdBu_r

bugncmap.set_bad(color='lightgrey')
bugncmap.set_under(color='blanchedalmond')
brbgcmap.set_bad(color='lightgrey')
pubucmap.set_bad(color='lightgrey')
pubucmap.set_under(color='blanchedalmond')
ylorbrcmap.set_bad(color='lightgrey')
puorcmap.set_bad(color='lightgrey')
rdburcmap.set_bad(color='lightgrey')

# Temperature colormap
norm = matplotlib.colors.Normalize(-60,120)

colors = [[norm(-60.0), [145./255.,0.,63./255.]],
          [norm(-55.0), [206./255.,18./255.,86./255.]],
          [norm(-50.0), [231./255.,41./255.,138./255.]],
          [norm(-45.0), [223./255.,101./255.,176./255.]],
          [norm(-40.0), [1.,115./255.,223./255.]],
          [norm(-35.0), [1.,190./255.,232./255.]],
          [norm(-30.0), [1.,1.,1.]],
          [norm(-25.0), [218./255.,218./255.,235./255.]],
          [norm(-20.0), [188./255.,189./255.,220./255.]],
          [norm(-15.0), [158./255.,154./255.,200./255.]],
          [norm(-10.0), [117./255.,107./255.,177./255.]],
          [norm(-5.0), [84./255.,39./255.,143./255.]],
          [norm(0.0), [13./255.,0.,125./255.]],
          [norm(5.0), [13./255.,61./255.,156./255.]],
          [norm(10.0), [0.,102./255.,194./255.]],
          [norm(15.0), [41./255.,158./255.,1.]],
          [norm(20.0), [74./255.,199./255.,1.]],
          [norm(25.0), [115./255.,215./255.,1.]],
          [norm(30.0), [173./255.,1.,1.]],
          [norm(35.0), [48./255.,207./255.,194./255.]],
          [norm(40.0), [0.,153./255.,150./255.]],
          [norm(45.0), [18./255.,87./255.,87./255.]],
          [norm(50.0), [6./255.,109./255.,44./255.]],
          [norm(55.0), [49./255.,163./255.,84./255.]],
          [norm(60.0), [116./255.,196./255.,118./255.]],
          [norm(65.0), [161./255.,217./255.,155./255.]],
          [norm(70.0), [211./255.,1.,190./255.]],
          [norm(75.0), [1.,1.,179./255.]],
          [norm(80.0), [1.,237./255.,160./255.]],
          [norm(85.0), [254./255.,209./255.,118./255.]],
          [norm(90.0), [254./255.,174./255.,42./255.]],
          [norm(95.0), [253./255.,141./255.,60./255.]],
          [norm(100.0), [252./255.,78./255.,42./255.]],
          [norm(105.0), [227./255.,26./255.,28./255.]],
          [norm(110.0), [177./255.,0.,38./255.]],
          [norm(115.0), [128./255.,0.,38./255.]],
          [norm(120.0), [89./255.,0.,66./255.]]]

tcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Wind gust colormap
norm = matplotlib.colors.Normalize(0,140)

colors = [[norm(0.0), [16./255.,63./255.,120./255.]],
          [norm(5.0), [34./255.,94./255.,168./255.]],
          [norm(10.0), [29./255.,145./255.,192./255.]],
          [norm(15.0), [65./255.,182./255.,196./255.]],
          [norm(20.0), [127./255.,205./255.,187./255.]],
          [norm(25.0), [180./255.,215./255.,158./255.]],
          [norm(30.0), [223./255.,1.,158./255.]],
          [norm(35.0), [1.,1.,166./255.]],
          [norm(40.0), [1.,232./255.,115./255.]],
          [norm(45.0), [1.,196./255.,0.]],
          [norm(50.0), [1.,170./255.,0.]],
          [norm(60.0), [1.,89./255.,0.]],
          [norm(70.0), [1.,0.,0.]],
          [norm(80.0), [168./255.,0.,0.]],
          [norm(100.0), [110./255.,0.,0.]],
          [norm(120.0), [1.,190./255.,232./255.]],
          [norm(140.0), [1.,115./255.,223./255.]]]

gcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

dnorm = matplotlib.colors.Normalize(-60,80)

dcolors = [[dnorm(-60.0), [1.,0.,0.]],
          [dnorm(-0.01), [59./255.,34./255.,4./255.]],
          [dnorm(0.0), [84./255.,48./255.,5./255.]],
          [dnorm(10.0), [140./255.,82./255.,10./255.]],
          [dnorm(20.0), [191./255.,129./255.,45./255.]],
          [dnorm(30.0), [204./255.,168./255.,84./255.]],
          [dnorm(40.0), [223./255.,194./255.,125./255.]],
          [dnorm(45.0), [230./255.,217./255.,181./255.]],
          [dnorm(50.0), [211./255.,235./255.,231./255.]],
          [dnorm(55.0), [169./255.,219./255.,211./255.]],
          [dnorm(60.0), [114./255.,184./255.,173./255.]],
          [dnorm(65.0), [49./255.,140./255.,133./255.]],
          [dnorm(70.0), [1./255.,102./255.,95./255.]],
          [dnorm(75.0), [0.,60./255.,48./255.]],
          [dnorm(80.0), [0.,41./255.,33./255.]]]

dcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", dcolors)

tcmap.set_bad(color='lightgrey')
gcmap.set_bad(color='lightgrey')
dcmap.set_bad(color='lightgrey')

# Element dictionary for records
elems_rec = {'maxtmp': {'id': 'maxtmp', 'title': 'Record High Daily Max Temperatures', 
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 'val': 1, 'col': 'b',
                    'reclab': 'Max'},
         'mintmp': {'id': 'mintmp', 'title': 'Record Low Daily Min Temperatures',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 'val': 2, 'col': 'r',
                    'reclab': 'Min'},
         'hmntmp': {'id': 'hmntmp', 'title': 'Record High Daily Min Temperatures',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 'val': 2, 'col': 'b',
                    'reclab': 'High Min'},
         'lmxtmp': {'id': 'lmxtmp', 'title': 'Record Low Daily Max Temperatures',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 'val': 1, 'col': 'r',
                    'reclab': 'Low Max'},
         'maxpcp': {'id': 'maxpcp', 'title': 'Record High Daily Precipitation',
                    'unit': 'inches', 'label': 'Precipitation (inches)', 'val': 3, 'col': 'r', 
                    'reclab': 'Precip'},
         'maxsnw': {'id': 'maxsnw', 'title': 'Record High Daily Snowfall',
                    'unit': 'inches', 'label': 'Snowfall (inches)', 'val': 4, 'col': 'r',
                    'reclab': 'Snowfall'},
         'maxavg': {'id': 'maxavg', 'title': 'Record High Daily Avg Temperatures',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 'val': 5, 'col': 'r',
                    'reclab': 'High Avg'},
         'minavg': {'id': 'minavg', 'title': 'Record Low Daily Avg Temperatures',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 'val': 5, 'col': 'b',
                    'reclab': 'Low Avg'},
#         'maxrng': {'id': 'maxrng', 'title': 'Record Daily Temperature Range',
#                    'unit': 'degrees', 'label': 'Range (degrees Fahrenheit)', 'val': 4, 'col': 'b'}
        }

# Element dictionary for averages
elems_avg = {'avgmax': {'id': 'avgmax', 'title': 'Average Daily Max Temperatures', 
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'dfile': 'dly-tmax-normal.txt', 'mfile': 'mly-tmax-normal.txt',
                    'col': 'b', 'aname': 'maxt'},
         'avgmin': {'id': 'avgmin', 'title': 'Average Daily Min Temperatures',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'dfile': 'dly-tmin-normal.txt', 'mfile': 'mly-tmin-normal.txt',
                    'col': 'r', 'aname': 'mint'},
         'avgavg': {'id': 'avgavg', 'title': 'Average Daily Mean Temperatures',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'dfile': 'dly-tavg-normal.txt', 'mfile': 'mly-tavg-normal.txt',
                    'col': 'r', 'aname': 'avgt'},
         'avgpcp': {'id': 'avgpcp', 'title': 'Average Daily Precipitation',
                    'unit': 'inches', 'label': 'Precipitation (inches)', 
                    'dfile': 'dly-prcp-50pctl.txt', 'mfile': 'mly-prcp-normal.txt',
                    'col': 'r', 'aname': 'pcpn'}, 
         'avgsnw': {'id': 'avgsnw', 'title': 'Average Daily Snowfall',
                    'unit': 'inches', 'label': 'Snowfall (inches)', 
                    'dfile': 'dly-snow-50pctl.txt', 'mfile': 'mly-snow-normal.txt',
                    'col': 'r', 'aname': 'snow'},
        }

# Element dictionary for YTD obs
elems_ytd = {'ytdmax': {'id': 'ytdmax', 'title': 'Daily Max Temperature', 
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'dfile': 'dly-tmax-normal.txt', 'mfile': 'mly-tmax-normal.txt',
                    'col': 'b', 'aname': 'maxt', 'cmap': 'tcmap', 'red': 'mean'},
         'ytdmin': {'id': 'ytdmin', 'title': 'Daily Min Temperature',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'dfile': 'dly-tmin-normal.txt', 'mfile': 'mly-tmin-normal.txt',
                    'col': 'r', 'aname': 'mint', 'cmap': 'tcmap', 'red': 'mean'},
         'ytdavg': {'id': 'ytdavg', 'title': 'Daily Mean Temperature',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'dfile': 'dly-tavg-normal.txt', 'mfile': 'mly-tavg-normal.txt',
                    'col': 'r', 'aname': 'avgt', 'cmap': 'tcmap', 'red': 'mean'},
         'ytdpcp': {'id': 'ytdpcp', 'title': 'Year-to-Date Precipitation',
                    'unit': 'inches', 'label': 'Precipitation (inches)', 
                    'dfile': 'dly-prcp-50pctl.txt', 'mfile': 'mly-prcp-normal.txt',
                    'col': 'r', 'aname': 'pcpn', 'cmap': plt.cm.BuGn, 'red': 'sum'}, 
         'ytdsnw': {'id': 'ytdsnw', 'title': 'Year-to-Date Snowfall',
                    'unit': 'inches', 'label': 'Snowfall (inches)', 
                    'dfile': 'dly-snow-50pctl.txt', 'mfile': 'mly-snow-normal.txt',
                    'col': 'r', 'aname': 'snow', 'cmap': plt.cm.PuBu, 'red': 'sum'},
        }

# Element dictionary for YTD table plots
elems_ydt = {'ytdmax': {'id': 'ytdmax', 'title': 'Daily Max Temperature', 
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'col': 'b', 'aname': 'maxt', 'cmap': tcmap, 'val': 6,
                    'jval': 6, 'vmin': -60, 'vmax': 120},
         'ytdmin': {'id': 'ytdmin', 'title': 'Daily Min Temperature',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'col': 'r', 'aname': 'mint', 'cmap': tcmap, 'val': 4,
                    'jval': 4, 'vmin': -60, 'vmax': 120},
         'ytdavg': {'id': 'ytdmin', 'title': 'Daily Average Temperature',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'col': 'r', 'aname': 'avgt', 'cmap': tcmap, 'val': 15,
                    'jval': 15, 'vmin': -60, 'vmax': 120},
         'ytdmxd': {'id': 'ytdmxd', 'title': 'Daily Max Dew Point',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'col': 'r', 'aname': 'dewp', 'cmap': dcmap, 'val': 35,
                    'jval': 35, 'vmin': -60, 'vmax': 80},
         'ytdpcp': {'id': 'ytdpcp', 'title': 'Daily Precipitation',
                    'unit': 'inches', 'label': 'Precipitation (inches)', 
                    'col': 'r', 'aname': 'pcpn', 'cmap': bugncmap, 'val': 3,
                    'jval': 14, 'lab': 'pcpn', 'vmin': 0.000001, 'vmax': 2.00}, 
         'ytdsnw': {'id': 'ytdsnw', 'title': 'Daily Snowfall',
                    'unit': 'inches', 'label': 'Snowfall (inches)', 
                    'col': 'r', 'aname': 'snow', 'cmap': pubucmap, 'val': 5,
                    'jval': 5, 'lab': 'snow', 'vmin': 0.000001, 'vmax': 12},
         'ytdsnd': {'id': 'ytdsnd', 'title': 'Daily Snow Depth',
                    'unit': 'inches', 'label': 'Snow Depth (inches)', 
                    'col': 'r', 'aname': 'snwd', 'cmap': pubucmap, 'val': 6,
                    'jval': 6, 'lab': 'snwd', 'vmin': 0.000001, 'vmax': 12},
         'ytdpkw': {'id': 'ytdpkw', 'title': 'Daily Peak Wind Speed',
                    'unit': 'mph', 'label': 'Peak Wind (mph)', 
                    'col': 'r', 'aname': 'pkwd', 'cmap': gcmap, 'val': 1,
                    'jval': 1, 'vmin': 0, 'vmax': 140},
        }

# Element dictionary for YTD line plots
# Also need records csvs
elems_ydl = {
         'ytdmax': {'id': 'maxstd', 'title': 'Daily Max Temps', 
             'unit': 'degrees', 'label': 'Temperature (degrees Fahrenheit)', 'val': 1, 'xcol': 'r', 'ncol': 'b',
             'xreclab': 'maxtmp', 'nreclab': 'lmxtmp', 'aname': 'maxt', 'vmin': -15, 'vmax': 110, 'lw': 1},
         'ytdmin': {'id': 'minstd', 'title': 'Daily Min Temps',
             'unit': 'degrees', 'label': 'Temperature (degrees Fahrenheit)', 'val': 2, 'xcol': 'r', 'ncol': 'b',
             'xreclab': 'hmntmp', 'nreclab': 'mintmp', 'aname': 'mint', 'vmin': -40, 'vmax': 85, 'lw': 1},
         'ytdavg': {'id': 'avgstd', 'title': 'Daily Average Temps',
             'unit': 'degrees', 'label': 'Temperature (degrees Fahrenheit)', 'val': 5, 'xcol': 'r', 'ncol': 'b',
             'xreclab': 'maxavg', 'nreclab': 'minavg', 'aname': 'avgt', 'vmin': -30, 'vmax': 95, 'lw': 1},
         'ytdpcp': {'id': 'pcpstd', 'title': 'Daily Precipitation', 
             'unit': 'inches', 'label': 'Precipitation (inches)', 'val': 3, 'xcol': 'g', 'ncol': 'orange',
             'xreclab': 'maxpcp', 'nreclab': 'minpcp', 'aname': 'pcpn', 'vmin': 0, 'vmax': 40, 'lw': 3},
         'ytdsnw': {'id': 'snwstd', 'title': 'Daily Snowfall',
             'unit': 'inches', 'label': 'Snowfall (inches)', 'val': 4, 'xcol': 'b', 'ncol': 'orange',
             'xreclab': 'maxsnw', 'nreclab': 'minsnw', 'aname': 'snow', 'vmin': 0, 'vmax': 100, 'lw': 3},
         }

elems_ylp = {
         'ytdpcp': {'id': 'pcpstd', 'aname': 'pcpn', 'title': 'Daily Precipitation'},
         'ytdsnw': {'id': 'snwstd', 'aname': 'snow', 'title': 'Daily Snowfall'}
         }
         
# Element dictionary for departures
elems_dep = {'depmax': {'id': 'depmax', 'title': 'Daily Max Temp Departure', 
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'dfile': 'dly-tmax-normal.txt', 'mfile': 'mly-tmax-normal.txt',
                    'col': 'b', 'aname': 'maxt'},
         'depmin': {'id': 'depmin', 'title': 'Daily Min Temp Departure',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'dfile': 'dly-tmin-normal.txt', 'mfile': 'mly-tmin-normal.txt',
                    'col': 'r', 'aname': 'mint'},
         'depavg': {'id': 'depavg', 'title': 'Daily Mean Temp Departure',
                    'unit': 'degrees', 'label': 'Temperature (Fahrenheit)', 
                    'dfile': 'dly-tavg-normal.txt', 'mfile': 'mly-tavg-normal.txt',
                    'col': 'r', 'aname': 'avgt'},
         'deppcp': {'id': 'deppcp', 'title': 'Daily Precip Departure',
                    'unit': 'inches', 'label': 'Precipitation (inches)', 
                    'dfile': 'dly-prcp-50pctl.txt', 'mfile': 'mly-prcp-normal.txt',
                    'col': 'r', 'aname': 'pcpn'}, 
         'depsnw': {'id': 'depsnw', 'title': 'Daily Snowfall Departure',
                    'unit': 'inches', 'label': 'Snowfall (inches)', 
                    'dfile': 'dly-snow-50pctl.txt', 'mfile': 'mly-snow-normal.txt',
                    'col': 'r', 'aname': 'snow'},
        }

# Element dictionary for 10-day departures
elems_d10 = {'depmax': {'id': 'depmax', 'title': 'Max Temp Departure, Last 10 Days', 
                    'unit': 'degrees', 'label': 'Temperature Departure (Fahrenheit)', 
                    'dfile': 'dly-tmax-normal.txt', 'mfile': 'mly-tmax-normal.txt',
                    'col': 'b', 'aname': 'maxt'},
         'depmin': {'id': 'depmin', 'title': 'Min Temp Departure, Last 10 Days',
                    'unit': 'degrees', 'label': 'Temperature Departure (Fahrenheit)', 
                    'dfile': 'dly-tmin-normal.txt', 'mfile': 'mly-tmin-normal.txt',
                    'col': 'r', 'aname': 'mint'},
         'depavg': {'id': 'depavg', 'title': 'Mean Temp Departure, Last 10 Days',
                    'unit': 'degrees', 'label': 'Temperature Departure (Fahrenheit)', 
                    'dfile': 'dly-tavg-normal.txt', 'mfile': 'mly-tavg-normal.txt',
                    'col': 'r', 'aname': 'avgt'},
         'deppcp': {'id': 'deppcp', 'title': 'Precip Departure, Last 10 Days',
                    'unit': 'inches', 'label': 'Precipitation Departure (inches)', 
                    'dfile': 'dly-prcp-50pctl.txt', 'mfile': 'mly-prcp-normal.txt',
                    'col': 'r', 'aname': 'pcpn'}, 
        }

# Element dictionary for 30-day departures
elems_d30 = {'depmax': {'id': 'depmax', 'title': 'Max Temperature Departure from Normal, Last 30 Days', 
                    'unit': 'degrees', 'label': 'Temperature Departure (Fahrenheit)', 
                    'dfile': 'dly-tmax-normal.txt', 'mfile': 'mly-tmax-normal.txt',
                    'col': 'b', 'aname': 'maxt'},
         'depmin': {'id': 'depmin', 'title': 'Min Temperature Departure from Normal, Last 30 Days',
                    'unit': 'degrees', 'label': 'Temperature Departure (Fahrenheit)', 
                    'dfile': 'dly-tmin-normal.txt', 'mfile': 'mly-tmin-normal.txt',
                    'col': 'r', 'aname': 'mint'},
         'depavg': {'id': 'depavg', 'title': 'Mean Temperature Departure from Normal, Last 30 Days',
                    'unit': 'degrees', 'label': 'Temperature Departure (Fahrenheit)', 
                    'dfile': 'dly-tavg-normal.txt', 'mfile': 'mly-tavg-normal.txt',
                    'col': 'r', 'aname': 'avgt'},
         'deppcp': {'id': 'deppcp', 'title': 'Precipitation Departure from Normal, Last 30 Days',
                    'unit': 'inches', 'label': 'Precipitation Departure (inches)', 
                    'dfile': 'dly-prcp-50pctl.txt', 'mfile': 'mly-prcp-normal.txt',
                    'col': 'r', 'aname': 'pcpn'}, 
        }

# Element dictionary for 90-day departures
elems_d90 = {'depmax': {'id': 'depmax', 'title': 'Max Temperature Departure from Normal, Last 90 Days', 
                    'unit': 'degrees', 'label': 'Temperature Departure (Fahrenheit)', 
                    'dfile': 'dly-tmax-normal.txt', 'mfile': 'mly-tmax-normal.txt',
                    'col': 'b', 'aname': 'maxt'},
         'depmin': {'id': 'depmin', 'title': 'Min Temperature Departure from Normal, Last 90 Days',
                    'unit': 'degrees', 'label': 'Temperature Departure (Fahrenheit)', 
                    'dfile': 'dly-tmin-normal.txt', 'mfile': 'mly-tmin-normal.txt',
                    'col': 'r', 'aname': 'mint'},
         'depavg': {'id': 'depavg', 'title': 'Mean Temperature Departure from Normal, Last 90 Days',
                    'unit': 'degrees', 'label': 'Temperature Departure (Fahrenheit)', 
                    'dfile': 'dly-tavg-normal.txt', 'mfile': 'mly-tavg-normal.txt',
                    'col': 'r', 'aname': 'avgt'},
         'deppcp': {'id': 'deppcp', 'title': 'Precipitation Departure from Normal, Last 90 Days',
                    'unit': 'inches', 'label': 'Precipitation Departure (inches)', 
                    'dfile': 'dly-prcp-50pctl.txt', 'mfile': 'mly-prcp-normal.txt',
                    'col': 'r', 'aname': 'pcpn'}, 
        }

# Additional colormaps
import matplotlib.colors

# Temperature #
norm = matplotlib.colors.Normalize(-60,120)

colors = [[norm(-60.0), [145./255.,0.,63./255.]],
          [norm(-55.0), [206./255.,18./255.,86./255.]],
          [norm(-50.0), [231./255.,41./255.,138./255.]],
          [norm(-45.0), [223./255.,101./255.,176./255.]],
          [norm(-40.0), [1.,115./255.,223./255.]],
          [norm(-35.0), [1.,190./255.,232./255.]],
          [norm(-30.0), [1.,1.,1.]],
          [norm(-25.0), [218./255.,218./255.,235./255.]],
          [norm(-20.0), [188./255.,189./255.,220./255.]],
          [norm(-15.0), [158./255.,154./255.,200./255.]],
          [norm(-10.0), [117./255.,107./255.,177./255.]],
          [norm(-5.0), [84./255.,39./255.,143./255.]],
          [norm(0.0), [13./255.,0.,125./255.]],
          [norm(5.0), [13./255.,61./255.,156./255.]],
          [norm(10.0), [0.,102./255.,194./255.]],
          [norm(15.0), [41./255.,158./255.,1.]],
          [norm(20.0), [74./255.,199./255.,1.]],
          [norm(25.0), [115./255.,215./255.,1.]],
          [norm(30.0), [173./255.,1.,1.]],
          [norm(35.0), [48./255.,207./255.,194./255.]],
          [norm(40.0), [0.,153./255.,150./255.]],
          [norm(45.0), [18./255.,87./255.,87./255.]],
          [norm(50.0), [6./255.,109./255.,44./255.]],
          [norm(55.0), [49./255.,163./255.,84./255.]],
          [norm(60.0), [116./255.,196./255.,118./255.]],
          [norm(65.0), [161./255.,217./255.,155./255.]],
          [norm(70.0), [211./255.,1.,190./255.]],
          [norm(75.0), [1.,1.,179./255.]],
          [norm(80.0), [1.,237./255.,160./255.]],
          [norm(85.0), [254./255.,209./255.,118./255.]],
          [norm(90.0), [254./255.,174./255.,42./255.]],
          [norm(95.0), [253./255.,141./255.,60./255.]],
          [norm(100.0), [252./255.,78./255.,42./255.]],
          [norm(105.0), [227./255.,26./255.,28./255.]],
          [norm(110.0), [177./255.,0.,38./255.]],
          [norm(115.0), [128./255.,0.,38./255.]],
          [norm(120.0), [89./255.,0.,66./255.]]]

tcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Temp - Condensed #
#norm = matplotlib.colors.Normalize(-60,120)
#
#colors = [[norm(-60.0), [1.,190./255.,232./255.]],
#          [norm(-35.0), [1.,190./255.,232./255.]],
#          [norm(-34.99), [218./255.,218./255.,235./255.]],
#          [norm(-25.0), [218./255.,218./255.,235./255.]],
#          [norm(-24.99), [13./255.,0.,125./255.]],
#          [norm(0.0), [13./255.,0.,125./255.]],
#          [norm(0.01), [173./255.,1.,1.]],
#          [norm(32.0), [173./255.,1.,1.]],
#          [norm(32.01), [1.,1.,1.]],
#          [norm(89.99), [1.,1.,1.]],
#          [norm(90.0), [254./255.,174./255.,42./255.]],
#          [norm(94.99), [254./255.,174./255.,42./255.]],
#          [norm(95.0), [253./255.,141./255.,60./255.]],
#          [norm(99.99), [253./255.,141./255.,60./255.]],
#          [norm(100.0), [252./255.,78./255.,42./255.]],
#          [norm(104.99), [252./255.,78./255.,42./255.]],
#          [norm(105.0), [227./255.,26./255.,28./255.]],
#          [norm(120.0), [227./255.,26./255.,28./255.]]]
#
#tcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Apparent Temperature (total) #
norm = matplotlib.colors.Normalize(-60,120)

colors = [[norm(-60.0), [145./255.,0.,63./255.]],
          [norm(-55.0), [206./255.,18./255.,86./255.]],
          [norm(-50.0), [231./255.,41./255.,138./255.]],
          [norm(-45.0), [223./255.,101./255.,176./255.]],
          [norm(-40.0), [1.,115./255.,223./255.]],
          [norm(-35.0), [1.,190./255.,232./255.]],
          [norm(-30.0), [1.,1.,1.]],
          [norm(-25.0), [218./255.,218./255.,235./255.]],
          [norm(-20.0), [188./255.,189./255.,220./255.]],
          [norm(-15.0), [158./255.,154./255.,200./255.]],
          [norm(-10.0), [117./255.,107./255.,177./255.]],
          [norm(-5.0), [84./255.,39./255.,143./255.]],
          [norm(0.0), [13./255.,0.,125./255.]],
          [norm(5.0), [13./255.,61./255.,156./255.]],
          [norm(10.0), [0.,102./255.,194./255.]],
          [norm(15.0), [41./255.,158./255.,1.]],
          [norm(20.0), [74./255.,199./255.,1.]],
          [norm(25.0), [115./255.,215./255.,1.]],
          [norm(30.0), [173./255.,1.,1.]],
          [norm(35.0), [48./255.,207./255.,194./255.]],
          [norm(40.0), [0.,153./255.,150./255.]],
          [norm(40.01), [255./255.,255./255.,255./255.]],
          [norm(74.99), [255./255.,255./255.,255./255.]],
          [norm(75.0), [1.,1.,179./255.]],
          [norm(80.0), [1.,237./255.,160./255.]],
          [norm(85.0), [254./255.,209./255.,118./255.]],
          [norm(90.0), [254./255.,174./255.,42./255.]],
          [norm(95.0), [253./255.,141./255.,60./255.]],
          [norm(100.0), [252./255.,78./255.,42./255.]],
          [norm(105.0), [227./255.,26./255.,28./255.]],
          [norm(110.0), [177./255.,0.,38./255.]],
          [norm(115.0), [128./255.,0.,38./255.]],
          [norm(120.0), [89./255.,0.,66./255.]]]

atcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Apparent Temperature (Wind Chill) #
norm = matplotlib.colors.Normalize(-60,120)

colors = [[norm(-60.0), [145./255.,0.,63./255.]],
          [norm(-55.0), [206./255.,18./255.,86./255.]],
          [norm(-50.0), [231./255.,41./255.,138./255.]],
          [norm(-45.0), [223./255.,101./255.,176./255.]],
          [norm(-40.0), [1.,115./255.,223./255.]],
          [norm(-35.0), [1.,190./255.,232./255.]],
          [norm(-30.0), [1.,1.,1.]],
          [norm(-25.0), [218./255.,218./255.,235./255.]],
          [norm(-20.0), [188./255.,189./255.,220./255.]],
          [norm(-15.0), [158./255.,154./255.,200./255.]],
          [norm(-10.0), [117./255.,107./255.,177./255.]],
          [norm(-5.0), [84./255.,39./255.,143./255.]],
          [norm(0.0), [13./255.,0.,125./255.]],
          [norm(5.0), [13./255.,61./255.,156./255.]],
          [norm(10.0), [0.,102./255.,194./255.]],
          [norm(15.0), [41./255.,158./255.,1.]],
          [norm(20.0), [74./255.,199./255.,1.]],
          [norm(25.0), [115./255.,215./255.,1.]],
          [norm(30.0), [173./255.,1.,1.]],
          [norm(35.0), [48./255.,207./255.,194./255.]],
          [norm(40.0), [0.,153./255.,150./255.]],
          [norm(40.01), [255./255.,255./255.,255./255.]],
          [norm(120.0), [255./255.,255./255.,255./255.]]]

atwccmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Apparent Temperature (Heat Index) #
norm = matplotlib.colors.Normalize(-60,120)

colors = [[norm(-60.0), [255./255.,255./255.,255./255.]],
          [norm(74.99), [255./255.,255./255.,255./255.]],
          [norm(75.0), [1.,1.,179./255.]],
          [norm(80.0), [1.,237./255.,160./255.]],
          [norm(85.0), [254./255.,209./255.,118./255.]],
          [norm(90.0), [254./255.,174./255.,42./255.]],
          [norm(95.0), [253./255.,141./255.,60./255.]],
          [norm(100.0), [252./255.,78./255.,42./255.]],
          [norm(105.0), [227./255.,26./255.,28./255.]],
          [norm(110.0), [177./255.,0.,38./255.]],
          [norm(115.0), [128./255.,0.,38./255.]],
          [norm(120.0), [89./255.,0.,66./255.]]]

athicmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Heat Index #
#norm = matplotlib.colors.Normalize(60,120)
#
#colors = [[norm(60.0), [220./255.,220./255.,220./255.]],
#          [norm(80.0), [220./255.,220./255.,220./255.]],
#          [norm(80.01), [1.,237./255.,160./255.]],
#          [norm(85.0), [254./255.,209./255.,118./255.]],
#          [norm(90.0), [254./255.,174./255.,42./255.]],
#          [norm(95.0), [253./255.,141./255.,60./255.]],
#          [norm(100.0), [252./255.,78./255.,42./255.]],
#          [norm(105.0), [227./255.,26./255.,28./255.]],
#          [norm(110.0), [177./255.,0.,38./255.]],
#          [norm(115.0), [128./255.,0.,38./255.]],
#          [norm(120.0), [89./255.,0.,66./255.]]]
#
#hicmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Heat Index - Condensed #
norm = matplotlib.colors.Normalize(60,120)

colors = [[norm(60.0), [1.,1.,1.]],
          [norm(99.99), [1.,1.,1.]],
          [norm(100.0), [252./255.,78./255.,42./255.]],
          [norm(104.99), [252./255.,78./255.,42./255.]],
          [norm(105.0), [227./255.,26./255.,28./255.]],
          [norm(120.0), [227./255.,26./255.,28./255.]]]

hicmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Wind Chill #
#norm = matplotlib.colors.Normalize(-60,40)
#
#colors = [[norm(-60.0), [145./255.,0.,63./255.]],
#          [norm(-55.0), [206./255.,18./255.,86./255.]],
#          [norm(-50.0), [231./255.,41./255.,138./255.]],
#          [norm(-45.0), [223./255.,101./255.,176./255.]],
#          [norm(-40.0), [1.,115./255.,223./255.]],
#          [norm(-35.0), [1.,190./255.,232./255.]],
#          [norm(-30.0), [1.,1.,1.]],
#          [norm(-25.0), [218./255.,218./255.,235./255.]],
#          [norm(-20.0), [188./255.,189./255.,220./255.]],
#          [norm(-15.0), [158./255.,154./255.,200./255.]],
#          [norm(-10.0), [117./255.,107./255.,177./255.]],
#          [norm(-5.0), [84./255.,39./255.,143./255.]],
#          [norm(0.0), [13./255.,0.,125./255.]],
#          [norm(5.0), [13./255.,61./255.,156./255.]],
#          [norm(10.0), [0.,102./255.,194./255.]],
#          [norm(15.0), [41./255.,158./255.,1.]],
#          [norm(20.0), [74./255.,199./255.,1.]],
#          [norm(25.0), [115./255.,215./255.,1.]],
#          [norm(30.0), [173./255.,1.,1.]],
#          [norm(30.01), [220./255.,220./255.,220./255.]],
#          [norm(40.0), [220./255.,220./255.,220./255.]]]
#
#wccmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Wind Chill - Condensed #
norm = matplotlib.colors.Normalize(-60,40)

colors = [[norm(-60.0), [1.,190./255.,232./255.]],
          [norm(-35.0), [1.,190./255.,232./255.]],
          [norm(-34.99), [218./255.,218./255.,235./255.]],
          [norm(-25.0), [218./255.,218./255.,235./255.]],
          [norm(-24.99), [13./255.,0.,125./255.]],
          [norm(0.0), [13./255.,0.,125./255.]],
          [norm(0.01), [173./255.,1.,1.]],
          [norm(32.0), [173./255.,1.,1.]],
          [norm(32.01), [1.,1.,1.]],
          [norm(40.0), [1.,1.,1.]]]

wccmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Wind Gusts #
norm = matplotlib.colors.Normalize(0,80)

colors = [[norm(0.0), [255./255.,255./255.,255./255.]],
          [norm(19.99), [255./255.,255./255.,255./255.]],
          [norm(20.0), [127./255.,205./255.,187./255.]],
          [norm(25.0), [180./255.,215./255.,158./255.]],
          [norm(30.0), [223./255.,1.,158./255.]],
          [norm(35.0), [1.,1.,166./255.]],
          [norm(40.0), [1.,232./255.,115./255.]],
          [norm(45.0), [1.,196./255.,0.]],
          [norm(50.0), [1.,170./255.,0.]],
          [norm(60.0), [1.,89./255.,0.]],
          [norm(70.0), [1.,0.,0.]],
          [norm(80.0), [168./255.,0.,0.]]]

wgcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Wind Speeds #
norm = matplotlib.colors.Normalize(0,80)

colors = [[norm(0.0), [16./255.,63./255.,120./255.]],
          [norm(5.0), [34./255.,94./255.,168./255.]],
          [norm(10.0), [29./255.,145./255.,192./255.]],
          [norm(15.0), [65./255.,182./255.,255./255.]],
          [norm(20.0), [127./255.,205./255.,187./255.]],
          [norm(25.0), [180./255.,215./255.,158./255.]],
          [norm(30.0), [223./255.,1.,158./255.]],
          [norm(35.0), [1.,1.,166./255.]],
          [norm(40.0), [1.,232./255.,115./255.]],
          [norm(45.0), [1.,196./255.,0.]],
          [norm(50.0), [1.,170./255.,0.]],
          [norm(60.0), [1.,89./255.,0.]],
          [norm(70.0), [1.,0.,0.]],
          [norm(80.0), [168./255.,0.,0.]]]

wspmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Wind Gusts - Condensed #
#norm = matplotlib.colors.Normalize(0,80)
#
#colors = [[norm(0.0), [1.,1.,1.]],
#          [norm(19.99), [1.,1.,1.]],
#          [norm(20.0), [220./255.,220./255.,220./255.]],
#          [norm(29.99), [220./255.,220./255.,220./255.]],
#          [norm(30.0), [223./255.,1.,158./255.]],
#          [norm(44.99), [223./255.,1.,158./255.]],
#          [norm(45.0), [1.,196./255.,0.]],
#          [norm(57.99), [1.,196./255.,0.]],
#          [norm(58.0), [1.,0.,0.]],
#          [norm(80.0), [1.,0.,0.]]]
#
#wgcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Wind Gusts - Alt Condensed #
#norm = matplotlib.colors.Normalize(0,80)
#
#colors = [[norm(0.0), [1.,1.,1.]],
#          [norm(19.99), [1.,1.,1.]],
#          [norm(20.0), [220./255.,220./255.,220./255.]],
#          [norm(29.99), [220./255.,220./255.,220./255.]],
#          [norm(30.0), [223./255.,1.,158./255.]],
#          [norm(39.99), [223./255.,1.,158./255.]],
#          [norm(40.0), [1.,196./255.,0.]],
#          [norm(49.99), [1.,196./255.,0.]],
#          [norm(50.0), [1.,0.,0.]],
#          [norm(80.0), [1.,0.,0.]]]
#
#wgcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Wind Direction #
norm = matplotlib.colors.Normalize(0,360)

colors = [[norm(0.0), [1.,0.,0.]],
          [norm(90.0), [1.,1.,0.]],
          [norm(180.0), [1.,1.,1.]],
          [norm(270.0), [0.,0.,0.]],
          [norm(360.0), [1.,0.,0.]]]

wdrmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Sky Cover #
norm = matplotlib.colors.Normalize(0,100)

colors = [[norm(0.0), [36./255.,160./255.,242./255.]],
          [norm(10.0), [78./255.,176./255.,242./255.]],
          [norm(20.0), [128./255.,183./255.,248./255.]],
          [norm(30.0), [160./255.,200./255.,1.]],
          [norm(40.0), [210./255.,225./255.,1.]],
          [norm(50.0), [225./255.,225./255.,225./255.]],
          [norm(60.0), [201./255.,201./255.,201./255.]],
          [norm(70.0), [165./255.,165./255.,165./255.]],
          [norm(80.0), [110./255.,110./255.,110./255.]],
          [norm(90.0), [80./255.,80./255.,80./255.]],
          [norm(100.0), [60./255.,60./255.,60./255.]]]

sccmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Relative Humidity #
norm = matplotlib.colors.Normalize(0,100)

colors = [[norm(0.0), [145./255.,0.,34./255.]],
          [norm(5.0), [166./255.,17./255.,34./255.]],
          [norm(10.0), [189./255.,46./255.,36./255.]],
          [norm(15.0), [212./255.,78./255.,51./255.]],
          [norm(20.0), [227./255.,109./255.,66./255.]],
          [norm(25.0), [250./255.,143./255.,67./255.]],
          [norm(30.0), [252./255.,173./255.,88./255.]],
          [norm(35.0), [254./255.,216./255.,132./255.]],
          [norm(40.0), [1.,242./255.,170./255.]],
          [norm(50.0), [230./255.,244./255.,157./255.]],
          [norm(60.0), [188./255.,227./255.,120./255.]],
          [norm(70.0), [113./255.,181./255.,92./255.]],
          [norm(80.0), [38./255.,145./255.,75./255.]],
          [norm(90.0), [0.,87./255.,46./255.]],
          [norm(100.0), [0.,87./255.,46./255.]]]

rhcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# PoPs #
norm = matplotlib.colors.Normalize(0,100)

colors = [[norm(0.0), [1.,1.,1.]],
          [norm(20.0), [144./255.,238./255.,144./255.]],
          [norm(40.0), [0.,1.,0.]],
          [norm(60.0), [50./255.,205./255.,50./255.]],
          [norm(80.0), [34./255.,139./255.,34./255.]],
          [norm(100.0), [0.,100./255.,0.]]]

popmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Precipitation Types #
tsnorm = matplotlib.colors.Normalize(1,4)

tscolors = [[tsnorm(1.0), 'indianred'],
          [tsnorm(1.999), 'indianred'],
          [tsnorm(2.0), 'red'],
          [tsnorm(2.999), 'red'],
          [tsnorm(3.0), 'darkred'],
          [tsnorm(4.0), 'darkred']]

tscmap = matplotlib.colors.LinearSegmentedColormap.from_list("", tscolors)

rnorm = matplotlib.colors.Normalize(1,4)

rcolors = [[rnorm(1.0), 'palegreen'],
          [rnorm(1.999), 'palegreen'],
          [rnorm(2.0), 'green'],
          [rnorm(2.999), 'green'],
          [rnorm(3.0), 'darkgreen'],
          [rnorm(4.0), 'darkgreen']]

rcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", rcolors)

snorm = matplotlib.colors.Normalize(1,4)

scolors = [[snorm(1.0), [88./255.,204./255.,237./255.]],
          [snorm(1.999), [88./255.,204./255.,237./255.]],
          [snorm(2.0), [18./255.,97./255.,160./255.]],
          [snorm(2.999), [18./255.,97./255.,160./255.]],
          [snorm(3.0), [7./255.,47./255.,95./255.]],
          [snorm(4.0), [7./255.,47./255.,95./255.]]]

scmap = matplotlib.colors.LinearSegmentedColormap.from_list("", scolors)

pnorm = matplotlib.colors.Normalize(1,4)

pcolors = [[pnorm(1.0), [214./255.,202./255.,255./255.]],
          [pnorm(1.999), [214./255.,202./255.,255./255.]],
          [pnorm(2.0), [122./255.,75./255.,237./255.]],
          [pnorm(2.999), [122./255.,75./255.,237./255.]],
          [pnorm(3.0), [71./255.,4./255.,161./255.]],
          [pnorm(4.0), [71./255.,4./255.,161./255.]]]

pcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", pcolors)

mnorm = matplotlib.colors.Normalize(1,4)

mcolors = [[mnorm(1.0), [253./255.,208./255.,162./255.]],
          [mnorm(1.999), [253./255.,208./255.,162./255.]],
          [mnorm(2.0), [241./255.,105./255.,19./255.]],
          [mnorm(2.999), [241./255.,105./255.,19./255.]],
          [mnorm(3.0), [127./255.,39./255.,4./255.]],
          [mnorm(4.0), [127./255.,39./255.,4./255.]]]

mcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", mcolors)

znorm = matplotlib.colors.Normalize(1,4)

zcolors = [[znorm(1.0), 'lightpink'],
          [znorm(1.999), 'lightpink'],
          [znorm(2.0), 'm'],
          [znorm(2.999), 'm'],
          [znorm(3.0), 'darkmagenta'],
          [znorm(4.0), 'darkmagenta']]

zcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", zcolors)

################################################

# Precip Accum #
norm = matplotlib.colors.Normalize(0,50)

colors = [[norm(0.0), [1.,1.,1.]],
          [norm(0.01), [199./255.,233./255.,192./255.]],
          [norm(0.10), [161./255.,217./255.,155./255.]],
          [norm(0.25), [116./255.,196./255.,118./255.]],
          [norm(0.50), [49./255.,163./255.,83./255.]],
          [norm(1.00), [0.,109./255.,44./255.]],
          [norm(1.50), [1.,250./255.,138./255.]],
          [norm(2.00), [1.,204./255.,79./255.]],
          [norm(3.00), [254./255.,141./255.,60./255.]],
          [norm(4.00), [252./255.,78./255.,42./255.]],
          [norm(6.00), [214./255.,26./255.,28./255.]],
          [norm(8.00), [173./255.,0.,38./255.]],
          [norm(10.00), [112./255.,0.,38./255.]],
          [norm(15.00), [59./255.,0.,48./255.]],
          [norm(20.00), [76./255.,0.,115./255.]],
          [norm(30.00), [1.,219./255.,1.]],
          [norm(50.00), [1.,1.,1.]]]

qacmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Precip Amount #
#  --condensed for RC climo & 48 hr
norm = matplotlib.colors.Normalize(0,1.5)

colors = [[norm(0.0), [1.,1.,1.]],
          [norm(0.01), [199./255.,233./255.,192./255.]],
          [norm(0.05), [161./255.,217./255.,155./255.]],
          [norm(0.10), [116./255.,196./255.,118./255.]],
          [norm(0.25), [49./255.,163./255.,83./255.]],
          [norm(0.50), [0.,109./255.,44./255.]],
          [norm(0.75), [1.,250./255.,138./255.]],
          [norm(1.00), [1.,204./255.,79./255.]],
          [norm(1.25), [254./255.,141./255.,60./255.]],
          [norm(1.50), [252./255.,78./255.,42./255.]]]
#          [norm(6.00), [214./255.,26./255.,28./255.]],
#          [norm(8.00), [173./255.,0.,38./255.]],
#          [norm(10.00), [112./255.,0.,38./255.]],
#          [norm(15.00), [59./255.,0.,48./255.]],
#          [norm(20.00), [76./255.,0.,115./255.]],
#          [norm(30.00), [1.,219./255.,1.]],
#          [norm(50.00), [1.,1.,1.]]]

qpcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

################################################

# Snow Accum #
norm = matplotlib.colors.Normalize(0,120)

colors = [[norm(0.0), [1.,1.,1.]],
          [norm(0.99), [189./255.,215./255.,231./255.]],
          [norm(1.00), [107./255.,174./255.,214./255.]],
          [norm(2.00), [49./255.,130./255.,189./255.]],
          [norm(3.00), [8./255.,81./255.,156./255.]],
          [norm(4.00), [8./255.,38./255.,148./255.]],
          [norm(6.00), [1.,1.,150./255.]],
          [norm(8.00), [1.,196./255.,0.]],
          [norm(12.00), [1.,135./255.,0.]],
          [norm(18.00), [219./255.,20./255.,0.]],
          [norm(24.00), [158./255.,0.,0.]],
          [norm(30.00), [105./255.,0.,0.]],
          [norm(36.00), [54./255.,0.,0.]],
          [norm(48.00), [204./255.,204./255.,1.]],
          [norm(60.00), [159./255.,140./255.,216./255.]],
          [norm(72.00), [124./255.,82./255.,165./255.]],
          [norm(96.00), [86./255.,28./255.,114./255.]],
          [norm(120.00), [46./255.,0.,51./255.]]]

sacmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Snow Amount #
#  --condensed for 48 hr
norm = matplotlib.colors.Normalize(0,12)

colors = [[norm(0.0), [1.,1.,1.]],
          [norm(0.1), [189./255.,215./255.,231./255.]],
          [norm(0.25), [107./255.,174./255.,214./255.]],
          [norm(0.50), [49./255.,130./255.,189./255.]],
          [norm(1.00), [8./255.,81./255.,156./255.]],
          [norm(1.50), [8./255.,38./255.,148./255.]],
          [norm(2.00), [1.,1.,150./255.]],
          [norm(3.00), [1.,196./255.,0.]],
          [norm(4.00), [1.,135./255.,0.]],
          [norm(5.00), [219./255.,20./255.,0.]],
          [norm(6.00), [158./255.,0.,0.]],
          [norm(8.00), [105./255.,0.,0.]],
          [norm(10.00), [54./255.,0.,0.]],
          [norm(12.00), [204./255.,204./255.,1.]]]
#          [norm(60.00), [159./255.,140./255.,216./255.]],
#          [norm(72.00), [124./255.,82./255.,165./255.]],
#          [norm(96.00), [86./255.,28./255.,114./255.]],
#          [norm(120.00), [46./255.,0.,51./255.]]]

sncmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Snow Amount #
#  --alt
norm = matplotlib.colors.Normalize(0,12)

colors = [[norm(0.0), [1.,1.,1.]],
          [norm(0.99), [189./255.,215./255.,231./255.]],
          [norm(1.00), [107./255.,174./255.,214./255.]],
          [norm(2.00), [49./255.,130./255.,189./255.]],
          [norm(3.00), [8./255.,81./255.,156./255.]],
          [norm(4.00), [8./255.,38./255.,148./255.]],
          [norm(6.00), [204./255.,204./255.,1.]],
          [norm(8.00), [159./255.,140./255.,216./255.]],
          [norm(10.00), [124./255.,82./255.,165./255.]],
          [norm(12.00), [86./255.,28./255.,114./255.]]]
#          [norm(120.00), [46./255.,0.,51./255.]]]

sncmap_alt = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

################################################

################################################

# Ice Accum #
norm = matplotlib.colors.Normalize(0,2)

colors = [[norm(0.0), [1.,1.,1.]],
          [norm(0.01), [243./255.,234./255.,59./255.]],
          [norm(0.10), [1.,192./255.,0.]],
          [norm(0.25), [1.,0.,0.]],
          [norm(0.50), [192./255.,0.,0.]],
          [norm(0.75), [153./255.,102./255.,1.]],
          [norm(1.00), [114./255.,10./255.,200./255.]],
          [norm(2.00), [36./255.,5./255.,91./255.]]]

iccmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

# Ice Amount #
#  --condensed for 48 hr
norm = matplotlib.colors.Normalize(0,0.5)

colors = [[norm(0.0), [1.,1.,1.]],
          [norm(0.01), [243./255.,234./255.,59./255.]],
          [norm(0.025), [1.,192./255.,0.]],
          [norm(0.05), [1.,0.,0.]],
          [norm(0.10), [192./255.,0.,0.]],
          [norm(0.25), [153./255.,102./255.,1.]],
          [norm(0.333), [114./255.,10./255.,200./255.]],
          [norm(0.50), [36./255.,5./255.,91./255.]]]

iacmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

################################################

# Categorical Hazards
norm = matplotlib.colors.Normalize(0,4)

colors = [[norm(0), 'white'],
          [norm(0.999), 'white'],
          [norm(1), 'orange'],
          [norm(1.999), 'orange'],
          [norm(2), 'red'],
          [norm(2.999), 'red'],
          [norm(3), 'hotpink'],
          [norm(4), 'hotpink']]

chcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

################################################

# Smoke Dispersal
norm = matplotlib.colors.Normalize(0,5)

colors = [[norm(0), 'red'],
          [norm(0.999), 'red'],
          [norm(1), 'gold'],
          [norm(1.999), 'gold'],
          [norm(2), 'limegreen'],
          [norm(2.999), 'limegreen'],
          [norm(3), 'darkgreen'],
          [norm(3.999), 'darkgreen'],
          [norm(4), 'darkturquoise'],
          [norm(5), 'darkturquoise'],
]

smdmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

################################################

# Visibility
norm = matplotlib.colors.Normalize(0,10)

colors = [[norm(0), [175./255.,80./255.,200./255.]],
          [norm(0.2499), [175./255.,80./255.,200./255.]],
          [norm(0.25), [145./255.,50./255.,185./255.]],
          [norm(0.4999), [145./255.,50./255.,185./255.]],
          [norm(0.50), [185./255.,0./255.,0./255.]],
          [norm(0.7499), [185./255.,0./255.,0./255.]],
          [norm(0.75), [210./255.,0./255.,0./255.]],
          [norm(0.9999), [210./255.,0./255.,0./255.]],
          [norm(1.00), [255./255.,30./255.,5./255.]],
          [norm(1.4999), [255./255.,30./255.,5./255.]],
          [norm(1.50), [255./255.,95./255.,15./255.]],
          [norm(1.9999), [255./255.,95./255.,15./255.]],
          [norm(2.00), [255./255.,125./255.,45./255.]],
          [norm(2.4999), [255./255.,125./255.,45./255.]],
          [norm(2.50), [255./255.,155./255.,75./255.]],
          [norm(2.9999), [255./255.,155./255.,75./255.]],
          [norm(3.00), [25./255.,105./255.,223./255.]],
          [norm(3.4999), [25./255.,105./255.,223./255.]],
          [norm(3.50), [35./255.,120./255.,238./255.]],
          [norm(3.9999), [35./255.,120./255.,238./255.]],
          [norm(4.00), [50./255.,140./255.,242./255.]],
          [norm(4.4999), [50./255.,140./255.,242./255.]],
          [norm(4.50), [70./255.,157./255.,245./255.]],
          [norm(5.00), [70./255.,157./255.,245./255.]],
          [norm(6.00), [205./255.,205./255.,205./255.]],
          [norm(10.00), [255./255.,255./255.,255./255.]],
          ]

vscmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

################################################

# Cloud Base (kft)
norm = matplotlib.colors.Normalize(0,25)

colors = [[norm(0), [175./255.,80./255.,200./255.]],
          [norm(0.2499), [175./255.,80./255.,200./255.]],
          [norm(0.25), [145./255.,50./255.,185./255.]],
          [norm(0.4999), [145./255.,50./255.,185./255.]],
          [norm(0.50), [185./255.,0./255.,0./255.]],
          [norm(0.7499), [185./255.,0./255.,0./255.]],
          [norm(0.75), [255./255.,30./255.,5./255.]],
          [norm(0.9999), [255./255.,30./255.,5./255.]],
          [norm(1.00), [25./255.,105./255.,223./255.]],
          [norm(1.4999), [25./255.,105./255.,223./255.]],
          [norm(1.50), [35./255.,120./255.,238./255.]],
          [norm(1.9999), [35./255.,120./255.,238./255.]],
          [norm(2.00), [50./255.,140./255.,242./255.]],
          [norm(2.4999), [50./255.,140./255.,242./255.]],
          [norm(2.50), [70./255.,157./255.,245./255.]],
          [norm(3.00), [70./255.,157./255.,245./255.]],
          [norm(3.0001), [205./255.,205./255.,205./255.]],
          [norm(25.00), [255./255.,255./255.,255./255.]],
          ]

cbcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

################################################

# Fire Risk
norm = matplotlib.colors.Normalize(0,5)

colors = [[norm(0), [0./255.,255./255.,0./255.]],
          [norm(0.999), [0./255.,255./255.,0./255.]],
          [norm(1), [255./255.,255./255.,0./255.]],
          [norm(1.999), [255./255.,255./255.,0./255.]],
          [norm(2), [255./255.,153./255.,0./255.]],
          [norm(2.999), [255./255.,153./255.,0./255.]],
          [norm(3), [255./255.,0./255.,0./255.]],
          [norm(3.999), [255./255.,0./255.,0./255.]],
          [norm(4), [255./255.,60./255.,231./255.]],
          [norm(5), [255./255.,60./255.,231./255.]]
          ]

frcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

################################################

# Categorical Hazards
norm = matplotlib.colors.Normalize(0,5)

colors = [[norm(0), [1.,1.,1.]],
          [norm(0.999), [1.,1.,1.]],
          [norm(1), [255./255.,255./255.,6./255.]],
          [norm(1.999), [255./255.,255./255.,6./255.]],
          [norm(2), [254./255.,164./255.,5./255.]],
          [norm(2.999), [254./255.,164./255.,5./255.]],
          [norm(3), [255./255.,5./255.,6./255.]],
          [norm(3.999), [255./255.,5./255.,6./255.]],
          [norm(4), [201./255.,20./255.,255./255.]],
          [norm(5), [201./255.,20./255.,255./255.]]]

hzcmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
