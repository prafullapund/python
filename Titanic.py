import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier

tt=pd.read_csv("/Users/Prafull/Desktop/Prafulla/Aegis/Python/Orientation on Python/titanic/train.csv")
tt
tt.head()
tt['Gender']=tt['Sex'].map({'female':0,'male':1}).astype(int)
tt['Gender']

if len(tt.Embarked[tt.Embarked.isnull()])>0:tt.Embarked[tt.Embarked.isnull()]=tt.Embarked.dropna().mode().values

Ports=list(enumerate(np.unique(tt['Embarked']))) 
Ports_dict={name:i for i, name in Ports}

tt.Embarked=tt.Embarked.map(lambda x: Ports_dict[x]).astype(int)    
tt.Embarked   