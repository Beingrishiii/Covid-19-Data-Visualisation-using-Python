#!/usr/bin/env python
# coding: utf-8

# # PROJECT - COVID 19

# ## IMPORTING LIBRARIES 

# ### TASK 1

# In[ ]:





# In[2]:


import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
print ('Modules are imported')


# In[ ]:





# ## TASK 1.1

# ### Loading the Dataset

# In[3]:


dataset_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(dataset_url)


# In[4]:


df.head()


# In[5]:


df.tail()


# ### Lets check the shape of the dataframe

# In[6]:


df.shape


# ## TASK 2.1

# ### Lets do some preprocessing

# In[7]:


df = df[df.Confirmed > 0]


# In[8]:


df.head()


# In[9]:


### Lets see the data related to a country for example Italy


# In[10]:


df[df.Country == 'Italy']


# ### Let's see Global spread of Covid 19

# In[11]:


fig = px.choropleth(df, locations = 'Country', locationmode= 'country names', color = 'Confirmed', animation_frame='Date')
fig.show()


# In[ ]:





# In[ ]:




