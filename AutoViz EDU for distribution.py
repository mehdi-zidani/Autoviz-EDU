#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://pypi.org/project/autoviz/ 
# downloaded package using the following line of code in terminal
# pip3 install autoviz --user 

import pandas as pd

from autoviz.AutoViz_Class import AutoViz_Class

AV = AutoViz_Class() #creating an instance of Autoviz object


# In[2]:


data = pd.read_csv(#'in between the speech marks, enter the Data's location, be sure to include the ext for example.csv') #importing dataset on csv into dataframe


# In[5]:


df = AV.AutoViz(filename="" ,dfte=data, chart_format ="html", save_plot_dir = #'in-between the speech marks, specify where you would like the visulizations to be saved')


# In[ ]:




