#!/usr/bin/env python
# coding: utf-8

# Block 1 of Hour 1
# Decision Boundary
# 
# a line or surface which separates two classes
# at decision boundary P=0.5
# sigmoid(0) = 0.5
# wx+b = 0
# 
# wx+b>0 → Class 1
# wx+b<0 → Class 0
# output is non linear - sigmoid
# boudnary is still linear
# 
# Block Summary
# Decision boundary = separation line
# Occurs when probability = 0.5
# Defined by:
# wx+b=0
# Linear in nature

# Block 2 of Hour 1
# when we change threshold
# If threshold = 0.7
# P(Y=1)>=0.7
# 0.7 = 1/(1+e**-z)
# z =log(0.7/(1-.07))
# wx+b = constant
# wx+b = log(threshold/(1-threshold))
# 

# Hour 2
# Block 1
# Changing threshold affects:
# 
# Precision (how correct positives are)
# Recall (how many positives you catch)
# 
# 0.5  works - for balanced dataset, equal cost of error (cost means business case like
# medical,fraud etc)
# 
# Block 2
# How to choose right threshold
# 
# 1. Start with model output
#     y_prob = model.predict_proba(X)[:,1]
# 
# 2. try multiple threshold
#     threhold =[0.3,0.4,0.5,0.6,0.7]
#     for i in threshold:
#         y_pred = (y_prob>=i).astype(int)
# 
# 3. Evaluate using Metrics
# -- Precision
# -- Recall
# -- F1-Score
# 
# Best threshold = where your problem’s goal is best satisfied

# Hour 3
# Block 1
# Probability = model’s confidence in class membership
# 
# Output = P(Y=1∣X) :-
# Represents confidence
# Enables threshold tuning
# Critical for decision making
# 
# Block 2
# when probability can be misleading
# probability = confidence
# but confidence is not always correctness
# model may give 0.95 but actual class 0
# model is overconfident
# 
# Reasons : - model is  not perfect - has not captured pattern
# - less data - bias
# - Overfitting - model tried to memorise the data points instead of generalising
# 
# so here comes the calibration
# if model say 80% correct - 80 % of such prediction should be correct
# 
# How to do calibration 
# 1. Train a logistic Reg model on models output
# take X_new = prob(1)
# y_new - actual vaule
# y_prob = model.predict_proba(X_val)[:, 1]
# 
# Example:
# 
# Input	True y	Model Output
# x1	      1	        0.9
# x2	      0	        0.8 ❌
# x3	      1	        0.6
# x4	      0	        0.3
# 
# here model is overconfident giving 0.8 prob for 0 true value
# so here comes the calibration
# X_new  = model output (it is treated as input) and y_new = True y (it is output)
# 
# X_new = y_prob   # model predictions
# y_new = y_val    # true labels
# 
# So dataset becomes:
# 
# Input (X_new)	Output (y_new)
# 0.9	                1
# 0.8	                0
# 0.6	                1
# 0.3	                0
# 
# so we train logistic regression on this
# calibration_model.fit(X_new,y_new)
# suppose it give output
# 
# Original	Calibrated
# 0.9	          0.85
# 0.8	          0.65
# 0.6	          0.7
# 0.3	          0.25
# 👉 It corrects bias
# 
# Original model → gives probability
# Calibration model → adjusts probability
# 
# df → X, y
#       ↓
# split → X_train, X_test
#       ↓
# (train split further OR Cross Validation)
#       ↓
# model.fit(X_train)
#       ↓
# calibration uses validation inside training
#       ↓
# FINAL → evaluate on X_test
# 
# Validation data comes from splitting the training data (manually or via cross-validation), 
# not from the test set
# 
# calibrated_model = CalibratedClassifierCV(model, method='sigmoid')
# calibrated_model.fit(X_train, y_train)
# 
# what it doesn internally is -
# Splits X_train into folds
# Gets predictions
# Uses those as:
# X_new = predicted probs
# y_new = actual labels of validation folds
# 
# Train = learn
# Validation = tune
# Test = final check

