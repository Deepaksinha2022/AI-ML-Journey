#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Key Difference (Very Important)
# Feature	          Regression	                  Classification
# Output	       Continuous values	              Discrete labels
# Example	       Price prediction	                  Yes/No prediction
# Model Goal	   Fit a line/curve	                  Separate classes


# Decsion Boundary
# Model creates a line to separate classes 0 or 1
# This line is called decision boundary
# Model first make probability then classify yes or no or 0 or 1
# after probability model applies threshold to classify the points
# 

# Hour 2
# Block 1
# why linear regression fails
# 1. it can predict values for - infinity to + infinity which are invalid probability
# - poor fit for binary data
# 2. predictions dont align with class boundart - it tries to fit through the points
# 3. Sensitive to Outliers
# Linear regression is heavily affected by extreme values.
# Example:
# One wrong data point far away → line shifts completely
# 4. No Probability Interpretation
# Linear regression gives:
# 👉 Just a number
# 
# Block 2
# Logistic Regression
# 
# What the Model Actually Does
# Step-by-step:
# Compute linear output → z=wx+b
# Apply sigmoid → get probability
# Use threshold (0.5) → classify - chosen based on case and precision and recall
# for disease detection use less threshold for spam use more threshold
# 
# Why This Works Perfectly
# ✔ Output always between 0 and 1 → valid probability
# ✔ Smooth transition → handles uncertainty
# ✔ Naturally forms a decision boundary

# What is the Sigmoid Function?
# 
# This is the function that converts any number into a probability:
# 
# σ(z)=1/(1+e**−z)
# 1
# 👉 Input: any value (−∞ to +∞)
# 👉 Output: always between 0 and 1
# 
# Key Intuition
# Linear model → gives raw score (z)
# Sigmoid → converts score into probability
# 👉 This is the exact fix to linear regression’s problem
# s-shaped curve
# 

# Sigmoid Output Range
# 
# Recall:
# 
# 0<σ(z)<1
# 
# 👉 No matter what value of z is:
# 
# Output is never < 0
# Output is never > 1
# 🔹 Intuition
# Very large negative z → output ≈ 0
# Very large positive z → output ≈ 1
# 
# 👉 This makes it perfect for probability
# 
# 🔹 2. Why 0–1 Range is Critical
# 
# In classification, we want:
# 
# 👉 “How confident is the model?”
# 
# Not just:
# 
# Yes / No ❌
# But:
# How likely? ✔
# 
# Probability Interpretation:-
# 👉 Sigmoid output is interpreted as:
# P(Y=1∣X)
# Meaning:
# 👉 Probability that output belongs to class 1 given input X

# Odds
# What are Odds? (Basic Idea)
# 👉 Odds compare:
# “Chance of happening” vs “chance of not happening”
# Odds= P/(1−P)
# if P = 0.75 - chances if happening is 3 timre than not
# 
# Why Not Use Probability Directly?
# Because:
# Probability is bounded (0 to 1)
# Hard to model linearly
# 👉 Odds:
# Range = 0 to ∞
# Easier to transform mathematically
# 
# Key Insight (Very Important)
# 👉 Logistic Regression doesn’t directly model probability
# 👉 It models:
# Odds → then log-odds → then probability
# 
# 
# Final Intuition (Very Important)
# 👉 We choose:
# Linear model → predicts log-odds
# Then mathematically convert → probability
# 
# One-Line Answer
# 👉 z=log(P/(1−P)) comes because:
# We define the linear model to predict log-odds, since it matches the (-∞, +∞) range.
# 
# z=log(P/(1−P)) comes because:
# We define the linear model to predict log-odds, since it matches the (-∞, +∞) range.

# Hour 4
# What is Log-Odds (Logit)?
# Log-odds is simply:
# log(P/(1-P))
# It is the log of odds
# Log-odds → range (-∞, +∞)

# In[1]:


## Model Implementation
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
X = [[25],
     [30],
     [35],
     [40]]   # Age
y = [0, 0, 1, 1]               # Bought product or not
model.fit(X, y)

# Here error is minimised using log loss (cross - entropy) , not MSE
print(model.coef_)      # weights
print(model.intercept_) # bias


# In[ ]:


## Hour 6 
# Block 1
# Predict 
y_pred = model.predict(X)
y_prob = model.predict_proba(X)

print(y_pred)
print(y_prob)

## frquency = 0.5 not always better
# for disease detection lower threshold - more positive good for us than to miss
# - high recall low precision
# for spam higher threshold is good as it may not miss important emails as spam
# - low recall and high precision

# How to change threshold
y_prob = model.predict_proba(X)[:, 1]
threshold = 0.3
y_pred = (y_prob >= threshold).astype(int)

## threshold is a business decision not a model decision


# In[12]:


## Train a model using logistic regression

from sklearn.linear_model import LogisticRegression
import numpy as np

# Feature: Age
X = np.array([[22], [25], [30], [35], [40], [45]])

# Target: Bought product (0 = No, 1 = Yes)
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X,y)

# Check Probability
probs = model.predict_proba(X)
print(probs)

## Extract only class 1 Probability
p_class1 = probs[:,1]
print(p_class1)

# Apply threshold
threshold = 0.5
predictions = (p_class1 >= threshold).astype(int)
print(predictions)

threshold = 0.2
predictions = (p_class1 >= threshold).astype(int)
print(predictions)


# Logistic Regression is:
# 
# Linear in:
# log(P/(1-P))
# Non-linear in probability due to sigmoid
# 
# We use log loss because:
# 
# It works with probabilities
# Penalizes wrong confident predictions heavily
# MSE doesn’t suit classification

# In[ ]:


# DSA
## Two Sum
nums = [2, 11, 15,7]
target = 9

## Time Complexity O(n**2)
def TwoSumArray(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
          
## Using hashmaps
def TwoSumArr(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement] , i]
        hashmap[nums[i]] = i
print(TwoSumArr(nums,target))


# In[ ]:


## Problem 2 :Best Time to Buy and Sell Stock
prices = [7, 1, 5, 3, 6, 4]

## Time Complexity O(n**2)
def bruteforce_stockbuy(prices):
    max_profit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i+1,n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit,profit)
    return max_profit
print(bruteforce_stockbuy(prices))

## O(n)
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price,price)
        profit = price -min_price
        max_profit = max(max_profit,profit)
    return max_profit
print(max_profit(prices))


# In[ ]:


## Two sum pattern - return index of sum of target
nums = [2, 3, 4, 7, 11]
target = 9

def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]   # ✅ FIX
        
        hashmap[nums[i]] = i
print(two_sum(nums,target))


# In[ ]:


# Q3 (Very Important — HashSet Pattern)
#  Contains Duplicate
nums = [1, 2, 3, 4]
# Return:
# True if duplicate exists
# False otherwise

def contain_duplicate(nums):
    seen = set()
    for num in (nums):
        if num in seen:
            return True
        seen.add(num)
    else:
        return False
print(contain_duplicate(nums))


# In[3]:


# Maximum Difference (Stock Pattern Reuse)
arr = [7, 1, 5, 3, 6, 4]
def max_diff(arr):
    current_min = float('inf')
    max_diff = 0
    for num in arr:
        if num < current_min:
            current_min = num
        else:
            max_diff = max(max_diff, num - current_min)
    return max_diff

print(max_diff(arr))

