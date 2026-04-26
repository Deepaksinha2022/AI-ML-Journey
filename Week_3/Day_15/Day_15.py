#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Day - 15
## Block 1 of Hour 1

## use regression model
import pandas as pd
df=pd.read_csv("house_price_v6_final.csv")
df.head()

X = df.drop('target',axis=1)
y = df['target']

## Train tesr split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42)

## Train Module
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

## compare results
import pandas as pd

results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

print(results.head())


# In[11]:


## Basic error check
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)


# In[19]:


## Block 6
## Residual - diff between actual and predicted value
## psoitive residue - unerpredicted
## neg residue - over predicted
## Residual = y-y^
## sum((y-y^)**2)  = mean ssquared error
# Good model - no pattern in residual, scattered
# bad model - pattern inresidual, curve or trend

residuals = y_test - y_pred

## Visualisation 
import matplotlib.pyplot as plt

plt.scatter(y_pred, residuals)
plt.axhline(0, color='red')
plt.xlabel("Predicted")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()


# In[ ]:


## Baseline Modle
## A simple model used as a reference point
## it answers is my model better than 
# something very simple model

# Your model MSE = 50,000  
# Baseline MSE = 60,000 → Good ✔  

# Your model MSE = 50,000  
# Baseline MSE = 40,000 → Bad ❌

## type of baseline
## Mean Baseline

## Predit average of target
y_mean = y_train.mean()
y_pred_baseline = [y_mean]*len(y_test)

# evaluate baseline
from sklearn.metrics import mean_squared_error

## COmpute baseline error
mse_baseline = mean_squared_error(y_test, y_pred_baseline)
print("Baseline MSE:", mse_baseline)

## Compare with model
print("Model MSE:", mse)
print("Baseline MSE:", mse_baseline)

# 📌 Interpretation
# Case	Meaning
# Model < Baseline	Good ✔
# Model ≈ Baseline	Weak ⚠
# Model > Baseline	Bad ❌


# In[11]:


## Hour 7

## Problem 1 - Minimum Size Subarray Sum
# Problem

# Given an array and a target, find the minimum 
# length subarray whose sum ≥ target

# Example
nums = [2,3,1,2,4,3]
target = 7
# Output = 2   (subarray [4,3])
def minSubArrayLen(target, nums):
    left = 0
    curr_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len   


# In[14]:


## Product of array except self
nums = [1,2,3,4]
Output = [24,12,8,6]

def prod_array(nums):
    prod =[]
    for i in range(len(nums)):
        mul = 1
        for j in range(len(nums)):
            if i!=j:
                mul=mul*nums[j]
        prod.append(mul)
    return prod
print(prod_array(nums))   

