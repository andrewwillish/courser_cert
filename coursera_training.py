#!/usr/bin/env python
# coding: utf-8

# In[2]:


import yfinance as yf
import panda as pd


# In[3]:


tesla_data = yf.Ticker('TSLA')


# In[5]:


print (tesla_data)


# In[7]:


tesla_data_history = tesla_data.history(period='max')
tesla_data_history.head()


# In[8]:


tesla_data_history.tail()


# In[10]:


gme_data = yf.Ticker('GME')
gme_data.history(period='max').head()


# In[12]:


gme_revenue = gme_data.history(period='max').tail()
gme_revenue


# In[13]:


tesla_data_history.reset_index(inplace=True)
tesla_data_history.plot(x="Date", y="Open")


# In[20]:


gme_data_history = gme_data.history(period='max')
gme_data_history.make_graph()

