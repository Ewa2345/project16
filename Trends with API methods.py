#!/usr/bin/env python
# coding: utf-8

# # Trends with API methods
# 

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


from pytrends.request import TrendReq
from matplotlib import pyplot as plt


# In[4]:


pytrends = TrendReq(hl='en-US', tz=360)


# With these two lines of code, connecting the Google Trends is possible. “hl” stands for “Host Language” while “tz” stands for “time zone”. Google uses Central Standard Time, CST for time management. So while using PyTrends, we need to use CST instead of Coordinated Universal Time, UTC.

# ##  Topic - Sports

# ### United States

# To pull data from the Google Trends, we need to determine which keywords we want to pull data about. To state that, we will create a variable below:

# In[5]:


sport_list_US = ['hockey ','football','basketball']
pytrends.build_payload(sport_list_US, cat=0, timeframe='today 5-y', geo='US', gprop='')


# In[6]:


b=pytrends.interest_over_time()
b.plot(figsize=(14,6))
plt.title('Interest over time for US');


# In[ ]:





# ### Historical Hourly Interest  for US

# In[7]:


bb=pytrends.get_historical_interest(sport_list_US, year_start=2019, month_start=1, day_start=1, hour_start=0, year_end=2019, month_end=11, day_end=1, hour_end=23, cat=0, geo='US', gprop='', sleep=0)


# In[8]:


bb.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for US');


# ### United Kingdom
# 

# In[42]:


sport_list_UK = ['hockey ','football','basketball']
pytrends.build_payload(sport_list_UK, cat=0, timeframe='today 5-y', geo='GB', gprop='')


# In[43]:


pytrends.interest_over_time()


# In[44]:


b=pytrends.interest_over_time()
b.plot(figsize=(14,6))
plt.title('Interest over time for UK');


# ###   Historical Hourly Interest  for UK

# In[45]:


bb=pytrends.get_historical_interest(sport_list_UK, year_start=2019, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=2, day_end=1, hour_end=0, cat=0, geo='GB', gprop='', sleep=0)


# In[46]:


bb.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for UK');


# ### Poland
# 

# In[50]:


sport_list_PL = ['hockey ','football','basketball']
pytrends.build_payload(sport_list_PL, cat=0, timeframe='today 5-y', geo='PL', gprop='')


# In[51]:


b=pytrends.interest_over_time()
b.plot(figsize=(14,6))
plt.title('Interest over time for PL');


# ### Historical Hourly Interest  for PL

# In[52]:


bb=pytrends.get_historical_interest(sport_list_PL, year_start=2019, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=2, day_end=1, hour_end=0, cat=0, geo='PL', gprop='', sleep=0)


# In[53]:


bb.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for PL');


# ## Topic - Politics

# ### United States

# #### last 3 months

# In[54]:


politics_list_US = ['biden ','elections','trump']
c=pytrends.build_payload(politics_list_US, cat=0, timeframe='today 3-m', geo='US', gprop='')


# In[55]:


c=pytrends.interest_over_time()
c.plot(figsize=(14,6))
plt.title('Interest over time fo US');


# ### Historical Hourly Interest for US

# In[56]:


cc=pytrends.get_historical_interest(politics_list_US, year_start=2019, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=2, day_end=1, hour_end=0, cat=0, geo='US', gprop='', sleep=0)


# In[57]:


cc.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for US');


# ### United Kingdom

# #### last 3 months

# In[58]:


politics_list_UK = ['biden ','elections','trump']
c=pytrends.build_payload(politics_list_UK, cat=0, timeframe='today 3-m', geo='GB', gprop='')


# In[60]:


c=pytrends.interest_over_time()
c.plot(figsize=(14,6))
plt.title('Interest over time for UK');


# ### Historical Hourly Interest for UK

# In[61]:


dd=pytrends.get_historical_interest(politics_list_UK, year_start=2019, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=2, day_end=1, hour_end=0, cat=0, geo='GB', gprop='', sleep=0)


# In[62]:


dd.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for UK');


# ### Poland

# #### last 3 months

# In[63]:


politics_list_PL = ['biden ','elections','trump']
c=pytrends.build_payload(politics_list_PL, cat=0, timeframe='today 3-m', geo='PL', gprop='')


# In[65]:


c=pytrends.interest_over_time()
c.plot(figsize=(14,6))
plt.title('Interest over time for PL');


