#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 10:42:14 2017

@author: Prafull
"""

import numpy as np
x=np.array([[1,2,3],[4,445,6],[7,8,9]])
x.ndim
print x
x.shape
x.itemsize
x.size
x[0,2]
x[0:2]
x[:,0]
x[:,:1]
x[:2,1:]
x[1:]
x[:,2]=[11,1,11]
x.sum()

x.prod()
np.sum(x)
x.mean()
x.var()
x.min()
x.max()
np.arange(10)
x.sort()
x
sorted(x,reverse=True)
a=np.array([[1,7],[5,1]])
b=np.array([[3,4],[2,1]])
a*b

a.dot(b)

c=np.array([11.1,21.5,31.6])
np.floor(c)
np.ceil(c)

a=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int)
b=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int)
print a+b

a.transpose()

np.invert(a)

# x+y+z=6
# y+5z=-4
# x+5y-z=27

a=np.array([[1,1,1],[0,1,5],[1,5,-1]])
b=np.array([[6],[-4],[27]])
aI=np.linalg.inv(a)
x=np.dot(aI,b)
print x
#or directly using solve
x=np.linalg.solve(a,b)
print x


a=np.array([1,1,1])
b=np.array([6,1,2])
a>b
a==b
a<=b


a=np.array([[1,1,1],[0,1,5],[1,5,-1]])
np.arange(2)
np.median(a)

np.corrcoef(a)

np.cov(a)


a=np.mat([[4,3],[2,1]])
b=np.mat([[1,2],[3,4]])
print a*b


#Shallow/deep copy

a=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int)
b=a
print id(a) == id(b)

d=a.copy
print id(a)== id(d)




import numpy as np
x=np.array([[1,2,3],[4,445,6],[7,8,9]])
x.ndim
print x
x.shape
x.itemsize
x.size
x[0,2]
x[0:2]
x[:,0]
x[:,:1]
x[:2,1:]
x[1:]
x[:,2]=[11,1,11]
x.sum()
x.prod()
np.sum(x)
x.mean()
x.var()
x.min()
x.max()
np.arange(10)
x.sort()
x
sorted(x,reverse=True)
a=np.array([[1,1],[0,1]])
b=np.array([[3,4],[2,1]])
a*b

a.dot(b)
np.dot(a,b)
















