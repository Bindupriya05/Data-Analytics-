#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[2]:


covid_df=pd.read_csv("/Users/alurubindu/Downloads/covid_india/covid_19_india.csv")


# In[3]:


covid_df.head(10)


# In[4]:


covid_df.info()


# In[5]:


covid_df.describe()


# In[6]:


vaccine_df=pd.read_csv("/Users/alurubindu/Downloads/covid_india/covid_vaccine_statewise.csv")


# In[7]:


vaccine_df.head()


# In[8]:


covid_df.drop(["Sno","Time","ConfirmedIndianNational","ConfirmedForeignNational"],inplace=True,axis=1)


# In[9]:


covid_df.head()


# In[10]:


covid_df['Date']=pd.to_datetime(covid_df['Date'],format='%Y-%m-%d')


# In[11]:


covid_df.head()


# In[12]:


#Active cases
covid_df['Active_cases']=covid_df['Confirmed']-(covid_df['Cured']+covid_df['Deaths'])
covid_df.tail()


# In[13]:


statewise=pd.pivot_table(covid_df,values=["Confirmed","Deaths","Cured"],index="State/UnionTerritory", aggfunc=max)


# In[14]:


statewise["Recovery_Rate"]=statewise["Cured"]*100/statewise["Confirmed"]


# In[15]:


statewise["Mortality_Rate"]=statewise["Deaths"]*100/statewise["Confirmed"]


# In[16]:


statewise=statewise.sort_values(by="Confirmed", ascending=False)


# In[17]:


statewise.style.background_gradient(cmap="cubehelix")


# In[18]:


#top 10 active cases in states
top10_Activecases=covid_df.groupby(by='State/UnionTerritory').max()[['Active_cases','Date']].sort_values(by=['Active_cases'],ascending=False).reset_index()


# In[19]:


fig=plt.figure(figsize=(16,9))


# In[20]:


plt.title("Top 10 states with the most active cases in india", size=25)


# In[21]:


ax=sns.barplot(data=top10_Activecases.iloc[:10],y="Active_cases",x="State/UnionTerritory",linewidth=2,edgecolor='red')


# In[22]:


top10_Activecases=covid_df.groupby(by='State/UnionTerritory').max()[['Active_cases','Date']].sort_values(by=['Active_cases'],ascending=False).reset_index()
fig=plt.figure(figsize=(16,9))
plt.title("Top 10 states with the most active cases in india", size=25)
ax=sns.barplot(data=top10_Activecases.iloc[:10],y="Active_cases",x="State/UnionTerritory",linewidth=2,edgecolor='red')
plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show()


# In[23]:


#Top states with highest deaths
top10_deaths=covid_df.groupby(by="State/UnionTerritory").max()[['Deaths','Date']].sort_values(by=['Deaths'],ascending=False).reset_index()
fig=plt.figure(figsize=(18,5))
plt.title("Top 10 states with highest deaths")
ax=sns.barplot(data=top10_deaths.iloc[:12],y="Deaths", x="State/UnionTerritory",linewidth=2,edgecolor='black')
plt.xlabel("States")
plt.ylabel("Total Death Cases")
plt.show()


# In[24]:


#Growth trend

# fig=plt.figure(figsize=(12,6))
# ax=sns.lineplot(data=covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu','Uttar Pradesh']), x= 'Date', y='Active_cases', hue='State/UnionTerritory'])
# ax.set_title("Top 5 Affected States in India",size=16)


# In[25]:



vaccine_df.head()


# In[26]:


vaccine_df.rename(columns={'Updated On': 'Vaccine_Date'}, inplace=True)


# In[27]:


vaccine_df.head()


# In[28]:


vaccine_df.info()


# In[29]:


vaccine_df.isnull().sum()


# In[34]:


vaccination=vaccine_df.drop(['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'], axis=1)


# In[35]:


vaccination.head()


# In[39]:


#male vs female vaccination

male=vaccination['Male(Individuals Vaccinated)'].sum()
female=vaccination['Female(Individuals Vaccinated)'].sum()
px.pie(names=["Male","Female"], values=[male,female],title="male and female vaccination")


# In[42]:


#Remove rows where state is India
vaccine=vaccine_df[vaccine_df.State!="India"]
vaccine


# In[48]:


vaccine.rename(columns={"Total Individuals Vaccinated" : "Total"},inplace=True)
vaccine.head()


# In[46]:


vaccine.head()


# In[65]:


#Most vaccinated states

max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac=max_vac.sort_values('Total', ascending=False)[:5]
max_vac


# In[52]:


fig=plt.figure(figsize=(10,5))
plt.title("Top 5 Vaccinated States in India", size=20)
x=sns.barplot(data=max_vac.iloc[:10],y=max_vac.Total,x=max_vac.index,linewidth=2,edgecolor='Black')
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()


# In[64]:


#leastst vaccinated states

low_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
low_vac=max_vac.sort_values('Total', ascending=True)[:5]
low_vac


# In[66]:


fig=plt.figure(figsize=(10,5))
plt.title("Least 5 Vaccinated States in India", size=20)
x=sns.barplot(data=low_vac.iloc[:10],y=low_vac.Total,x=low_vac.index,linewidth=2,edgecolor='Black')
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()


# In[ ]:




