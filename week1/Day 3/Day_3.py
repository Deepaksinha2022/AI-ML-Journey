#!/usr/bin/env python
# coding: utf-8

# ## Day 3 Hour 1

# In[ ]:


## List operations

# lst = [23,45,85,68,32,2,54,87,69]
# lst.append(102)
# lst.insert(4,542)
# lst.pop()
# lst.remove(2)
# lst


# In[ ]:


## Block 2

# lst = [10,20,30,40]
# lst.insert(2,25)
# lst.pop(3)
# lst.pop()
# lst.append(50)
# lst

## Task 2 - Remove even numbers
# lst = [1,2,3,4,5]
# for i in lst:
#     if i%2 ==0:
#         lst.remove(i)
# lst


# In[ ]:


## Block 3

## Task 1

# lst = [1,2,3,2,4,2,5]
# # for i in lst:
# #     if i == 2:
# #         lst.remove(i)
# # lst

# lst = [x for x in lst if x!=2]
# lst

## Task 2
## Sort list manually
# lst = [5,1,3,2,4]
# def sort_lst(lst):
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i]>lst[j]:
#                 lst[i],lst[j] = lst[j],lst[i]
#     return lst

# print(sort_lst(lst))

## Task 3

# reverse list without slicing

# lst = [1,2,3,4,5]
# def reverse_lst(lst):
#     i = 0
#     j = len(lst) -1
#     while i<j:
#         lst[i],lst[j] = lst[j],lst[i]
#         i+=1
#         j-=1
#     return lst
# print(reverse_lst(lst))


# In[ ]:


## Block 4

## List Comprehension

# lst = [1,5,8,7,6,3]

# lst1 = [x**2 for x in lst ]
# lst1

# ## Get even number
# lst2 = [x for x in lst if x%2==0]
# lst2

# ## Convert

# #["a","b","c"] → ["A","B","C"]

# lst3 = ["a","b","c"]
# lst4 = [x.upper() for x in lst3]
# lst4


# In[ ]:


## HOUR 2

## BLOCK 1
# tp = (1,7,45,87,36)
# tp[4] = 4
# tp


# In[ ]:


## Block 2
## Sets

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a.union(b))
# print(a.intersection(b))
# print(a.symmetric_difference(b))
# a.add(63)
# a.pop()
# a.remove(4)
# a

## Block 3
## Check if two list have any common element

# l = [2,5,6,8,7,96]
# h = [5,8,63,25,74,14]

# print(set(l).intersection(set(h)))

## Find Unique Characters

# s = "programming"
# print(set(s))


# In[ ]:


## Hour 3

## Block 1

# dct = {"a":1, "b":2, "c":3}
# print(dct.keys())
# print(dct.values())
# print(dct.items())

## task 2
# for i,j in dct.items():
#     print(i,j)


## Block 3

# s = "apple"
# dct = {}
# for i in s:
#     if i in dct:
#         dct[i] +=1
#     else:
#         dct[i] = 1
# dct


## Task 3
# lst = ["a","b","a","c","b","a"]
# dct = {}
# for i in lst:
#     if i in dct:
#         dct[i] += 1
#     else:
#         dct[i] = 1
# dct


# In[7]:


## Hour 4
## Block 1

import numpy as np
# arr = np.array([10,15,20,25,30])

# print(arr[arr>20])
# print(arr[arr%10==0])
# print(arr[(arr>15) & (arr<30)])
# # print(arr>15)
# print(arr)

## Block 2

arr = np.array([10,20,30,40,50])
print(arr[0])


# In[11]:


# Block 3

## task 2
# arr = np.array([[1,2,3],
#                 [4,5,6]])
# ar = [10,20,30]

# print(arr+ar)

## Task 3 ---- Multiply

a = np.array([[1,2,3],
 [4,5,6]])
b= np.array([1,2,3])

print(a*b)


# In[ ]:


## Numpy does operation in one go --- faster


# In[17]:


## Hour 5

## block 1

import pandas as pd

df = pd.read_csv("Telco_Customer_Churn.csv")
print(df.head())
df.groupby("Churn").mean(numeric_only= "True")


# In[ ]:


#df.groupby("Churn").agg({"tenure":"mean","MonthlyCharges":"max"})
# df.groupby("gender").count()


# In[ ]:


## Block -------> 3
# df.groupby("Contract")["tenure"].mean()
# df.groupby("Churn")["MonthlyCharges"].max()
df.groupby("gender").count()


# In[32]:


## Hour -----------> 6

## Block 1
df.groupby("Contract").count()

## Block 2

df.groupby("Contract")["tenure"].mean()

## Block 3

df.groupby("gender")["MonthlyCharges"].mean()

df.groupby("Contract")["Churn"].count()


# In[33]:


df[df["Churn"]=="Yes"].groupby("Contract").count()


# In[ ]:


## Hour 7

# Remove duplicates from sorted array

lst = [1,1,2,2,3]

def remove_dup(lst):
    i = 0
    for j in range(1,len(lst)):
        if lst[i]!= lst[j]:
            i+=1
            lst[i] = lst[j]
    return lst
print(remove_dup(lst))


# In[ ]:


## Hour 8

# print(df["tenure"].describe())
# df["MonthlyCharges"].describe()


# In[ ]:


# df["tenure"].hist()
print(df.head())
df["MonthlyCharges"].hist()


# In[45]:


df.boxplot(column="MonthlyCharges")


# In[46]:


df.boxplot(column="tenure")


# In[51]:


print(df.dtypes)


# In[54]:


df["tenure"].hist()


# In[53]:


df["MonthlyCharges"].hist()


# . Monthly Charges Distribution
# 
# MonthlyCharges appears right-skewed, with a high concentration of customers in the lower range (~18–27), indicating many users are on lower-priced plans.
# 
# 🔹 2. Tenure Distribution
# 
# The tenure variable does not show significant outliers based on the boxplot, suggesting a relatively stable spread of customer duration.
# 
# 🔹 3. Spread Comparison
# 
# MonthlyCharges exhibits a wider spread compared to tenure, indicating greater variability in pricing than in customer duration.
