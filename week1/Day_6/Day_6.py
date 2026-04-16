#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Hour 1
## Block 1
## Task 1

# data = {
#     "A": [10,20,30],
#     "B": [5,15,25],
#     "C": [2,4,6]
# }

# ## Average of each keu
# ## Overall max value
# def analyze(data):
#     dc = {}
#     overall_max = float('-inf')
    
#     for key in data:
#         total = 0
        
#         for val in data[key]:
#             total += val
            
#             if val > overall_max:
#                 overall_max = val
        
#         avg = total / len(data[key])
#         dc[key] = avg
    
#     return dc, overall_max
# print(analyze(data))

## Task 2

lst = ["apple","banana","apple","cherry","banana","apple"]
## Output
{"apple":3, "banana":2, "cherry":1}
## Donot use counter

# def count_word(lst):
#     dc={}
#     for i in lst:
#         dc[i]=dc.get(i,0)+1
#     return dc
# print(count_word(lst))

## Shorter solution

# from collections import Counter
# Counter(lst)

## Task 3

# lst = [[1,2,3],[4,5],[6,7,8,9]]
# def sum_s(lst):
#     l=[]
#     for i in lst:
#         s=0
#         for j in i:
#             s+=j
#         l.append(s)
#     return l
# print(sum_s(lst))


# In[20]:


## Block 2
## Task 1
# lst = [10, 20, 4, 45, 99]
# def sec(lst):
#     max=float('-inf')
#     sec_max=float('-inf')
#     for i in lst:
#         if i>max:
#             sec_max=max
#             max=i
#         elif i>sec_max and i!=max:
#             sec_max=i
#     return sec_max
# print(sec(lst))


## Task 2
# lst = [1,2,3,4,5,6,7]
# k = 3
# # output - [5,6,7,1,2,3,4]

# def left_rot(lst,k):
#     res=[]
#     n=len(lst)
#     for i in range(n):
#         res.append(lst[(i-k)%n])
#     return res
# print(left_rot(lst,k))

# Task -3 Spiral Traversal

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
## Output - [1,2,3,6,9,8,7,4,5]

def spiral(matrix):
    res = []
    
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1
    
    while top <= bottom and left <= right:
        
        # left → right
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1
        
        # top → bottom
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # right → left
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # bottom → top
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
    
    return res

print(spiral(matrix))


# In[24]:


## Hour 3
## Block 1
## task 1
import numpy as np

A = np.array([
 [1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]
])
## First Row
print(A[0,:])
## Last Column
print(A[:,3])
# Submatrix - [6,7],[10,11]
print(A[1,1:3],A[2,1:3])


# In[28]:


## Block 2
## Task 2 - Broadcasting
A = np.array([
 [1,2,3],
 [4,5,6]
])
print(A+10)

## Task-3 - Sorting
arr = np.array([5,2,9,1,7])
print(np.sort(arr))

## 2D Case
B = np.array([
 [3,1,2],
 [6,5,4]
])
## Sort - Row Wise
print(np.sort(B, axis=1))
## Sort - Column Wise
print(np.sort(B,axis=0))


# In[13]:


## Hour 4
## Task 1
import pandas as pd
df= pd.read_csv("Telco_Customer_Churn.csv")
# print(df.head())
# df["Contract"].value_counts()
# df["Contract"].value_counts(normalize=True)

# Task 2
# Drop COlumn
df.drop("customerID",axis=1)
# df.drop(0,axis=0,inplace=True) ## Inplace modifies the original data 
df


# In[ ]:


## Tsk 1
## Rename
df.rename(columns={"MonthlyCharges":"Monthly_Charges"},inplace=True)
df.head()

## Task 2
## Convert Churn (Yes/No to 1/0)
df["Churn"]=df["Churn"].str.strip()
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
df.head()


# In[ ]:


## Hour 5
## Block 1
df.describe()
df.describe(include="object")


# In[21]:


## Block 2
## Correlation Matrix
df.corr(numeric_only=True)


# In[24]:


## Hour 6
## Block 1
print(df["tenure"].hist())
print(df["Monthly_Charges"].hist())


# In[26]:


## Block 2
## Countplot
import seaborn as sns
sns.countplot(x="Churn", data=df)
sns.countplot(x="Contract", data=df)


# In[28]:


## Block 3
sns.boxplot(x="Churn", y="Monthly_Charges", data=df)


# In[29]:


sns.boxplot(x="Churn", y="tenure", data=df)


# In[33]:


## HOur 7
nums1 = [1,2,2,1]
nums2 = [2,2]

Output = [2]
def intersec(nums1,nums2):
    return list(set(nums1).intersection(set(nums2)))

print(intersec(nums1,nums2))


# In[ ]:


## hour 8
# 1. Tenure vs churn - short tenure tend to churn more
## Monthly charges v churn - churn customer have more median monthly charges
# 3. contract type - distribution - month to month contract have higher count
## 4. churn customer have less count than non churn

## Block 3
## what should company do-
## Company should provide attarctive offer to new customers 
# as short term tend to churn more
## Where to focus-
## 1. company should target short term contract customers, high monthly charges customer
## 

