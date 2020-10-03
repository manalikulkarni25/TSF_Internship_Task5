#!/usr/bin/env python
# coding: utf-8

# # Manali Kulkarni

# # Task-5: Exploratory Data Analysis
#      Objective is to perform 'Exploratory Data Analysis, on the provided dataset of 'SampleStore'.
#      
# If we are business owner of the retail firm and want to see how our company is performing. We are interested in finding out the weak areas where we can work to make more profit.

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


dataset=pd.read_csv('C:/Users/acer/Downloads/SampleSuperstore.csv')
dataset.shape


# In[11]:


dataset.head()


# In[13]:


#Data Preprocessing
dataset.isnull().sum().sum()
dataset.dtypes

There is no need of preprocessing is required as there are no null values and data types are correct.
# In[14]:


#Data Visualisation
sns.pairplot(dataset)
plt.show()


# In[23]:


plt.figure(1)
plt.subplot(221)
dataset['Category'].value_counts().plot.bar(figsize=(20,10),color='red',title='Category')
plt.subplot(222)
dataset['Segment'].value_counts().plot.bar(color='violet',title='Segment')
plt.subplot(223)
dataset['Ship Mode'].value_counts().plot.bar(color='green',title='Ship Mode')
plt.subplot(224)
dataset['Region'].value_counts().plot.bar(color='yellow',title='Region')
plt.show()
    

We can observe from above plots, Most of the Category are Supplies,Most of the segment are consumer,Most of the Ship Mode are standard class,Region is distributed but maximum is from west region.
# In[40]:


dataset.plot(kind='scatter',x='Profit',y='Sales',figsize=(14,8),color='green')
sns.regplot('Sales','Profit',data=dataset,color='red')
plt.show()

From above Scatter & Regplot,Profit is not wholely depend upon Sales. There are many other factors depend upon it.
# In[36]:


dataset.plot(kind='scatter',x='Quantity',y='Profit',figsize=(12,6),color='brown')
plt.show()


# In[35]:


sns.catplot(x="Sub-Category",y="Profit",data=dataset,color='Blue',height=4,aspect=4);


# From above Catplot, It can be viewed that Binders are highly variable and copiers earns maximum Profit.

# In[39]:


dataset.plot.scatter('Discount','Profit',figsize=(12,6),color='black')
plt.show()


# In[ ]:


Conclusion: We have derived all business problem using exploratory data analysis for this data. 


# # Thank You!! 
