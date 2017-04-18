#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:35:28 2017

@author: Prafull
"""

#1.	Create a dictionary that contain ten student name and mark of 5 Subjects, display marks >50 students.
import pandas as pd
a=pd.DataFrame({'Amir': [40,50,60,70,80],'Bob':[40,20,30,80,50], 'Cirus':[100,50,30,90,20], 'Derik':[40,20,70,90,50], 'Raj':[40,50,70,30,60], 'Vishal':[60,80,90,60,40],'fil':[60,40,50,60,70],'Nil':[70,80,90,80,50],'Arjun':[30,40,50,60,70],'Kiran':[40,60,70,30,50]})
a[a>50]

#2.	Create Dataframe perform groupby operation animal and only display group of cat .
df = pd.DataFrame({'adult':['False','False','False','False','False','True','True'], 'animal':['cat','dog','cat','fish','dog','cat','cat'], 'size':['S','S','M','M','M','L','L'], 'weight':['8','10','11','1','20','12','12']})
df
df.groupby('animal').get_group('cat')


#3.	Demonstrate the .loc[],.iloc[],.ix[] take above dataframe as a input.
df = pd.DataFrame({'adult':['False','False','False','False','False','True','True'], 'animal':['cat','dog','cat','fish','dog','cat','cat'], 'size':['S','S','M','M','M','L','L'], 'weight':['8','10','11','1','20','12','12']})
df
df.loc[0,:]
df.loc[0:2,:]
ss=df.loc[:,'adult']

qq=df.iloc[0:2,0:1]
df.iloc[:,[0,2]]

df.ix[1,'adult']
df.ix[0:2,0:2]
df.ix[[1,2],['animal','size']]
df.columns

#4 Demonstrate join, merge and append,concat operation. 

a=pd.DataFrame({'Eid':[1,2,3],'Ename':['Brijesh','Pratik','Raftar'],'Did':[10,30,50]}, index=['a','b','c'])
aa=pd.DataFrame({'Did':[10,30,40],'Dname':['IPF','HR','TIS']},index=['a','b','c'])
re=a.join(aa,how='outer')
res=a.join(aa,how='inner')
merged=pd.merge(a,aa,on='Did',how='left')
merged
merged1=pd.merge(a,aa,on='Did',how='right')
merged1

a.append(aa)

fr=(a,aa)
pd.concat(fr)


#5.Take snsdata.csv file as input perform Data Exploration , Data cleaning task,sort values of age column.
import matplotlib.pyplot as plt
import numpy as np

sns=pd.read_csv("/Users/Prafull/Desktop/Prafulla/Aegis/Machine Learning/snsdata.csv")
print (sns.head(3))

fig=plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(sns['age'],sns['drunk'])
plt.xlabel('age')
plt.ylabel('drunk')
plt.show()

fig=plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(sns['age'],bins = 2)

ax = fig.add_subplot(100,100,100)
ax.hist(sns['age'],bins = 5)
p = plt.show()
p


df.isnull()
meanAge = np.mean(sns.age) 
dfage = sns.age.fillna(meanAge)
g='M'
grouped = sns.groupby('gender')
dfage = sns.gender.fillna(g)

print( sns.sort(['age','friends'], ascending=[True, False]))


















