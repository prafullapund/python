#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 16:54:03 2017

@author: Prafull
"""
import numpy as np

#1Create two dimensional array with 4 columns[1,2,3,4],[5,6,7,8]

a=np.array([[1,2,3,4],[6,7,8,9]])

#2. Display row sum and Column sum of above matrix.
a.sum(axis=0)
a.sum(axis=1)

#3. Create 3*3 matrix using arange function.
np.arange(9).reshape(3,3)

#4. a = [0,1,2,3,4,5,6,7,8,9] using Slicing Display even and odd no in a list
a = [0,1,2,3,4,5,6,7,8,9]
even=filter(lambda x: x%2==0, a)
odd=filter(lambda x: x%2!=0, a)

#5. Create a matrix of order 3*3 find determinant, Eigen values, transpose the matrix.

m=np.arange(9).reshape(3,3)
np.linalg.det(m)
np.linalg.eig(m)
m.transpose()

#6.Demonstatre all the statistical function take 20 uniform distribution values as a input.

x=np.random.uniform(size=20)

x.prod()
np.sum(x)
x.mean()
x.var()
x.min()
x.max()
x.sort()
x.std()