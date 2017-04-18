#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 19:29:33 2017

@author: Prafull
"""
#write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
     if i < 5:
          print i

 #Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list         
new=[]
for i in a:
     if i < 5:
          new.append(i)
print new

#b)	Write this in one line of Python.

[i for i in a if i<5]


#c)	Ask the user for a number and return a list that contains only elements   from the original list a that are smaller than that number given by the user.
num = int(raw_input("Choose a number: "))
[i for i in a if i<num]


#2.a = [5, 10, 15, 20, 25, 30, 35, 40] Slice 20 and  25 using slicing.

a = [5, 10, 15, 20, 25, 30, 35, 40]
a[3:5]

#3 Write a Program to display Fibonacci series <1000 and value separated by commas.


a=0
b=1
newl=[]
while b < 1000:
     newl.append(b)
     a,b=b,a+b

print newl


#4 Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name=str(raw_input("Please enter name:"))
age=int(raw_input("Please enter age:"))

print (name+", You will turn 100 on :" + str(100-age+2017))



#5Ask the user for a string and print out whether this string is a palindrome or not. 
a=raw_input("Please enter string:")
b=a[::-1]
if a==b:
     print("String is palindrome")
else:
     print("String is not palindrome")     
     

#6 Use for loop to calculate the sum of 1, 2, 3, …, 100 odd number.
sum=0
for i in range(1,101):
     if i%2==1:
         sum=sum+i
print sum

#7Assign a string “GIS Programming” to a string variable. Print all the letters (in uppercase) line by line and calculate length and display in reverse order

a="GIS Programming"
a.upper()
len(a)
a[::-1]













