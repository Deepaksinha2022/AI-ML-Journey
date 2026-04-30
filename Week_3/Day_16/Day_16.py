#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ## Hour 1
# ## Block 1
# # Cost Function
# #- it measures how wrong the model is
# # it means it meausre the difference between actual and predicted value
# # and sees how far is predicted value from the actual value
# # model tries to minimise the error = y-y^ and it is like feedback signal to model

# ## Block 2
# # Mean Squared Error
# # MSE = (1/n)sum(y-y^)**2
# ## Squared to penalise large errors
# # Linear Regression - cost function - mse
# # for linear regression cost function is same as mse
# # Squareing make the function continous and differenciable
# # Helps in gradient descent 
# # optimise optimal weights

# ## Residual  - error per point
# ## MSE - average error
# # Cost function is what model tries to minimise

# ## Block 3
# ## During model training model starts somehwere on the curve and 
# # then tries to find the min cost downhill
# # Lowest point - global minima
# # Single mimina is required a no risk of getting wrong
# # minima and confuse between multiple solutions
# # 

# ## How to reach global minima
# # start at any weight and then move downward
# ## new wieght = old weight - small step*slope
# # small step - learning rate
# # Learning rate - small - too slow, 
# # Learning rate - big - weight overshoot

# ## Gardient - rate of change of cost w.r.t parameters 
# ## too high learnig=ng rate can overshoot and we may never 
# ## reach bottom and may diverge also

# ## Gradient represents the slope of the cost function with respect to parameters. 
# We move in the opposite direction of the gradient to minimize the cost. 
# If the learning rate is too large, the model may overshoot the minimum and fail to converge.



# Block 6
# Task 1
# Manual COst calculation
# Actual (y)     = [10, 20, 30]
# Predicted (ŷ)  = [12, 18, 33]
# 
# Residual - [10-12,20-18,30-33] = [-2,2,-3]
# Square - [4,4,9]
# MSE - (4+4+9)/3 = 5.67
# 
# Change Prediction - [11,19,31]
# 
# residual = [-1,-1,-1] , MSE = [1,1,1] - 3/3 = 1
# 
# Campare
# Prediction	     MSE
# First	         5.67
# Second	          1

# In[ ]:


## Code Version
from sklearn.metrics import mean_squared_error

y = [10, 20, 30]

y_pred1 = [12, 18, 33]
y_pred2 = [11, 19, 31]

print("MSE 1:", mean_squared_error(y, y_pred1))
print("MSE 2:", mean_squared_error(y, y_pred2))

# The second prediction is better because it has lower MSE, 
# meaning predictions are closer to actual values. 
# The model tries to minimize the cost function (MSE), which measures overall error. 
# Gradient helps by providing the direction to update weights 
# so that the cost decreases iteratively.


# Block 7
# Optimisation
# FInding parameters w,b that minimise the cost
# 
# We want to minimize:
# 
# J= 1/n ∑(y−y^)2
# 
# 👉 This is the cost (MSE)
# 
# Gradient descent update rule
# 
# $$ w = w - \alpha \cdot \frac{\partial J}{\partial w} $$
# 
# Learning
# Learning rate controls the step size of updates. 
# We subtract the gradient because it points toward increasing cost, so moving opposite reduces cost. 
# We stop updating when the model converges, i.e., cost changes become negligible.
# 

# In[2]:


import pandas as pd

data = {
    "Area": [500, 800, 1000, 1200, 1500, 1800],
    "Rooms": [1, 2, 2, 3, 3, 4],
    "Price": [100, 150, 180, 250, 300, 360]
}

df = pd.DataFrame(data)


# In[3]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X1 = df[["Area"]]   # only 1 feature
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.3, random_state=42)

model1 = LinearRegression()
model1.fit(X_train, y_train)

y_pred1 = model1.predict(X_test)

print("MSE (Area only):", mean_squared_error(y_test, y_pred1))


# In[4]:


## Use room and area both
X2 = df[["Area", "Rooms"]]   # added feature

X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.3, random_state=42)

model2 = LinearRegression()
model2.fit(X_train, y_train)

y_pred2 = model2.predict(X_test)

print("MSE (Area + Rooms):", mean_squared_error(y_test, y_pred2))


# In[ ]:


## Hour 7
## Maximum Sum Subbarray
nums = [-2,1,-3,4,-1,2,1,-5,4]
Output = 6   
# (subarray [4,-1,2,1])

def maxSubArray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


# In[5]:


nums = [-2,1,-3,4,-1,2,1,-5,4]
Output = 6   

def max_sub_array_Kadane(nums):
    cur_sum = nums[0]
    max_sum = nums[0]
    for i in range(1,len(nums)):
        cur_sum = max(nums[i],cur_sum+nums[i])
        max_sum = max(max_sum,cur_sum)
    return max_sum
print(max_sub_array_Kadane(nums))


# In[8]:


## Kadane algo with storing the subarray of max sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]

    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > curr_sum + nums[i]:
            curr_sum = nums[i]
            temp_start = i
        else:
            curr_sum += nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

    return max_sum, nums[start:end+1]
print(maxSubArray(nums))


# In[ ]:


## Problem 2
## Longest Subarray with Sum k
# Pattern - Prefix Sum + Hashmap

## Example
nums = [1,2,3,1,1,1,1], k = 3
Output = 3

def longestSubarraySumK(nums, k):
    prefix_sum = 0
    hashmap = {0: -1}
    max_len = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum - k in hashmap:
            max_len = max(max_len, i - hashmap[prefix_sum - k])

        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i

    return max_len


    ## Problem 3
# PROBLEM 3 — Valid Parentheses
# 📌 Pattern: Stack
# 📌 Example
# "()[]{}" → True  
# "(]" → False


