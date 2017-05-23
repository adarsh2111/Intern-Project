
# coding: utf-8

# In[256]:

#Python 3.5


# In[257]:

import os
import xlrd


# In[258]:

import pandas as pd


# In[259]:

import numpy as np


# In[260]:

import openpyxl


# In[261]:

os.chdir('C:\\Users\\user\\Desktop\\Ninjacart')


# In[262]:

price=pd.ExcelFile('C:\\Users\\user\\Desktop\\Ninjacart\\Pricing File - 17thMay.xlsx')


# In[263]:

mprice=price.parse('MarketPrice',skiprows=1)


# In[264]:

mpriced=pd.DataFrame(mprice)


# In[265]:

mpriced


# In[311]:

f_Retail=[]
f_Wholesale=[]

for i in range(0,mpriced['SKUName'].count()):
        if (mpriced['SKUClassification'][i]=="Leaves"):
            f_Wholesale.append(mpriced['T-1 WS'][i])
        else:
            if(mpriced['WS1'][i]==mpriced['T-1 WS'][i]):
                f_Wholesale.append(mpriced['WS1'][i])
            elif (mpriced['WS2'][i]==mpriced['T-1 WS'][i]):
                                                   f_Wholesale.append(mpriced['WS2'][i])
            elif(mpriced['GRN_Price'][i]!='-'):
                if (mpriced['WS1'][i]>int(mpriced['GRN_Price'][i])):
                    small_ws=mpriced['WS1'][i]
                elif mpriced['WS2'][i]>int(mpriced['GRN_Price'][i]):
                    small_ws=mpriced['WS1'][i]
                elif mpriced['WS3'][i]>int(mpriced['GRN_Price'][i]):
                    small_ws=mpriced['WS3'][i]
                elif mpriced['WS4'][i]>int(mpriced['GRN_Price'][i]):
                    small_ws=mpriced['WS4'][i]
                
                if mpriced['WS1'][i] > int(mpriced['GRN_Price'][i]) :
                    small_ws=min(mpriced['WS1'][i],small_ws)
                if mpriced['WS2'][i] >int(mpriced['GRN_Price'][i]):
                    small_ws = min(mpriced['WS2'][i],small_ws)
                if mpriced['WS3'][i]>int(mpriced['GRN_Price'][i]):
                    small_ws = min(mpriced['WS3'][i],small_ws)
                if mpriced['WS4'][i]>int(mpriced['GRN_Price'][i]):
                    small_ws = min(mpriced['WS4'][i],small_ws)
                if(mpriced['GRN_Price'][i]!='-'):
                    if ((int(small_ws)-int(mpriced['GRN_Price'][i]))>=5):
                        f_Wholesale.append(small_ws)
                    else:
                        f_Wholesale.append(0)
                else:
                    f_Wholesale.append(small_ws)
            elif(mpriced['GRN_Price'][i]=='-'):
                f_Wholesale.append(mpriced['WS1'][i])
            
                    
for i in range(0,mpriced['SKUName'].count()):
        if (mpriced['SKUClassification'][i]=="Leaves"):
            f_Retail.append(mpriced['T-1 NC_Retail'][i])
        else:
            if(mpriced['Retail1'][i]==mpriced['T-1 NC_Retail'][i]):
                f_Retail.append(mpriced['Retail1'][i])
            elif (mpriced['Retail2'][i]==mpriced['T-1 NC_Retail'][i]):
                                                   f_Retail.append(mpriced['Retail2'][i])
            elif(mpriced['GRN_Price'][i]!='-'):
                if mpriced['Retail1'][i]>int(mpriced['GRN_Price'][i]):
                    small=mpriced['Retail1'][i]
                elif mpriced['Retail2'][i]>int(mpriced['GRN_Price'][i]):
                    small=mpriced['Retail2'][i]
                elif mpriced['Retail3'][i]>int(mpriced['GRN_Price'][i]):
                    small=mpriced['Retail3'][i]
                elif mpriced['Retail4'][i]>int(mpriced['GRN_Price'][i]):
                    small=mpriced['Retail4'][i]
                
                if mpriced['Retail1'][i] > int(mpriced['GRN_Price'][i]):
                    small=mpriced['Retail1'][i]
                if mpriced['Retail2'][i] > int(mpriced['GRN_Price'][i]):
                    small = min(mpriced['Retail2'][i],small)
                if mpriced['Retail3'][i]>int(mpriced['GRN_Price'][i]):
                    small = min(mpriced['Retail3'][i],small)
                if mpriced['Retail4'][i]>int(mpriced['GRN_Price'][i]):
                    small = min(mpriced['Retail4'][i],small)
                if(mpriced['GRN_Price'][i]!='-'):
                    if ((int(small)-int(mpriced['GRN_Price'][i]))>=5):
                        f_Retail.append(small)
                    else:
                        f_Retail.append(0)
                else:
                    f_Retail.append(small)
                    
            elif(mpriced['GRN_Price'][i]=='-'):
                f_Retail.append(mpriced['Retail1'][i])
            



# In[312]:

f_Retail




# In[313]:

f_Wholesale


# In[314]:

f_Wholesale=pd.DataFrame(f_Wholesale)
f_Wholesale.to_csv('Wholesale.csv')


# In[ ]:



