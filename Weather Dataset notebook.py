#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv('weather data.csv')


# In[4]:


data


# In[12]:


data.index


# In[13]:


data.columns


# In[14]:


type(data)


# In[17]:


data.dtypes


# In[18]:


data['Weather'].unique()


# In[19]:


data.nunique()


# In[21]:


data['Weather'].count()


# In[24]:


data['Weather'].value_counts()


# In[25]:


data.info()


# In[16]:


data['Wind Speed_km/h'].unique()


# In[11]:


data['Wind Speed_km/h'].nunique() # Answer


# In[14]:


data['Weather'].nunique()


# In[23]:


data['Weather'].value_counts() # count values of excatly Weather clear 


# In[25]:


data[data['Weather'] == 'Clear'] # using syntax


# In[29]:


data.groupby('Weather').get_group('Clear') # using groupby method


# In[38]:


data['Wind Speed_km/h'].unique()


# In[39]:


data['Wind Speed_km/h'].value_counts() # Answer using value_counts()


# In[42]:


data.isna().any()  # Answer to find the null values


# In[44]:


data.isnull().sum()


# In[46]:


data.rename(columns = {'Weather':'Weather Condition'}, inplace=True)  # rename the column name


# In[47]:


data


# In[48]:


data['Visibility_km'].mean() # Answer to find the mean visibility


# In[49]:


data['Visibility_km'].describe()


# In[50]:


data['Weather Condition'].value_counts()


# In[54]:


data[data['Weather Condition'].str.contains('Snow')] # Answer to find snow in all rows


# In[58]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)] # Answer to find wind speed > 24 and visibility ==25


# In[64]:


data.groupby('Weather Condition').mean() # Answer all instances of weather conditions.


# In[65]:


data.groupby('Weather Condition').min() # min. value of each column against each weather condition 


# In[67]:


data.groupby('Weather Condition').max()# for max against each columns with Weather condition


# In[71]:


data[data['Weather Condition']== 'Fog']


# In[74]:


data['Weather Condition'].value_counts()


# In[77]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]


# In[79]:


data[((data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)] 


# In[ ]:




