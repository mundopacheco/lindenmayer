#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 08:37:15 2019

@author: mundo
"""

class Lindenmayer:
    
    def __init__(self,V,P,omega):
        # V is a set of symblos
        self.V = V
        # P are the production rules (dictionary)
        self.P = P
        # Initial symbol sequence (string)
        self.omega = omega
        
    # Function that recursively rewrites the current step according to P 
    def step(self, s):
        return (self.P[s[0]] if s[0] in self.P else s[0]) +\
                self.step(s[1:]) if s else s
                
        # This is the unpythonic version
#        if not s:
#            res = s
#        else:
##            if s[0] in self.P:
##                resultado = self.P[s[0]] + self.paso(s[1:])
##            else:
##                resultado = s[0] + self.paso(s[1:])
#            res = (self.P[s[0]] if s[0] in self.P else s[0]) + self.paso(s[1:])
#       
#        return res
        
    # Function that recursively writes a single time the current sequence of symbols
    def __rewrite__(self, n, s):
        return s if n == 0 else self.__rewrite__(n-1, self.step(s))
 
    # Function that rewritres the inital sequence n times
    def rewrite(self,n):
        return self.__rewrite__(n,self.omega)
            



        

            