# ### Historical Hourly Interest for PL

# In[66]:


dd=pytrends.get_historical_interest(politics_list_PL, year_start=2019, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=2, day_end=1, hour_end=0, cat=0, geo='PL', gprop='', sleep=0)


# In[67]:


dd.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for PL');


# ## Health

# ### United States

# In[68]:


health_list_US = ['disease ','cancer','doctor']
e=pytrends.build_payload(health_list_US, cat=0, timeframe='today 5-y', geo='US', gprop='')


# In[69]:


e=pytrends.interest_over_time()


# In[71]:


e.plot(figsize=(14,6))
plt.title('Interest over time for US');


# ### Historical Hourly Interest for US
# 

# In[72]:


dd=pytrends.get_historical_interest(health_list_US, year_start=2019, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=2, day_end=1, hour_end=0, cat=0, geo='US', gprop='', sleep=0)


# In[73]:


dd.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for US');


# ### United Kingdom

# In[74]:


health_list_UK = ['disease ','cancer','doctor']
e=pytrends.build_payload(health_list_UK, cat=0, timeframe='today 5-y', geo='GB', gprop='')


# In[75]:


e=pytrends.interest_over_time()
e.plot(figsize=(14,6))
plt.title('Interest over time for UK');


# ### Historical Hourly Interest for UK

# In[76]:


dd=pytrends.get_historical_interest(health_list_UK, year_start=2019, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=2, day_end=1, hour_end=0, cat=0, geo='GB', gprop='', sleep=0)


# In[77]:


dd.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for UK');


# ###  Poland

# In[78]:


health_list_PL = ['disease ','cancer','doctor']
e=pytrends.build_payload(health_list_PL, cat=0, timeframe='today 5-y', geo='PL', gprop='')


# In[80]:


e=pytrends.interest_over_time()
e.plot(figsize=(14,6))
plt.title('Interest over time for PL');


# ### Historical Hourly Interest for PL

# In[97]:


dd=pytrends.get_historical_interest(health_list_PL, year_start=2020, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=1, day_end=1, hour_end=23, cat=0, geo='PL', gprop='', sleep=0)


# In[98]:


dd.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for PL');


# ## Celebrities

# ### United States

# In[10]:


cele_list_US = ['Lopez ','Meghan','Harry']
e=pytrends.build_payload(cele_list_US, cat=0, timeframe='today 3-m', geo='US', gprop='')


# In[11]:


e=pytrends.interest_over_time()
e.plot(figsize=(14,6))
plt.title('Interest over time for US');


# ### Historical Hourly Interest for US

# In[28]:


dd=pytrends.get_historical_interest(cele_list_US, year_start=2021, month_start=3, day_start=8, hour_start=0, year_end=2021, month_end=3, day_end=8, hour_end=23, cat=0, geo='US', gprop='', sleep=0)


# In[29]:


dd.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for US');


# ### United Kingdom

# In[22]:


cele_list_UK = ['Lopez ','Meghan','Harry']
e=pytrends.build_payload(cele_list_UK, cat=0, timeframe='today 3-m', geo='GB', gprop='')


# In[23]:


e=pytrends.interest_over_time()
e.plot(figsize=(14,6))
plt.title('Interest over time fo UK');


# ### Historical Hourly Interest for UK

# In[36]:


dd=pytrends.get_historical_interest(cele_list_UK, year_start=2021, month_start=3, day_start=8, hour_start=0, year_end=2021, month_end=3, day_end=8, hour_end=23, cat=0, geo='GB', gprop='', sleep=0)


# In[37]:


dd.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for UK');


# ### Poland

# In[38]:


cele_list_PL = ['Lopez ','Meghan','Harry']
e=pytrends.build_payload(cele_list_PL, cat=0, timeframe='today 3-m', geo='PL', gprop='')


# In[39]:


e=pytrends.interest_over_time()
e.plot(figsize=(14,6))
plt.title('Interest over time to PL');


# ### Historical Hourly Interest for PL

# In[42]:


dd=pytrends.get_historical_interest(cele_list_PL, year_start=2021, month_start=3, day_start=8, hour_start=0, year_end=2021, month_end=3, day_end=8, hour_end=23, cat=0, geo='PL', gprop='', sleep=0)


# In[43]:


dd.plot.area(figsize=(14,6))
plt.title('Historical Hourly Interest for PL');


# In[ ]:





# In[ ]:




