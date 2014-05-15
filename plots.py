# -*- coding: utf-8 -*-
"""
Created on Tue May 13 10:55:20 2014

@author: bmorris
"""

import numpy as np
from matplotlib import pyplot as plt

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

majorLocator   = MultipleLocator(0.01)
majorFormatter = FormatStrFormatter('%.2f%%')
#minorLocator   = MultipleLocator(1)
from matplotlib.ticker import AutoMinorLocator


def faketransit(times, midtransit, duration, depth):
    fluxes = np.ones_like(times)
    intransit = (times < midtransit+duration/2)*(times > midtransit-duration/2)
    fluxes[intransit] -=depth
    return fluxes
    
times = np.linspace(0,1,100)    # times of fake photometric measurements
names = ['b', 'c']              # name for each planet
midtransits = [0.5, 0.5]        # time of mid-transit
durations = [0.3, 0.6]          # duration of the transit event
depths = [0.0008, 0.00015]        # fractional change in flux in transit event
noises = len(depths)*[0.15*np.min(depths)]#0.1*np.array(depths)   # simulated noise factor
markers = ['s','o']
answerkeyname = 'answerkey.txt'

outfile = open(answerkeyname,'w')
#fig, ax = plt.subplots(1,len(depths),figsize=(14,6))
fig, ax = plt.subplots(1,1,figsize=(14,10))

lightcurves = []
for i in range(len(depths)):
    # Generate (fake) model light curve
    lightcurve = faketransit(times, midtransits[i], durations[i], depths[i])
    
    # Add gaussian noise to make the model look like data
    lightcurve += noises[i]*np.random.randn(len(lightcurve))
    lightcurves.append(lightcurve)
    
    # Assuming R_* = R_sun, and R_sun = 109*R_earth, 
    R_planet = 109*np.sqrt(depths[i])
    newline = 'Radius of planet %s = %f Earth radii\n' % (names[i], R_planet)
    print newline
    outfile.write(newline)

    ax.plot(times+1.5*i, lightcurve*100, 'k-'+markers[i])
    annotation = 'Planet %s' % names[i]
    ax.annotate(annotation, (np.mean(times+1.5*i), np.max(lightcurve*100)*1.00001), textcoords='data', \
    ha='center', va='center',size=18,bbox=dict(fc="w",ec="none",alpha=0.8))

#ax.set_ylim([np.min(lightcurves*100)*0.99,100.001])

# Manage tick marks
ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
ax.yaxis.set_minor_locator(AutoMinorLocator())

#ax.set_title('Transit Observations')
ax.set_xlabel('Time (days)', fontsize=20)
ax.set_ylabel('Apparent Host-Star Brightness', fontsize=20)
ax.grid()

outfile.close()

fig.subplots_adjust(wspace=0.25)
fig.savefig('plots/faketransit.pdf',bbox_inches='tight')
plt.show()