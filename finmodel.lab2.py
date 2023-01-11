#!/usr/bin/env python
# coding: utf-8

# # input

# In[41]:


salary = 60000
savingsrate = 0.25
interestrate = 0.05
desiredcash = 1500000


# In[6]:


annualcash = salary * savingsrate


# In[8]:


print (annualcash)


# In[15]:


import numpy_financial as npf


# In[23]:


years_to_retirement = npf.nper(interestrate, -annualcash, 0, desiredcash)


# In[28]:


print  (years_to_retirement)


# # import our input

# In[30]:


input = [5,10,15]


# In[31]:


print (input)


# In[33]:


for item in input:
    new_value = item + 2
    print(new_value)


# # Get back to Martha's example

# In[36]:


investment_rate = [0.05, 0.06, 0.07]


# In[37]:


print (investment_rate)


# In[39]:


for i_rate in investment_rate:
    years_to_retirement = npf.nper(i_rate, -annualcash, 0, desiredcash)
    print (years_to_retirement)


# In[ ]:




