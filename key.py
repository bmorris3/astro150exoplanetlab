# -*- coding: utf-8 -*-
"""
Created on Tue May 13 16:20:44 2014

@author: bmorris
"""
import numpy as np

M_earth = 5.97219e24 # kg
rho_water = 1000 # kg m^-3
R_earth = 6378.1e3 # meters
R_planet = 3.082986*R_earth

M_planet = rho_water*((4./3)*np.pi*R_planet**3)
print 'Mass of water planet, planet b [M_earth]: %f' % (M_planet/M_earth)

const = 1e-3*M_planet/((4./3)*np.pi*R_earth**3) # convert to g/cm^3
print 'const = %d' % const
print 'rho = %f' % (const/(R_planet/R_earth)**3)