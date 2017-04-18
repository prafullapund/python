#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 18:31:53 2017

@author: Prafull
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 14:32:45 2017

@author: Prafull
"""

#Assignment No1

#1	What is 7 to the power of 4?
pow(7,4)
7**4

#2	Split this string:"Hi there Sam!"

sp="Hi there Sam!"
sp.split()

#3	Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. 'Is there a dog here?'

d='Is there a dog here?'
d
e=d.split()
'dog'in (e)

#4	Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. “This dog runs faster than the other dog dude!”

d="This dog runs faster than the other dog dude!"
count=d.count('dog')
count
     
#5	You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket".
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.

def ticket(x,isBirthday):
    gift=0
    if isBirthday:
       gift=5 
    if x <= 60+gift: 
        print('No Ticket')
    elif x <= 80+gift:
        print('Small Ticket')
    elif x > 80:
        print ('Big Ticket')

ticket(65,1)        

#6	Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. 
#For example:seq = ['soup','dog','salad','cat','great']

seq = ['soup','dog','salad','cat','great']
print filter(lambda x:x[0]!='s',seq)

#7	Write the code to create a list with seven colors of rainbow? 

import matplotlib
import numpy as np

X = [1,2,3,4]
Ys = np.array([[4,8,12,16],
      [1,4,9,16],
      [17, 10, 13, 18],
      [9, 10, 18, 11],
      [4, 15, 17, 6],
      [7, 10, 8, 7],
      [9, 0, 10, 11],
      [14, 1, 15, 5],
      [8, 15, 9, 14],
       [20, 7, 1, 5]])
nCols = len(X)  
nRows = Ys.shape[0]

colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(Ys)))

cs = [colors[i//len(X)] for i in range(len(Ys)*len(X))] 
Xs=X*nRows
matplotlib.pyplot.scatter(Xs,Ys.flatten(),color=cs)


#8	Write the code to add 2 string in 2 different ways? 
a='Prafulla'
b='Pund'
a+b
c=''.join(['Prafulla','Pund'])

#9	What is the easiest way to print the same string 10 times? 
a=['Prafulla']
repeat=a*10

#10	Write the code to add a value to an existing list? 
a=[1,2,3,4,5,6,7]
a.append(9)

#11	Write the code to covert temperature to Celsius to Fahrenheit using lambda function ?

celsius_to_fahrenheit = lambda x : x* 9/5 + 32
print celsius_to_fahrenheit(10)


#12	Write code to take input number of the user and tell if the even / odd 
def oe(x):
    if x%2==0:
        print('Number is even')
    else: 
        print('number is odd')    
oe(6)

#13	How to remove the 4th element of a list? 
a=[1,2,3,4,5,6]
a[4:5]
del(a[4])

#14	How to insert a value in a list in the 6th position? 

z=[1,2,3,4,5,6,7,8]
z[5]=1111

#15	Identify the following data types: 
A = (1, 2, 3)
#Tuple
 
B = [1,2,3]
#List
 
C = {'Name': 'Saikat', 'Age':49} 
#Dictionary

#16	Write the code to print numbers 1 to 100 using range? 
for i in range (1,101,1):
    print i

#17	How to display the output of a list in sorted order?
a=[1,3,4,5,6,7,4,2,33,4,5]
a.sort() 

#18	Which of the following data type is immutable? 
#Tuple 
#List
#String 

#Tuple and String

#19	How to delete all contents of a dictionary
a={'key':'Number','key1':'Name'}
a.clear()

#20	Write the code to display largest of three number

a=11
b=22
c=33

if a<b and b<c:
   print('c is largest')
elif a>b and a>c:
   print('a is largest')
else:
   print('b is largest') 
    








