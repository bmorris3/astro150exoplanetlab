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
midtransit = 0.5                # time of mid-transit
duration = 0.4                  # duration of the transit event
depth = 0.01                    # fractional change in flux in transit event
noise = 0.1*depth

# Generate (fake) model light curve
lightcurve = faketransit(times, midtransit, duration, depth)

# Add gaussian noise to make the model look like data
lightcurve += noise*np.random.randn(len(lightcurve))

fig, ax = plt.subplots(1,1)
ax.plot(times, lightcurve, 'k-o')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Apparent Host-Star Brightness')
ax.set_xlim([np.min(times), np.max(times)])
ax.set_ylim([1-2*depth, 1+depth])
fig.savefig('plots/faketransit.pdf')
plt.show()