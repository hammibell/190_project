#!/usr/bin/env python
# coding: utf-8

# In[74]:


print("Name : ")


# In[75]:


#import the libraries
import pandas as pd 
import numpy as np
import matplotlib as plt 


#Task 1
#Read the bmi.csv
health = pd.read_csv("bmi.csv")
h = health.dropna()
health.head()


# In[71]:


#Task 2
#Data is sorted in descending order in accordance with BMI value
#Find the top 5 age group where the BMI value is the highest, and plot a bar graph out of it

h_star = health["Age"]


name = ("Age")
number = ("BMI Values")

h1 = h_star[1]
h2 = h_star[2]
h3 = h_star[3]
h4 = h_star[4]
h5 = h_star[5]

plt.xlabel(name)
plt.xticks(rotation = "vertical")
plt.ylabel(number)

plt.bar(name, number, color = ("red", "orange", "yellow", "green", "blue", "purple"), width = 0.5) #bar-grap
plt.show()


# In[23]:


#Task 3
#Read blood_pressure.csv
blood = pd.read_csv("blood_pressure.csv")
b = blood.dropna()
blood.head()


# In[73]:


#Task 4
#Data is sorted in ascending order in accordance with Blood Pressure
#Find the top 5 age group where the BloodPressure value is the highest, and plot a bar graph out of it

b_star = blood["Age"]

b1 = b_star[762]
b2 = b_star[763]
b3 = b_star[764]
b4 = b_star[765]
b5 = b_star[766]

plt.xlabel("Age")
plt.xticks(rotation = "vertical")
plt.ylabel("Blood Pressure Values")

plt.bar(name, number, color = ("red", "orange", "yellow", "green", "blue", "purple"), width = 0.5) #bar-grap
plt.show()






# In[78]:


#Task 5
#Read the insulin.csv

insulin = pd.read_csv("insulin.csv")
insulin.head()


# In[95]:


#Task 6
#Data is sorted in descending order in accordance with Insulin value
#Find out what will be the Glucose and BMI value when the Insulin is highest

i_star = insulin["Insulin"]

i1 = i_star[4]
i2 = i_star[3]
i3 = i_star[2]
i4 = i_star[1]
i5 = i_star[0]

print(i1, i2, i3, i4, i5)
print("#1", "#2", "#3", "#4", "and #5")

bmi = insulin["BMI"]
bmi_value = bmi[0]

print(bmi_value)
print("BMI value at the highest insulin value")






# In[ ]:





# In[ ]:




