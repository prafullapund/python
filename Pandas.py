#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:10:41 2017

@author: Prafull
"""


import pandas as pd
import numpy as np

#series one dimensional array
d=[1,2,3,4,5,6,7]
day=['m','t','w','t','f','s','ss']
s=pd.Series(d,index=day)
s
s['marks']=555

df1=pd.DataFrame(d,index=day)
df1.columns=['fffg']
df1['marksss']=3333
s2={'a':123,'b':456,'c':789}
df=pd.Series(s2)


#Date frame 2d Array
df=pd.DataFrame({'AAA': [4,5,6,7],'BBB':[10,20,30,40], 'CCC':[100,50,-39,-49]})

df.loc[0,:]
df.loc[0:2,:]
df.loc[:,'AAA']

df.iloc[0:2,0:1]
df.iloc[:,[0,2]]

df.ix[1,'AAA']
df.ix[0:2,0:2]
df.ix[[1,2],['BBB','CCC']]
df.columns

#update
df.loc[1,'AAA']=9
df.loc[3]={11,22,333}

#date time series
dates=pd.date_range('20100101',periods=10,fre='M')
dff3=pd.DataFrame(np.random.randn(10,4),index=dates,columns=list('ABCD'))
dff3.dtypes
dff3.describe()
dff3.T
dff3.sort_values(by='B',ascending=False)
dff3['A']
dff3.iloc[0:2,]

#groupby
a=pd.DataFrame({'A':['f','f','f','q','q','q','q'],'B':['one','two','one','three','one','three','one'],'C':np.random.randn(7),'D':np.random.randn(7)})

print a
print a.groupby('A').sum()

a.groupby(['A','B']).sum()

#merged
#Inner join - only matching values from primary key
#left Join - Only merged left and right side will be null
#Right Join - Only merged Right and left side will be null

a=pd.DataFrame({'year':[2001,2002,2003,2004],'int_rate':[2,3,4,5],'ud_Gdp':[33,455,666,77]})
aa=pd.DataFrame({'year':[2001,2003,2004,2005],'unempl':[442,444,554,5], 'gdp' :[313,4555,6566,7117]})
merged=pd.merge(a,aa,on='year',how='left')
merged.set_index('year',inplace=True)
merged

import pandas as pd
import numpy as np

aa=pd.DataFrame({'Paris':[0,3,6],'Berlin':[1,7,4],'Madrid':[2,5,8]},index=d)
d=['b','a','c']

aa.sort_index(by='Berlin')#with sort_index only indexing will get sorted
aa.sort_index(axis=0)#0 for rows and 1 for columns
aa.ix['a',:]
aa.sum(axis=1)
aa.sum(axis=0)
aa.cov()
aa.describe()
aa.corr()
f=lambda x: math.sqrt(x)
aa.applymap(f)
aa.Berlin=aa['Berlin'].map(f)


























