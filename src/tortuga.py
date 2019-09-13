#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:28:39 2019

@author: mundo
"""

import matplotlib.pyplot as plt
from math import cos, sin, pi
from stack import Stack

class Tortuga:
    
    # Tortuga constructor
    def __init__(self,d,delta,x=0,y=0,angle=0,color='c'):
        self.x = x
        self.y = y
        self.x_p = x
        self.y_p = y
        self.angle = angle
        self.d = d
        self.delta = delta
        self.color = color
        plt.figure()
        plt.axis('off')
        plt.axis('equal')
        self.stack = Stack()
        self.stack.push((x,y,angle))
        
    # Move without drawing
    def move(self):
        self.x_p, self.y_p = self.x, self.y
        self.x = self.x + (self.d * cos(self.angle))
        self.y = self.y + (self.d * sin(self.angle))
        
    # Move drawing
    def draw(self):
        plt.plot([self.x_p, self.x], [self.y_p, self.y], color=self.color)
        #plt.pause(.2)
        
    # Read single symbol
    def __read__(self, c):
        if c == "F":
            self.move()
            self.draw()
        elif c == "f":
            self.move()
        elif c == "+":
            self.angle = self.angle + self.delta
        elif c == "-":
            self.angle = self.angle - self.delta
        elif c == "[":
            self.stack.push((self.x,self.y,self.angle))
        elif c == "]":
            self.x, self.y, self.angle = self.stack.pop()
        
    # Read all symbols
    def play(self,s):
        if len(s) == 1:
            self.__read__(s)
        elif len(s)>1:
            self.__read__(s[0])
            self.play(s[1:])
