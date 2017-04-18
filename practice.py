#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:32:03 2017

@author: Prafull
"""

x=input("enter the number:")
fact=1
if x<0:
    print("number is negative")
elif x==0:
    print("number is zero and fact is 1")
else:
    while(x>0):
        fact=fact*x
        x=x-1
    print(fact)        

    
n=[1,2,3,4,5,6]
for i in n:
    print i**2
    
a=range(1,100,5)    

r=[111,1,2,3,4,5]
r.append(22)# adding in last 22
r.insert(0,555)# adding 0th position 555
r.extend([3,2])# adding in last 3 and 2
r.remove(5) # removing the element/values
r.pop(0) # removing the given index 

r.sort()# sorting 

a=1,2,3,4
type(a)  
 
dict={'name':'Sachin','Age':12}

del dict['name'] # deleting key

dict.clear() # clearing the dictionary


# Function

def add(x):
    x=x+2
    print x

add(5);    

dec=2

print bin(dec)
print oct(dec)
print hex(dec)


# user define function
def greet(name):
    '''This function greets to the person '''
    print("hello,"+name+".good morning!")
greet('Paul');
    
def add(x,y):
    sum=x+y
    return sum

add(3,2)
    
def f(x):
    c=x**12
    return c
f(2)    

f=lambda x,y,z:x+y+z
f(1,1,2)

sum=lambda x,y:x+y

exp=lambda x:x**2
exp(3)

#map and lambda
cel=[39.5,35.6,34.56,65,44.33]
far=map(lambda x:(float(9)/5)*x+32,cel)
print far

# reduce and lambda

reduce(lambda x,y:x+y,[23,33,45,12,111])

reduce(lambda x,y,z:x+y+z,[12,33,44,66,77,88,222])

#filter and lambda 
#prime number
num=range(2,50)
for i in (2,8):
    num=filter(lambda x:x==1 or x%2!=0,num)
num
















