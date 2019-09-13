#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:54:00 2019

@author: mundo
"""
class Element:
    def __init__(self,e,nxt):
        self.e = e
        self.nxt = nxt


class Stack:    
    
    def __init__(self):
        self.tope = None
        
    def push(self, x):
        self.tope = Element(x,self.tope)
        
    def pop(self):
        if self.tope:
            e = self.tope.e
            self.tope = self.tope.nxt
        else:
            e = None
        return e
    
    def __to_list__(self,x):
        s = []
        if x != None:
            s.append(x.e)
            if x.nxt != None:
                s += self.__to_list__(x.nxt)
        return s
        
    def __str__(self):
        return " -> ".join(map(str,self.__to_list__(self.tope)))
    
    
        