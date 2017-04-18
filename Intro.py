
list1=[1,2,4,3]
list1
list1.append(5)
list1
list1.remove(3)
list1
list1.index(2)
list1
list1.pop(2)
list1
tuple_e=(1,2,3,4,5)
tuple_e[2]
dict={'name':'sachin','age':7}
dict

print sorted(list1)
list1.sort()
l=[1,2,3]
l2=[2,4,5]
l+l2

import pandas as pd
import numpy as np
import matplotlib as plt
df=pd.read_csv("/Users/Prafull/Desktop/Prafulla/Aegis/Python/Orientation on Python/Python Dataset/train.csv")
df
df.head(10)
df.tail
df.count
df.describe()
df['Property_Area'].value_counts()
df['Gender']
df['ApplicantIncome'].hist(bins=100)
temp1=df['Credit_History'].value_counts(ascending=True)
print temp1
temp2=df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x:x.map({'Y':1,'N':0}).mean())
temp2
df.apply(lambda x:sum(x.isnull()),axis=0)
df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)
df.apply(lambda x:sum(x.isnull()),axis=0)
df['Married'].fillna(df['Married'].mode(),inplace=True)
df.describe()
df['LoanAmount_log']=np.log(df['LoanAmount'])
from sklearn.preprocessing import LabelEncoder
var_mod=['Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
le=LabelEncoder()
for i in var_mod:
    df[i]=le.fit_transform(df[i])
df.dtypes
df.head(5)





























