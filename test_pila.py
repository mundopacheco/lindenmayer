#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:04:22 2019

@author: mundo
"""

#%%
import sys
sys.path.append('src/')
from stack import Stack

p = Stack()

p.push(1)
p.push("hola")
p.push([2,3,7])
p.push(True)

print(p)


print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())

p.push(2)
p.push("hello")
p.push({1,23,3})

print(p)
