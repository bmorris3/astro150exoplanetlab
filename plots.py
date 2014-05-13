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
durations = [0.3, 0.6]          # duration of the transit event
depths = [0.02, 0.00015]        # fractional change in flux in transit event
noises = 0.1*np.array(depths)   # simulated noise factor
answerkeyname = 'answerkey.txt'

outfile = open(answerkeyname,'w')
fig, ax = plt.subplots(1,len(depths),figsize=(14,6))

for i in range(len(depths)):
    # Generate (fake) model light curve
    lightcurve = faketransit(times, midtransits[i], durations[i], depths[i])
    
    # Add gaussian noise to make the model look like data
    lightcurve += noises[i]*np.random.randn(len(lightcurve))
    
    # Assuming R_* = R_sun, and R_sun = 109*R_earth, 
    R_planet = 109*np.sqrt(depths[i])
    newline = 'Radius of planet %s = %f Earth radii\n' % (names[i], R_planet)
    print newline
    outfile.write(newline)
    
    ax[i].plot(times, lightcurve, 'k-o')
    ax[i].set_title('Planet %s' % names[i])
    ax[i].set_xlabel('Time (days)')
    ax[i].set_ylabel('Apparent Host-Star Brightness')
    ax[i].set_xlim([np.min(times), np.max(times)])
    ax[i].set_ylim([1-2*depths[i], 1+depths[i]])
    ax[i].get_yaxis().get_major_formatter().set_useOffset(False)
    ax[i].grid()

outfile.close()

fig.subplots_adjust(wspace=0.25)
fig.savefig('plots/faketransit.pdf',bbox_inches='tight')
plt.show()