#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[144]:


df1=pd.read_csv('C:/Users/Ritik Sharma/Downloads/Covid 19 Data Set/covid_19_india.csv', parse_dates=['Date'], dayfirst=True) # Dataset 1
df2=pd.read_csv('C:/Users/Ritik Sharma/Downloads/Covid 19 Data Set/covid_vaccine_statewise.csv')       # Dataset 2
df3=pd.read_csv('C:/Users/Ritik Sharma/Downloads/Covid 19 Data Set/StatewiseTestingDetails.csv')       # Dataset 3


# In[145]:


df1   ## Dataset 1 


# In[98]:


df1.head()


# In[99]:


df2


# In[100]:


df3


# In[101]:


import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sns
import datetime as dt
import numpy as np


# In[102]:


df1.head()


# In[103]:


df1.shape


# In[104]:


print(df1['State/UnionTerritory'].unique())


# In[105]:


print(df1['ConfirmedIndianNational'].unique())


# In[106]:


print(df1['ConfirmedForeignNational'].unique())


# In[107]:


df1.head(10)


# ## Checking Null or Missing Values

# In[108]:


df1.isnull().sum()


# ### Understanding the pattern and making changes in Dataset

# In[109]:


df1 = df1[['Date', 'State/UnionTerritory','Cured','Deaths','Confirmed']] # Keeping only Important columns


# In[110]:


df1 = df1.rename(columns={'State/UnionTerritory': 'State'})


# In[111]:


df1.head()  # Earlier Dates


# In[112]:


df1.tail()  # Latest Dates


# ## Analysis

# In[113]:


#Random date
Random_Day = df1[df1.Date == '2021-05-19']


# In[114]:


Random_Day


# In[115]:


#Sorting of Random_Day data in descending order with respect to confirmed cases
max_confirmed_cases=Random_Day.sort_values(by="Confirmed",ascending=False)
max_confirmed_cases


# In[116]:


#Taking top 5 states with maximum number of confirmed cases
top_states_confirmed=max_confirmed_cases[0:5]


# In[117]:


top_states_confirmed


# In[118]:


#Making bar-plot for states with top confirmed cases
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x="State",y="Confirmed",data=top_states_confirmed,hue="State")
plt.show()


# In[119]:


#Sorting data with number of death cases
max_death_cases=Random_Day.sort_values(by="Deaths",ascending=False)
max_death_cases


# In[120]:


#Taking states with maximum number of death cases
top_states_death=max_death_cases[0:5]


# In[121]:


top_states_death


# In[122]:


#Making bar-plot for states with top death cases
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x="State",y="Deaths",data=top_states_death,hue="State")
plt.show()


# In[123]:


#Sorting data with respect to number of cured cases
max_cured_cases=Random_Day.sort_values(by="Cured",ascending=False)
max_cured_cases


# In[124]:


#Taking states with maximum number of cured cases
top_states_cured=max_cured_cases[0:5]


# In[125]:


#Making bar-plot for states with top cured cases
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x="State",y="Cured",data=top_states_cured,hue="State")
plt.show()


# ## Maharashtra

# In[136]:


MH = df1[df1.State == 'Maharashtra']


# In[137]:


MH


# ## Visualizing confirmed cases in maharashtra

# In[138]:


sns.set(rc={'figure.figsize':(20,10)})
sns.lineplot(x="Date",y="Confirmed",data=MH,color="b")
plt.show()


# ## Visualizing death cases in maharashtra

# In[139]:


sns.set(rc={'figure.figsize':(20,10)})
sns.lineplot(x="Date",y="Deaths",data=MH,color="r")
plt.show()


# ## Delhi

# In[126]:


DL = df1[df1.State == 'Delhi']


# In[127]:


DL


# ## Visualizing confirmed cases in Delhi

# In[129]:


sns.set(rc={'figure.figsize':(20,10)})
sns.lineplot(x="Date",y="Confirmed",data=DL,color="b")
plt.show()


# ## Visualizing death cases in Delhi

# In[131]:


sns.set(rc={'figure.figsize':(20,10)})
sns.lineplot(x="Date",y="Deaths",data=DL,color="r")
plt.show()


# ## Uttar Pradesh

# In[141]:


UP = df1[df1.State == 'Uttar Pradesh']
UP


# ## Visualizing confirmed cases in Uttar Pradesh

# In[142]:


sns.set(rc={'figure.figsize':(20,10)})
sns.lineplot(x="Date",y="Confirmed",data=UP,color="b")
plt.show()


# ## Visualizing Death Cases in Uttar Pradesh

# In[143]:


sns.set(rc={'figure.figsize':(20,10)})
sns.lineplot(x="Date",y="Deaths",data=UP,color="r")
plt.show()


# In[51]:


df1.describe()


# In[52]:


df1[df1.State=='Delhi'].describe()    # Individual State Delhi


# In[53]:


df1[df1.State=='Kerala'].describe()    # Individual State Kerala


# In[55]:


df1[df1.State=='Maharashtra'].describe()    # Individual State Maharashtra


# In[146]:


sns.pairplot(df1)


# In[ ]:




