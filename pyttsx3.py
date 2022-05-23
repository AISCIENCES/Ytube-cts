#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install pyttsx3')


# In[3]:


import pyttsx3


# In[4]:


friend = pyttsx3.init()


# In[10]:


friend.say("Im here for you.You are really good")


# In[11]:


friend.runAndWait()


# In[ ]:




