#!/usr/bin/env python
# coding: utf-8

# DAY 1

# In[ ]:


## Swap two numbers
# a= int(input("Enter first number (a) : - "))
# b= int(input("Enter second number (b) : - "))
# a,b = b,a
# print(" After swapping a = ", a)
# print(" After swapping b = ", b)


# In[ ]:


## Sum of list

# lst = [3,7,2,9,2]
# sum = 0
# for i in lst:
#     sum += i


# In[ ]:


## Find Maximum number in a list

# lst = [23,12,17,28,96,36,75,105]
# max_lst = lst[0]
# for i in lst:
#     if i>max_lst:
#         max_lst = i
# print(max_lst)


# In[ ]:


## Reverse a string

# str = input("Enter any word : - ")
# print("Reversed String is : -", str[::-1])

## Factorial of number using function


# In[ ]:


# def fact(num):
#     if num == 0:
#         return 1
#     return num*fact(num-1)

# print(fact(3))


# ============= HOUR 4: NUMPY==================

# In[6]:


### --------------- 1D Array-----------------
import numpy as np
arr1 = np.array([25,87,89,36,24])
print(arr1)
print(type(arr1))


# In[9]:


## 2D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(type(arr2))
arr2.shape


# In[ ]:


###--------- Zeros array-----------
# arr3 = np.zeros((2,3))
# print(arr3)

# arr4 = np.ones((3,2))
# arr4

# arr5 = np.full((2,2),7)
# arr5

# arr5 = np.ones((3,2))
# arr5


# In[ ]:


#### arange

# a1 = np.arange(0,10,2)
# # a1

# print(a1*2)

# a2 = np.arange(6).reshape(2,3)
# a2


# In[ ]:


# a1= np.arange(1,7).reshape(2,3)
# a2 = np.arange(7,13).reshape(2,3)

#print(a1,a2,a1+a2,a1*a2)


# In[35]:


#### INDEXING

a1 = np.arange(1,10).reshape(3,3,1)
print(a1)
print(a1[0][1])


# # ======= PANDAS ========

# In[40]:


import pandas as pd

df = pd.read_csv("mobile_price_dataset.csv")
print(df.head())
# print(df.info())
df.describe()


# In[42]:


df.shape
df.columns


# In[ ]:


## Problem: Two Sum
## Given:
# list of numbers
# a target
# Find:
# indices of two numbers whose sum = target

def two_sums(nums,target):
    dct= {}
    for i, num in enumerate(nums):
        if target-num in dct:
            return dct[target-num],i
        dct[num] = i

print(two_sums([2,7,11,15],18))



# In[57]:


## Telco Churn Analysis

import pandas as pd
df = pd.read_csv("Telco_Customer_Churn.csv")
df.head()


# In[59]:


df.columns
# customerID is identifier
# monthly charges, tenure, total charges are numerical
# Churn is the target 
# Partner, dependent, phone service are categorical
# 

