#%%
import pandas as pd
df2 = pd.read_csv('C:\Users\Vrishabh\Desktop\Aegis\Python\input.csv',header=None)
df2

df3 = pd.read_csv('C:/Users/Vrishabh/Desktop/Aegis/Python/train.csv',header=None)
df3

df4 = pd.read_html('https://www.safaribooksonline.com/library/view/python-for-data/9781449323592/ch04.html',header=0)
df4

#%%
dates = pd.date_range('20100101', periods = 10, freq = 'M')
df = pd.DataFrame(np.random.randn(10,4), index = dates, columns = list('ABCD'))
df.to_csv('C:/Users/Vrishabh/Desktop/Aegis/Python/dates.csv',sep = '\t')

#%%
from pandas import ExcelWriter
df = pd.DataFrame(np.random.randn(10,4), index = dates, columns = list('ABCD'))
writer = ExcelWriter('C:/Users/Vrishabh/Desktop/Aegis/Python/dates.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
s = pd.read_excel('C:/Users/Vrishabh/Desktop/Aegis/Python/dates.xlsx')

#%%




