#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:50:16 2017

@author: Prafull
"""

#1	Count the word ends with e 
word='Python provides a nice way of iterating over a string using a for loop Keep it simple'
word.count('e')
s=word.split()
len(s)
count=0
for i in range(len(s)):
    if s[i].endswith('e'):
        print s[i]
        count += 1    
print count



#2	Count the number of 'e' and 'a'
word='Python provides a nice way of iterating over a string using a for loop Keep it simple'
s=word.split()
count=0
for i in range(len(s)):
    if s[i].count('e') or s[i].count('a'):
        print s[i]
        count+=1
print count   

#3 	Write a Program to Display Reverse of a number
x=int(input('please entere a number:'))
b=0
while(x>0):
    r=x%10
    b=(b*10) + r
    x=x//10
print b
print('Reverse of enetered number is = %d'%b)

   
#4	Write a Program to display Fibonacci Series
n=input('please enter number of iteration:')
a=0
b=1
c=0
for i in range(n):
     c=a+b
     print c
     a=b
     b=c

#5 	Write a Program to display given no is prime or not

n=input('Please enter a number:')

if(n>1):
     for i in range(2,n):
          if (n%i)==0:
               print (n,'number is not prime number')  
               break
               
     else:
          print (n,'number is a prime number')
else:
     print(n,'is not a prime number')
          
     
#6	Write a program to display cube of number between 1 to 10 using lambda and map function
a = [1,2,3,4,5,6,7,8,9,10]
cube=map(lambda x:x*x*x,a)
cube
     

#7	Write a program to display number divisible by two in the given list [0,12,17,29,30,5,89,13,18,28] using lambda and filter function.

a=[0,12,17,29,30,5,89,13,18,28]

div=filter(lambda x:x%2==0,a)
div

# 8	Write a program to return output of this list [3,4,5,6,7,8],x*y using lambda and reduce function.
a=[3,4,5,6,7,8]
ret=reduce(lambda x,y:x*y ,a)
ret
#9.	Take the given matrix a=   and Find out Determinant, Inverse.
from numpy import matrix
A = matrix( [[2,3,4],[7,6,5],[1,2,3]]) 
print A.T                                    # Transpose of A.
print A.I                                    # Inverse of A.
det(A)                                       #Determinant of A.     

#10.	Take any array(3*3) as the input and Slice them

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int)

#a) Display column and rows
a.shape
a[:,:]
#b)Display only Second Column Element of all rows
a[:,1:2]

#c)Update the values of First Position of the matrix with 1,2,3

a[0,0]=1
a[1,0]=2
a[2,0]=3
a
#d)Display only third Column.
a[:,2:3]


#11	Demonstrate Difference between array and matrix multiplication

np.array([[1,2,3], [4,5,6]]).dot([[1], [2], [3]])
#array([[14],
#       [32]])

np.array([[1,2,3], [4,5,6]]).dot([1, 2, 3])
#array([14, 32])


np.matrix([[1,2,3], [4,5,6]])*[[1], [2], [3]]
#matrix([[14],
#        [32]])

np.matrix([[1,2,3], [4,5,6]])*[1, 2, 3]
#ValueError









