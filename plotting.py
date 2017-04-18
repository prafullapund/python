#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:15:11 2017

@author: Prafull
"""

import pylab as pl
import numpy as np

x=[1,2,3,4,5]
y=[6,7,8,9,10]
pl.plot(x,y, 'y-^')
pl.plot(x,y, 'y-.')

x=np.random.rand(100)
y=np.random.rand(100)
pl.plot(x,y, 'y-^')
pl.plot(x,y)


x=np.random.randn(100)
y=np.random.randn(100)
pl.plot(x,y, 'y-^')
pl.plot(x,y)
pl.scatter(x,y)
pl.plot(x,y, 'y-o')

pl.plot(np.sin(x))
pl.plot(np.cos(x))

x=np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s=np.cos(x),np.sin(x)
pl.plot(x,c)
pl.plot(x,s)
pl.show()

x=np.linspace(1,110,256,endpoint=True)
c,s=np.cos(x),np.sin(x)
pl.plot(x,c)
pl.plot(x,s)
pl.show()

x=np.arange(50)*2*np.pi/50
y=np.sin(x)
pl.plot(y)
pl.bar(x,y,width=x[1]-x[0])
pl.show()
pl.bar(x,y)


import matplotlib.pyplot as plt
import numpy as np
data=np.random.randn(1000)
f,(ax1,ax2)=plt.subplots(1,2,figsize=(6,3))
ax1.hist(data,bins=30,normed=True,color='b')
ax2.hist(data,bins=10, normed=False, color='r',cumulative=True)


x=[1,2,3,2,1]
y=[3,2,1,3,1]
pl.subplot(2,1,1)
pl.plot(x)
pl.subplot(2,1,2)
pl.plot(y)



x=[1,2,3,2,1]
y=[3,2,1,3,1]
pl.subplot(1,2,1)
pl.plot(x)
pl.subplot(1,2,2)
pl.plot(y)

x=np.random.randn(256)
pl.boxplot(x,vert=0)
pl.show()

samp1=np.random.normal(loc=0,scale=3.,size=200)
samp2=np.random.normal(loc=5.,scale=10.,size=500)
samp3=np.random.normal(loc=0.3,scale=1.2,size=100)
f,ax=plt.subplots(1,1,figsize=(5,4))
ax.boxplot((samp1,samp2,samp3))
ax.set_xticklabels(['sample1','sample2','sample3'])
















