#!/usr/bin/env python
# coding: utf-8

# ### From 20th march to 24th march

# In[1]:


import numpy as np
import pandas as pd
from pytrends.request import TrendReq
from matplotlib import pyplot as plt
pytrends = TrendReq(hl='en-US', tz=360)
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


health_list_US = ['Żulczyk ','Duda','debil','sąd']

bb=pytrends.get_historical_interest(health_list_US, year_start=2021, month_start=3, day_start=21, hour_start=0, year_end=2021, month_end=3, day_end=24, hour_end=23, cat=0, geo='PL', gprop='', sleep=0)

bb.plot(figsize=(14,6))
plt.title('Historical Hourly Interest for PL');


# In[3]:


bb


# In[4]:


df = pd.DataFrame (bb)


# In[5]:


df[df['Duda'] > 90]


# ### Analysing variable - debil

# In[5]:


#descriptive statistics summary
df['debil'].describe()


# ### Analysing variable - Duda
# 

# In[6]:


df['Duda'].describe()


# In[7]:


df['sąd'].describe()


# In[8]:


sns.distplot(df['debil']);


# In[9]:


sns.distplot(df['Duda']);


# In[10]:


sns.distplot(df['sąd']);


# ### Kurtosis and skewness are statistics that characterize the shape and symmetry of the distribution. These statistics are displayed with their standard errors.

# ### For normal distribution, the kurtosis stat is zero. Positive kurtosis indicates that there are more positive outliers in the data than there is for a normal distribution. Negative kurtosis indicates the presence of closer outliers than in the normal distribution.

# ##### The normal distribution is symmetrical and its skewness value is 0. A highly positive skewness distribution has the long right end. When the skewness is negative, the distribution has the long left end. As a guideline, a skew value of more than twice its standard error generally indicates a deviation from the symmetry of the distribution.

# In[11]:


#skewness and kurtosis
print("Skewness: %f" % df['debil'].skew())
print("Kurtosis: %f" % df['debil'].kurt())


# In[12]:


#skewness and kurtosis
print("Skewness: %f" % df['Duda'].skew())
print("Kurtosis: %f" % df['Duda'].kurt())


# In[13]:


#skewness and kurtosis
print("Skewness: %f" % df['sąd'].skew())
print("Kurtosis: %f" % df['sąd'].kurt())


# In[14]:


plt.boxplot([x for x in [df['debil'],df['Duda'],df['sąd']]])
plt.show()


# In[15]:


#correlation matrix
corrmat = df.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);


# ### 1-4 march

# In[16]:


health_list_PL = ['Żulczyk ','Duda','debil','sąd']

bb=pytrends.get_historical_interest(health_list_PL, year_start=2021, month_start=3, day_start=1, hour_start=0, year_end=2021, month_end=3, day_end=4, hour_end=23, cat=0, geo='PL', gprop='', sleep=0)

bb.plot(figsize=(14,6))
plt.title('Historical Hourly Interest for PL');


# In[17]:


df = pd.DataFrame (bb)


# In[18]:


#descriptive statistics summary
df['debil'].describe()


# In[19]:


df['Duda'].describe()


# In[20]:


df['sąd'].describe()


# In[21]:


sns.distplot(df['debil']);


# In[22]:


sns.distplot(df['Duda']);


# In[23]:


sns.distplot(df['sąd']);


# In[24]:


#skewness and kurtosis
print("Skewness: %f" % df['debil'].skew())
print("Kurtosis: %f" % df['debil'].kurt())


# In[25]:


#skewness and kurtosis
print("Skewness: %f" % df['Duda'].skew())
print("Kurtosis: %f" % df['Duda'].kurt())


# In[26]:


#skewness and kurtosis
print("Skewness: %f" % df['sąd'].skew())
print("Kurtosis: %f" % df['sąd'].kurt())


# In[27]:


plt.boxplot([x for x in [df['debil'],df['Duda'],df['sąd']]])
plt.show()


# In[28]:


#correlation matrix
corrmat = df.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);


# In[ ]:




