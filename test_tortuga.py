#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 08:21:45 2019

@author: mundo
"""

#%%
import sys
sys.path.append('src/')
from tortuga import Tortuga
from math import cos, sin, pi



t = Tortuga(d=1, delta=pi/3)

i_list = ['F', '-', '-','F', '-', '-','F', '-', '+',
        'F', '-', '-','F', '-', '-','F', '-', '-',
        '+','F', '-', '-','F', '-', '-','F', '-', '-',
        '+','F', '-', '-','F', '-', '-','F', '-', '-',
        '+','F', '-', '-','F', '-', '-','F', '-', '-',
        '+','F', '-', '-','F', '-', '-','F', '-', '-',
        '+','F', '-', '-','F', '-', '-','F', '-', '-']

for x in i_list:
    t.play(x)
    
#u = Tortuga(d=0.5, delta=pi/2, x=2, y=2, angle=pi/4)
#u.play('F')
#u.play('+')
#u.play('F')
#u.play('+')
#u.play('F')
#u.play('+')
#u.play('F')
