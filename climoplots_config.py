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

sites = {
        'bels2': {'id': ['bels2'], 'file': 'bels2', 'name': 'Belle Fourche', 'por': 1908, 'ppor': 1908, 'spor': 1908, 'snow': 1},
        'biss2': {'id': ['biss2'], 'file': 'biss2', 'name': 'Bison', 'por': 1916, 'ppor': 1916, 'spor': 1916, 'snow': 1},
        'cacs2': {'id': ['cacs2'], 'file': 'cacs2', 'name': 'Camp Crook', 'por': 1893, 'ppor': 1893, 'spor': 1893, 'snow': 1},
        'cuss2': {'id': ['cuss2'], 'file': 'cuss2', 'name': 'Custer', 'por': 1942, 'ppor': 1911, 'spor': 1911, 'snow': 1},
        'cwds2': {'id': ['cwds2'], 'file': 'cwds2', 'name': '2 miles east of Cottonwood', 'por': 1909, 'ppor': 1909, 'spor': 1909, 'snow': 1},
        'dtrw4': {'id': ['dtrw4'], 'file': 'dtrw4', 'name': 'Devils Tower', 'por': 1959, 'ppor': 1959, 'spor': 1959, 'snow': 0},
        'dups2': {'id': ['dups2'], 'file': 'dups2', 'name': 'Dupree', 'por': 1922, 'ppor': 1922, 'spor': 1922, 'snow': 1},
        'dprs2': {'id': ['dprs2'], 'file': 'dprs2', 'name': '15 miles south-southeast of Dupree', 'por': 1963, 'ppor': 1963, 'spor': 1963, 'snow': 1},
        'emts2': {'id': ['emts2'], 'file': 'emts2', 'name': 'Edgemont', 'por': 1979, 'ppor': 1948, 'spor': 1979, 'snow': 1},
        'ftms2': {'id': ['ftms2'], 'file': 'ftms2', 'name': 'Fort Meade', 'por': 1902, 'ppor': 1902, 'spor': 1902, 'snow': 1},
        'gilw4': {'id': ['gilw4'], 'file': 'gilw4', 'name': '4 miles southeast of Gillette', 'por': 1902, 'ppor': 1902, 'spor': 1902, 'snow': 1},
        'hics2': {'id': ['hics2'], 'file': 'hics2', 'name': 'Hill City', 'por': 1968, 'ppor': 1909, 'spor': 1909, 'snow': 1},
        'hoss2': {'id': ['hoss2'], 'file': 'hoss2', 'name': 'Hot Springs', 'por': 1894, 'ppor': 1894, 'spor': 1894, 'snow': 1},
        'ints2': {'id': ['ints2'], 'file': 'ints2', 'name': '3 miles northeast of Interior', 'por': 1949, 'ppor': 1949, 'spor': 1949, 'snow': 1},
        'krls2': {'id': ['krls2'], 'file': 'krls2', 'name': '6 miles north of Kirley', 'por': 1970, 'ppor': 1970, 'spor': 1970, 'snow': 1},
        'kyls2': {'id': ['kyls2'], 'file': 'kyls2', 'name': '2 miles east of Kyle', 'por': 1956, 'ppor': 1956, 'spor': 1956, 'snow': 0},
        'leas2': {'id': ['leas2'], 'file': 'leas2', 'name': 'Lead', 'por': 1909, 'ppor': 1909, 'spor': 1909, 'snow': 1}, 
        'lems2': {'id': ['lems2'], 'file': 'lems2', 'name': 'Lemmon', 'por': 1909, 'ppor': 1908, 'spor': 1909, 'snow': 1},
        'mrts2': {'id': ['mrts2'], 'file': 'mrts2', 'name': '8 miles east of Martin', 'por': 1980, 'ppor': 1980, 'spor': 1980, 'snow': 0},
        'mrns2': {'id': ['mrns2'], 'file': 'mrns2', 'name': '12 miles southwest of Maurine', 'por': 1975, 'ppor': 1975, 'spor': 1975, 'snow': 1},
        'mvls2': {'id': ['mvls2'], 'file': 'mvls2', 'name': '5 miles northeast of Milesville', 'por': 1911, 'ppor': 1911, 'spor': 1911, 'snow': 1},
        'msns2': {'id': ['msns2'], 'file': 'msns2', 'name': '14 miles south of Mission', 'por': 1951, 'ppor': 1951, 'spor': 1951, 'snow': 1},
        'rnms2': {'id': ['rnms2'], 'file': 'rnms2', 'name': 'Mount Rushmore', 'por': 1962, 'ppor': 1962, 'spor': 1962, 'snow': 1},
        'nclw4': {'id': ['nclw4'], 'file': 'nclw4', 'name': 'Newcastle', 'por': 1906, 'ppor': 1906, 'spor': 1906, 'snow': 1},
        'nwls2': {'id': ['nwls2'], 'file': 'nwls2', 'name': 'Newell', 'por': 1920, 'ppor': 1920, 'spor': 1920, 'snow': 1},
        'oels2': {'id': ['oels2'], 'file': 'oels2', 'name': 'Oelrichs', 'por': 1893, 'ppor': 1893, 'spor': 1893, 'snow': 1},
        'orls2': {'id': ['orls2'], 'file': 'orls2', 'name': 'Oral', 'por': 1971, 'ppor': 1971, 'spor': 1971, 'snow': 1},
        'raps2': {'id': ['raps2'], 'file': 'raps2', 'name': 'Pactola Dam', 'por': 1955, 'ppor': 1951, 'spor': 1955, 'snow': 1},
        'unrs2': {'id': ['UNRS2thr'], 'file': 'unrs2', 'name': 'Downtown Rapid City', 'por': 1888, 'ppor': 1888, 'spor': 1888, 'snow': 1},
        'krap': {'id': ['RAPthr'], 'file': 'rap', 'name': 'Rapid City Regional Airport', 'por': 1942, 'ppor': 1942, 'spor': 1942, 'snow': 1},
        'rocw4': {'id': ['rocw4'], 'file': 'rocw4', 'name': '7 miles east-northeast of Rochelle', 'por': 1928, 'ppor': 1927, 'spor': 1927, 'snow': 0},
        'spes2': {'id': ['spes2'], 'file': 'spes2', 'name': 'Spearfish', 'por': 1893, 'ppor': 1893, 'spor': 1893, 'snow': 1},
        'wesw4': {'id': ['wesw4'], 'file': 'wesw4', 'name': '1 mile east of Weston', 'por': 1960, 'ppor': 1951, 'spor': 1951, 'snow': 1},
        'wnds2': {'id': ['wnds2'], 'file': 'wnds2', 'name': 'Wind Cave', 'por': 1990, 'ppor': 1948, 'spor': 1990, 'snow': 1},
        'wins2': {'id': ['wins2'], 'file': 'wins2', 'name': 'Winner', 'por': 1910, 'ppor': 1910, 'spor': 1910, 'snow': 1},
        'wuds2': {'id': ['wuds2'], 'file': 'wuds2', 'name': 'Wood', 'por': 1913, 'ppor': 1913, 'spor': 1913, 'snow': 1},
        'kgcc': {'id': ['kgcc'], 'file': 'gcc', 'name': 'Gillette Campbell County Airport', 'por': 1998, 'ppor': 1998, 'spor': 1998, 'snow': 0},
        'k2wx': {'id': ['k2wx'], 'file': '2wx', 'name': 'Buffalo', 'por': 1998, 'ppor': 1998, 'spor': 1998, 'snow': 0},
        'kd07': {'id': ['kd07'], 'file': 'd07', 'name': 'Faith', 'por': 1998, 'ppor': 1998, 'spor': 1998, 'snow': 0},
        'kien': {'id': ['kien'], 'file': 'ien', 'name': 'Pine Ridge', 'por': 1997, 'ppor': 1997, 'spor': 1997, 'snow': 0},
        'kphp': {'id': ['kphp'], 'file': 'php', 'name': 'Philip', 'por': 1907, 'ppor': 1907, 'spor': 1907, 'snow': 0},
        'kcut': {'id': ['kcut'], 'file': 'cut', 'name': 'Custer', 'por': 1999, 'ppor': 1999, 'spor': 1999, 'snow': 0},
        'sdnw4': {'id': ['sdnw4'], 'file': 'sdnw4', 'name': 'Sundance', 'por': 1893, 'ppor': 1893, 'spor': 1893, 'snow': 1},
        }

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