# Hour 4 Block 1
# Feature Impact — What Coefficients Actually Mean
# Logistic Regression models:
# 
# log(P/(1−P)) = w1x1+w2x2+w3x3+...+b
# Each feature has a coefficient (w)
# 
# +ve - increases probability of class 1
# -ve - decreases probability if class 1
# 
# Coefficients affect log-odds, not probability directly
# we use e**w -----> how many times the odds changes
# 
# Logistic Regression is:
# Linear in log-odds
# So coefficients affect log-odds linearly
# If feature increases by 1 unit → odds multiply by e
# Coefficient = strength and direction of feature’s impact on odds
# 
# Block 2
# Multiple Feature - Combined Effect
# 
# log(P/(1−P)) = w1x1+w2x2+w3x3+...+b
# log(odds) = w1x1+w2x2
# odds = (e**w1x1)*(e**w2x2)
# 
# Effects multiply in odds space
# Add in log space
# 
# Logistic Regression assumes:
# 
# ❗ Features contribute independently (no interaction terms by default)
# interaction needed:
# You must manually add it

# In[5]:


## Hour 5
## Mini Experiment
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample data
X = np.array([[22], [25], [30], [35], [40], [45]])
y = np.array([0, 0, 0, 1, 1, 1])

# Train model
model = LogisticRegression()
model.fit(X, y)

# Get Probability
y_prob = model.predict_proba(X)[:, 1]
print(y_prob)
y_pred = model.predict(X)
print(y_pred)

# Threshold = 0.5
y_pred_05 = (y_prob >= 0.5).astype(int)
print(y_pred_05)

# Threshold = 0.3
y_pred_03 = (y_prob >= 0.3).astype(int)
print(y_pred_03)

# Threshold = 0.7
y_pred_07 = (y_prob >= 0.7).astype(int)
print(y_pred_07)


# In[8]:


## Hour 6
## Underfitting and Overfitting in Logistic Regression
# Underfitting - common if features weak
# Overfitting - too many features, no regularisation

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# simple dataset
X = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([0,0,0,1,1,1])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state =42)

model = LogisticRegression()
model.fit(X_train,y_train)

train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))

print("Train_acc",train_acc,"\n" "test accuracy",test_acc)

## Create Underfitting
# Making model too simple
model1 = LogisticRegression(C=0.01) 
# C = inverse of regularisation strenth --smaller C incresease regularisation
# by shrinking coefficient and reducing model complexity - chances of underfitting
model1.fit(X_train,y_train)

train_acc1 = accuracy_score(y_train, model1.predict(X_train))
test_acc1 = accuracy_score(y_test, model1.predict(X_test))
print("Train_acc1",train_acc1,"\n" "test acc1",test_acc1)

# Create overfitting
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=5)
X_poly = poly.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_poly,y,test_size=0.3)

model2 = LogisticRegression(C=1000)
model2.fit(X_train,y_train)

train_acc2 = accuracy_score(y_train, model2.predict(X_train))
test_acc2 = accuracy_score(y_test, model2.predict(X_test))
print("Train_acc1",train_acc2,"\n" "testacc1",test_acc2)


# In[11]:


# simple dataset
## Y changed to y = [0,0,0,0,1,1]

X = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([0,0,0,0,1,1])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state =42)

model = LogisticRegression()
model.fit(X_train,y_train)

train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))

print("Train_acc",train_acc,"\n" "test accuracy",test_acc)

## Y changed to y = y = [0,1,0,1,0,1]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state =42)

model = LogisticRegression()
model.fit(X_train,y_train)

train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))

print("Train_acc",train_acc,"\n" "test accuracy",test_acc)

## Change regularisation
C = [0.001, 0.01, 1, 100]
X = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([0,0,0,1,1,1])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state =42)
acc = []
for i in C:
    model = LogisticRegression(C=i)
    model.fit(X_train,y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    acc.extend([train_acc,test_acc])
print(acc)


# In[12]:


import numpy as np
## Change regularisation
C = [0.001, 0.01, 1, 100]
X = np.arange(1, 101).reshape(-1,1)
y = np.array([0]*50 + [1]*50)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state =42)
acc = []
for i in C:
    model = LogisticRegression(C=i)
    model.fit(X_train,y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    acc.extend([train_acc,test_acc])
print(acc)


# In[71]:


## Hour 8
## Retrain 
import numpy as np
from sklearn.model_selection import train_test_split

# create noisy data
np.random.seed(42)
X = np.arange(1, 101).reshape(-1,1)
y = np.array([0]*50 + [1]*50)

# add noise
noise_idx = np.random.choice(100, 10, replace=False)
y[noise_idx] = 1 - y[noise_idx]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression()
model.fit(X_train, y_train)

train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))

