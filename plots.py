# -*- coding: utf-8 -*-
"""
Created on Tue May 13 10:55:20 2014

@author: bmorris
"""

import numpy as np
from matplotlib import pyplot as plt

def faketransit(times, midtransit, duration, depth):
    fluxes = np.ones_like(times)
    intransit = (times < midtransit+duration/2)*(times > midtransit-duration/2)
    fluxes[intransit] -=depth
    return fluxes
    
times = np.linspace(0,1,100)    # times of fake photometric measurements
names = ['b', 'c']              # name for each planet
midtransits = [0.5, 0.5]        # time of mid-transit
durations = [0.4, 0.7]          # duration of the transit event
depths = [0.02, 0.005]          # fractional change in flux in transit event
noise = 0.1*np.min(depths)       # simulated noise factor

fig, ax = plt.subplots(1,len(depths),figsize=(14,6))

for i in range(len(depths)):
    # Generate (fake) model light curve
    lightcurve = faketransit(times, midtransits[i], durations[i], depths[i])
    
    # Add gaussian noise to make the model look like data
    lightcurve += noise*np.random.randn(len(lightcurve))
    
    ax[i].plot(times, lightcurve, 'k-o')
    ax[i].set_title('Planet %s' % names[i])
    ax[i].set_xlabel('Time (days)')
    ax[i].set_ylabel('Apparent Host-Star Brightness')
    ax[i].set_xlim([np.min(times), np.max(times)])
    ax[i].set_ylim([1-2*depths[i], 1+depths[i]])
    ax[i].grid()
fig.savefig('plots/faketransit.pdf',bbox_inches='tight')
plt.show()