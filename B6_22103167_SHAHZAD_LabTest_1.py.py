#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from scipy import *
import matplotlib.pyplot as plt


# In[7]:


cities = np.array(['City X', 'City Y', 'City Z'])


# In[8]:


CityX = np.array([100, 120, 85, 90, 110, 95])
CityY = np.array([80, 75, 60, 95, 85, 90])
CityZ = np.array([150, 140, 135, 160, 155, 170])
Total_X = np.sum(CityX)
Total_Y = np.sum(CityY)
Total_Z = np.sum(CityZ)

avg_X, avg_Y, avg_Z = Total_X/6, Total_Y/6, Total_Z/6

print(f"Total Rainfall:\n \t City X= {Total_X}\n \t City Y= {Total_Y}\n \t City Z= {Total_Z}\n")
print(f"Average Rainfall: \n \t City X= {avg_X}\n \t City Y= {avg_Y}\n \t City Z= {avg_Z}\n")


# In[25]:



def avg_rain_over_all_cities(cities) :
    print("Monthly Average over all cities: \n")
    monthly = []
    for i in range(0,6):
        avg= (CityX[i]+CityY[i]+CityZ[i])/3
        print(f"\t Month {i+1} = {avg}\n")
        monthly.append(avg)
    return monthly
trend = np.array(avg_rain_over_all_cities(cities))


# In[45]:



plt.plot(np.arange(1,7,1), CityX,  'g.-', markersize=12, label="City X")
plt.plot(np.arange(1,7,1), CityY,  'b.-', markersize=12, label="City Y")
plt.plot(np.arange(1,7,1), CityZ,  'r.-', markersize=12, label="City Z")
plt.legend()
plt.title("Monthly Trend")
plt.xlabel("Month")
plt.ylabel("Monthly Rainfall")
plt.show()


# In[51]:


maxi_X, mini_X = np.max(CityX), np.min(CityX)
maxi_Y, mini_Y = np.max(CityY), np.min(CityX)
maxi_Z, mini_Z = np.max(CityZ), np.min(CityX)
    
print(f"Range in Rainfall:\n \t City X= {maxi_X-mini_X}\n \t City Y= {maxi_Y-mini_Y}\n \t City Z= {maxi_Z-mini_Z}\n")

ranges = []
ranges.append(maxi_X-mini_X)
ranges.append(maxi_Y-mini_Y)
ranges.append(maxi_Z-mini_Z)

plt.bar(cities, ranges)

