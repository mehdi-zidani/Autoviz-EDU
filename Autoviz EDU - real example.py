#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://pypi.org/project/autoviz/ 
# downloaded package using the following line of code in terminal
# pip3 install autoviz --user 

import pandas as pd

from autoviz.AutoViz_Class import AutoViz_Class

AV = AutoViz_Class() #creating an instance of autoviz object


# In[2]:


data = pd.read_csv('D:\\Users\\mehdi.zidani\\OneDrive - MHCLG\\Documents\\Dataset for SDU.csv') #importing dataset on csv into dataframe


# In[5]:


df = AV.AutoViz(filename="" ,dfte=data, chart_format ="html", save_plot_dir = 'D:\\Users\\mehdi.zidani\\OneDrive - MHCLG\\Documents\\Charts')


# In[ ]:




