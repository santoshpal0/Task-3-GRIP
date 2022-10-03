#!/usr/bin/env python
# coding: utf-8

# ### OBJECTIVE:
# #### To perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
# #### The task is to try to find out the weak areas where you can work to make more profit. And what all business problems can be derived by exploring the data.
# #### Importing all relevant Libraries

# In[1]:


# Importing the libraries
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


#importing the dataset
data =pd.read_csv("C:\\Users\\user\\Desktop\\SampleSuperstore.csv")
data.head()


# In[5]:


data.info()


# In[6]:


data.isnull().sum()


# In[7]:


#Check for dublicate values
data.duplicated().sum()


# In[8]:


#Remove those dublicate values
data.drop_duplicates(inplace=True)


# ### Statistical Details

# In[9]:


data.describe()


# ### State wise sales distribution

# In[10]:


fig,ax=plt.subplots(figsize=(30,12))
x=data['State']
y=data['Sales']
ax.set_xlabel('State')
ax.set_ylabel('Sales')
ax.set_title('State wise Sales distribution')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# #### On visualizing the data, we can see Florida has the highest sales and Kansas has lowest sales

# ### State wise profit distribution

# In[11]:


fig,ax=plt.subplots(figsize=(30,12))
x=data['State']
y=data['Profit']
ax.set_xlabel('State')
ax.set_ylabel('Profit')
ax.set_title('State wise Profit distribution')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# #### We can see that though every state has some amount of sales, but some states has to face negative profit.
# #### This has to be taken care of.
# ### Region wise sales distribution

# In[12]:


fig,ax=plt.subplots(figsize=(30,12))
x=data['Region']
y=data['Sales']
ax.set_xlabel('Region')
ax.set_ylabel('Sales')
ax.set_title('Region wise Sales distribution')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# ### We can see that the South region has most amount of sales and East has the lowest.

# ### Region wise profit distribution

# In[13]:


fig,ax=plt.subplots(figsize=(30,12))
x=data['Region']
y=data['Profit']
ax.set_xlabel('Region')
ax.set_ylabel('Profit')
ax.set_title('Region wise Profit distribution')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# ####  Surprisingly though South region has highest sales, but Central has most of the profits. For East region, it has lowest sales & lowest profit.

# ### Region wise category classification

# In[14]:


plt.figure(figsize = (30, 12))
sns.countplot(x = 'Category', hue = 'Region', data = data, palette = 'rocket')
plt.xticks(rotation = 45, fontsize = 20)
plt.yticks(fontsize = 20)
plt.xlabel('Categories', fontsize = 25)
plt.ylabel('', fontsize = 20)
plt.legend(loc = 5, fontsize = 20)


# ## Category wise sales distribution

# In[15]:


fig,ax=plt.subplots(figsize=(30,12))
x=data['Category']
y=data['Sales']
ax.set_xlabel('Category')
ax.set_ylabel('Sales')
ax.set_title('Category wise Sales distribution')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# ### we can see from the graph that technology have the highest sales 

# In[16]:


plt.figure(figsize=(17,8))
sns.barplot(x='Category',y='Profit',data=data,ci=False)


# ### Technology sector earns most of the profit and furniture sector earns the lowest profit.
# 

# ## Region wise sub-category classification

# In[17]:


plt.figure(figsize = (30, 12))
sns.countplot(x = 'Sub-Category', hue = 'Region', data = data, palette = 'magma')
plt.xticks(rotation = 45, fontsize = 20)
plt.yticks(fontsize = 20)
plt.xlabel('Sub-Categories', fontsize = 25)
plt.ylabel('', fontsize = 20)
plt.legend(loc = 5, fontsize = 20)


# ###  Sub-category wise sales distribution

# In[18]:


fig,ax=plt.subplots(figsize=(30,12))
x=data['Sub-Category']
y=data['Sales']
ax.set_xlabel('Sub-Category')
ax.set_ylabel('Sales')
ax.set_title('Sub-Category wise Sales distribution')

fig.autofmt_xdate()
ax.bar(x,y)
plt.show()


# ###  Sub-category wise profit distribution

# In[19]:


plt.figure(figsize=(17,8))
sns.barplot(x='Sub-Category',y='Profit',data=data,ci=False)


# ###  Most of the profit is earned by Copiers sector and least profit is earned by Fasteners.

# ##  Correlation between different variables

# In[20]:


sns.heatmap(data.corr(),annot=True)


# # Final Conclusion:
# ### East region is the weakest part in terms of sales and profit.
# ### Furniture sector has lowest profit and the lowest sales and if we look into sub-categories we will find that Fasteners has the lowest sales and earns the lowest profit. So, these are the weakest parts.

# In[ ]:




