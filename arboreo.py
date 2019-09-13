#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:31:27 2019

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

# Símbolos
V = {'F','+','-','[',']'}

# Iniciador
omega = '++++F'

# Reglas de procucción
P = {
     'F' : 'FF-[-F+F+F]+[+F-F-F]',
     }

arboleo = Lindenmayer(V,P,omega)
bonsai = Tortuga(1,pi/8)
bonsai.play(arboleo.rewrite(3))
