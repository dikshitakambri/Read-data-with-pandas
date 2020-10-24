#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


a = [360,450,770,880]
print(a)


# In[3]:


b = pd.Series(a,name='series')


# In[4]:


print(b)


# In[5]:


b.index = pd.date_range('20280818',periods=4)


# In[7]:


print(b)


# In[8]:


print(b[2])


# In[9]:


print(b['2028-08-20'])


# In[10]:


b = b.astype(float)
print(b.dtype)


# In[11]:


c = b[1:3]
print(c)


# In[12]:


d = [20,None, 30,40]


# In[13]:


data = list(zip(a,b,d))
frame = pd.DataFrame(data)
print(frame)


# In[14]:


frame = pd.DataFrame(data,index=pd.date_range('20180815',periods=4),columns=['Walking','Running','Cycling'])
print(frame)


# In[15]:


g = frame.iloc[3]
print(g)


# In[ ]:




