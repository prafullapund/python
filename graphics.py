#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 00:10:25 2017

@author: Prafull
"""

from turtle import Turtle
t = Turtle()
 
t.speed(0)
def spiral(n):
    if n < 300:
        t.forward(n)
        t.right(91)
        spiral(n+2)
 
spiral(2)
input('Press any key to continue...')