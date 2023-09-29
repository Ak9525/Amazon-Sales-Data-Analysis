#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv("Amazon.csv", encoding= "unicode_escape")


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.drop(["New",'PendingS'], axis=1, inplace=True)


# In[8]:


df.info()


# In[9]:


pd.isnull(df)


# In[10]:


pd.isnull(df).sum()


# In[11]:


df.shape


# In[12]:


df.dropna(inplace=True)


# In[13]:


df.shape


# In[14]:


df.columns


# In[15]:


df['ship-postal-code']=df['ship-postal-code'].astype('int')


# In[16]:


df['ship-postal-code'].dtype


# In[17]:


df['Date']=pd.to_datetime (df['Date'])


# In[18]:


df.info()


# In[19]:


df.columns


# In[20]:


df.rename(columns={'Qty':'Quantity'})


# In[21]:


#describe() method returns description of the data in the dataframe(i.e count,mean,std,min, etc)
df.describe()


# In[22]:


df.describe(include='object')


# In[23]:


#use describe()for specific columns
df[['Qty','Amount']].describe()


# In[ ]:





# # Exploratory Data Analysis

# In[24]:


df.columns


# In[25]:


ax=sns.countplot(x='Size', data=df) 


# In[26]:


ax=sns.countplot(x='Size', data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# Note: From above graph you can see that most of the people buys M-size.

# # Group By

# The Groupby() function in pandas is used to group data based on one or more columns in a Dataframe

# In[27]:


df.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by="Qty",ascending=False)


# In[28]:


S_qty = df.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by="Qty",ascending=False)

sns.barplot(x='Size', y='Qty',data=S_qty)


# Note: From above graph you can see that most of the Qty buys M-size in the sales

# # Courier Status

# In[29]:


sns.countplot(data=df, x='Courier Status',hue='Status')


# In[30]:


plt.figure(figsize=(10,10))

ax=sns.countplot(data=df, x='Courier Status', hue= 'Status')

plt.show()


# Note: From above graph the majority of the orders are shipped through the courier.

# In[31]:


#histogram
df['Size'].hist()


# In[32]:


df['Category']=df['Category'].astype(str)
column_data =df['Category']
plt.figure(figsize=(10,10))
plt.hist(column_data, bins=20, edgecolor='red')
plt.xticks(rotation=90)
plt.show()


# Note: From above graph you can see that most of the buyers are T-shirt.

# In[33]:


#Checking B2B data by using pie chart
B2B_check =df['B2B'].value_counts()

#Plot the pie chart
plt.pie(B2B_check, labels=B2B_check, autopct='%1.1f%%')

#plt.axis('equal')
plt.show()


# In[34]:


#Checking B2B data by using pie chart
B2B_check =df['B2B'].value_counts()

#Plot the pie chart
plt.pie(B2B_check, labels=B2B_check.index, autopct='%1.1f%%')

#plt.axis('equal')
plt.show()


# Note: From above chart we can see that maximum i.e.99.2% of buyers are retailers and 0.8% are B2B buyers.

# In[37]:


#prepare data for scatter plot
x_data =df["Category"]
y_data =df["Size"]

#Plot the scatter Plot
plt.scatter(x_data,y_data)
plt.xlabel("Category")
plt.ylabel("Size")
plt.title("Scatter plot")
plt.show()


# In[41]:


#Plot count of cities by state
plt.figure(figsize=(12,10))
sns.countplot(data=df, x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)

plt.show()


# In[43]:


#Top 10 States
top_10_state =df['ship-state'].value_counts().head(10)

#plot count of cities by state
plt.figure(figsize=(12,8))
sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)],x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=45)

plt.show()


# Note: From above graph you can see that most of the buyers are Maharashtra state

# # Conclusion

# The data analysis reveals that the business has a significant customer base in Maharashtra state,mainly serves retailers,fulfills orders through Amazon, experiences high demand for T-shirts and sees M-size as the preferred choice among buyers.

# In[ ]:




