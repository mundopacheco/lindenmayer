#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 08:59:28 2019

@author: mundo
"""
#%%
import sys
sys.path.append('src/')
from tortuga import Tortuga
from Lindenmayer import Lindenmayer
from math import pi

# Up the recursion limit
sys.setrecursionlimit(10**5)

# Symbols
V = {'A','F','f','+','-'}
# Iniciador
omega = 'A+A+A+A+A+A'
# Production rules
P = {
     'A' : 'F--F--F--f--f',
     'F' : 'F+F--F+F',
     'f' : 'f+f--f+f'
     }

snowflake = Lindenmayer(V,P,omega)


voldetort = Tortuga(1,pi/3)

voldetort.play(snowflake.rewrite(4))