print("Baseline:", train_acc, test_acc)

## Retrain with different C
for c in [0.01, 0.1, 1, 10, 100]:
    model = LogisticRegression(C=c)
    model.fit(X_train, y_train)
    
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    
    print(f"C={c} → Train: {train_acc}, Test: {test_acc}")


## Adding Polynnomial feature
poly = PolynomialFeatures(degree=5)
X_poly = poly.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2)
print("With Polynomial Feature degree = 5")
for c in [0.01, 0.1, 1, 10, 100]:
    model = LogisticRegression(C=c)
    model.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    print(f"C={c} → Train: {train_acc}, Test: {test_acc}")

## Try Threshold tuning 
y_prob = model.predict_proba(X_test)[:,1]

threshold = 0.3
y_pred = (y_prob >= threshold).astype(int)

print("Custom threshold accuracy:", accuracy_score(y_test, y_pred))


# In[72]:


## Adding more noise
import numpy as np
from sklearn.model_selection import train_test_split

# create noisy data
np.random.seed(42)
X = np.arange(1, 101).reshape(-1,1)
y = np.random.randint(0,2,100)

# add noise
noise_idx = np.random.choice(100, 10, replace=False)
y[noise_idx] = 1 - y[noise_idx]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score

model = LogisticRegression()
model.fit(X_train, y_train)

train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))

print("Baseline:", train_acc, test_acc)

## Retrain with different C
for c in [0.01, 0.1, 1, 10, 100]:
    model = LogisticRegression(C=c)
    model.fit(X_train, y_train)
    
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    
    print(f"C={c} → Train: {train_acc}, Test: {test_acc}")


## Adding Polynnomial feature
poly = PolynomialFeatures(degree=5)
X_poly = poly.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2)
print("With Polynomial Feature degree = 5")
for c in [0.01, 0.1, 1, 10, 100]:
    model = LogisticRegression(C=c)
    model.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    print(f"C={c} → Train: {train_acc}, Test: {test_acc}")

## Try Threshold tuning 
y_prob = model.predict_proba(X_test)[:,1]

threshold = [0.2,0.5,0.8]
for i in threshold:
    y_pred = (y_prob >= i).astype(int)
    print(f"Threshold = {i},accuracy_score:- {accuracy_score(y_test, y_pred)}")
    print(f"Threshold = {i},precision_score:- {precision_score(y_test, y_pred)},recall_score:- {recall_score(y_test, y_pred)}")


# In[ ]:


## DSA
## If list contain duplicate
# True or False
nums = [1,2,3,1]
def contain_duplicate(nums):
    seen = set()
    for num in nums:
     if num in seen:
        return True
     seen.add(num)
    return False

# print(contain_duplicate(nums))

## Freq
def contain_duplicate(nums):
    freq ={}
    for num in nums:
      freq[num] = freq.get(num,0)+1
      if freq[num]>1:
         return True
    return False
# print(contain_duplicate(nums))

# nums = []
# nums = [1]
# nums = [1,1,1,1]
# nums = [1,2,3,4]

print(contain_duplicate(nums))

# Set is enough as set dont allow duplicates so adding to set will be enough
# because in key we stored num and in value we store the count 
# and we use count to find our result
# Time complexity if O(n) for both



# In[85]:


## Problem 2
s = "anagram"
t = "nagaram"

# use dict
def anagram(s,t):
    if len(s) != len(t):
        return False
    
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in t:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False
    
    return True
print(anagram(s,t))

## Other way
from collections import Counter

def is_anagram(s,t):
    return Counter(s) == Counter(t)


# In[89]:


# ## Stress Test
# s = "a"
# t = "a"

# s = "a"
# t = "b"

# s = "rat"
# t = "car"

s = "aacc"
t = "ccac"

print(anagram(s,t))


# In[99]:


## contains duplicate
nums = [1,2,5,2]
def if_contain_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(if_contain_duplicate(nums))


# In[108]:


# First Unique Character
s = "leetcode"
# Return index
def first_unique(s):
    dct = {}
    for char in s:
        dct[char] = dct.get(char,0)+1
    for i in range(len(s)):
        if dct[s[i]]==1:
            return i   
    return -1   
print(first_unique(s))

for i, ch in enumerate(s):
    print(i,ch)

