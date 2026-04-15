#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Hour 1
## Block 1
## Task one
# TASK 1 — Palindrome (Advanced Twist)
# 👉 Given number:
# check palindrome
# without converting to string
# ⚠️ Use math logic only

# def is_pallindrome(n):
#     rev = 0
#     cop = n
#     while cop>0:
#         mod = cop%10
#         rev = rev*10 + mod
#         cop = cop//10
#     if rev == n:
#         return True
#     else:
#         return False
# print(is_pallindrome(125))


# Task 2
# TASK 2 — Armstrong Number (Generalized)
# 👉 Input:
# any number
# 👉 Check:
# Armstrong for any number of digits
# ⚠️ Not just 3-digit

# def armstrong(num):
#     prod = 0
#     cop = num
#     while cop>0:
#         prod+=(cop%10)**3
#         cop=cop//10
#     return prod==num
# print(armstrong(153))

## Task 3
## Givem
# s = "  hello   world   python  "
# ## Count number of words

# def count_words(s):
#     return len(s.split())
# print(count_words(s))

## Task 4
# TASK 4 — Merge Sorted Lists (IMPORTANT)
# 👉 Given:
# a = [1,3,5,7]
# b = [2,4,6,8]
# 👉 Output:
# [1,2,3,4,5,6,7,8]

# a =[]
# b =[1,2,3]
# def merge_lists(a,b):
#     ml = []
#     i,j = 0,0
#     while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             ml.append(a[i])
#             i+=1
#         else:
#             ml.append(b[j])
#             j+=1
#     while i<len(a):
#         ml.append(a[i])
#         i+=1
#     while j<len(b):
#         ml.append(b[j])
#         j+=1
#     return ml
# print(merge_lists(a,b))

# TASK 5 — Flatten Nested List (INTERMEDIATE+)
# Given:
# inp=[1,[2,3],[4,[5,6]],7]
# #Output:
# out=[1,2,3,4,5,6,7]

# inp = [1,[2,3],[4,[5,[6,7]]]]
# def flatten_list(inp):
#     res = []
#     for item in inp:
#         if isinstance(item, list):
#             res.extend(flatten_list(item))
#         else:
#             res.append(item)
    
#     return res
# print(flatten_list(inp))


# In[ ]:


## Block 2

## Task 1
# s= "  hello   world  python  "

# ## Count words without using split

# def count_words(s):
#     count = 0
#     for i in range(len(s)):
#         if s[i] != " " and (i == 0 or s[i-1] == " "):
#             count += 1
#     return count
# print(count_words(s))


# In[ ]:


## Hour 2 (DSA Basics)
## Block 1
## Task 1
## Right Rotation

lst=[1,2,3,4,5]
k=2
## Without slicing

# def right_rot(lst, k):
#     n = len(lst)
#     res = []
#     for i in range(n):
#         res.append(lst[(i - k) % n])
#     return res
# print(right_rot(lst,k))

## Block 2
## Left rotate

# def left_rot(lst, k):
#     n = len(lst)
#     res = []
#     for i in range(n):
#         res.append(lst[(k + i) % n])
#     return res
# print(left_rot(lst,k))


# In[61]:


## Block 3
## Task -4 
## Rotation in place
## No extra list

lst=[1,2,3,4,5]
k=2

def reverse(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1


def right_rotate(lst, k):
    n = len(lst)
    
    if n == 0:
        return lst
    
    k = k % n
    
    reverse(lst, 0, n-1)
    reverse(lst, 0, k-1)
    reverse(lst, k, n-1)
    
    return lst
print(right_rotate(lst,k))


# In[ ]:


## Hour 3
## Task -1
# def is_even(n):
#     return True if n%2==0 else False
# print(is_even(4))

## Task 2
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# print(factorial(6))

## Task - 3
# lst = [2,5,8]
# def sum_list(lst):
#     sum =0
#     for i in lst:
#         sum+=i
#     return sum
# print(sum_list(lst))


# In[ ]:


## Block 2

## Task 4
# lst=[3,6,7,8,96,33,37]
# def filter_even(lst):
#     lst1 = list(filter(lambda x: x%2==0,lst ))
#     return lst1
# print(filter_even(lst))

## Task 5
# lst = [1,2,3,4]
# def apply_factorial(lst):
#     for i in lst:
#         fact = 1
#         lst1=[]
#         for j in range(1,i+1):
#             fact*=j
#         lst1.append(fact)
#     return lst1
# print(apply_factorial(lst))


# In[ ]:


## Block 3

## Task 7
# lst = [1,2,3,4,5,]
# def process_numbers(lst, condition, operation):
#     res=[]
#     for x in lst:
#         if condition(x):
#             res.append(operation(x))
#     return res
# print(process_numbers(lst,lambda x:x%2==0,lambda x:x*10))

# ## Task 8
# ## Even number -> square
# print(process_numbers(lst, lambda x: x%2==0, lambda x:x**2))
# print(process_numbers(lst, lambda x: x%2!=0, lambda x:x**3))


# In[86]:


## Hour 4
## Block 1
## task 
import numpy as np

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

## Task 1
print(np.dot(A,B)) ## Dot product
print(A.T) ## Transpose of A
print(A*B) # Element-wise multiply
print(A@B) ## Dot product
print(np.dot(A,A.T))


# In[87]:


## Task 6
A = np.array([[1,2,3],
              [4,5,6]])

print(A.T)


# In[ ]:


## Block 3
# Task 7
A = np.array([[1,2,3],
              [4,5,6]])

# Normalise row wise
# mean_row = np.mean(A,axis = 1,keepdims=True)
# print("mean_row ",mean_row,mean_row.shape)
# std_row= np.std(A,axis=1,keepdims=True)
# print("std_row :",std_row, std_row.shape)
# print((A - mean_row) / std_row)

## Task 8
## Normalise Column wise
# mean_col = np.mean(A,axis = 0,keepdims=True)
# print("mean_row ",mean_col,mean_col.shape)
# std_col= np.std(A,axis=0,keepdims=True)
# print("std_row :",std_col, std_col.shape)
# print((A - mean_col) / std_col)


# In[109]:


## Hour 5
## Block 1
## Task 1

import pandas as pd
df = pd.read_csv("Telco_Customer_Churn.csv")
# df.isnull().sum()
print((df["TotalCharges"]==" ").sum())
df["TotalCharges"] = df["TotalCharges"].replace(" ", np.nan)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])
# print((df["TotalCharges"]=="NaN").sum())
# print(df["TotalCharges"])
df["TotalCharges"].isnull()


# In[121]:


## Block 2
## Task 1
## For numeric column fill NaN with median
df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace= True)
print(df.head())
print(df["PaymentMethod"].unique())

## Task 
## For categorical column fill NaN with Mode
df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0],inplace=True)


# In[125]:


df["TotalCharges"].value_counts(dropna = False)


# In[ ]:


## insights
## Why median for numeric
## ----> Because median is robust to outliers,
# mean can be skewed by extreme values
# median can represent central tendency better in real world data

## Why mode for categorical
# mode gives most frequent category
# Keep data realistic
# Avoid including artificial values

## if data is normally distribute ---- mean can be used
## if skewed ---- median can be used


# In[ ]:


## Hour 6
import pandas as pd
import numpy as np

# data = {
#     "CustomerID": [1,2,3,4,5,6,7,8],
#     "Gender": ["Male","Female","Female","Male","","Female","Male"," "],
#     "Tenure": [12,24,"",36,48,60,"NA",72],
#     "MonthlyCharges": [29.85,56.95,53.85,"",70.7,99.65,89.1," "],
#     "TotalCharges": ["29.85","1889.5"," ","108.15","151.65","820.5","NaN"," "],
#     "Contract": ["Month-to-month","One year","Two year","Month-to-month","","One year","Two year","Month-to-month"]
# }
# df = pd.DataFrame(data)
# df


# In[ ]:


# df["MonthlyCharges"].value_counts(dropna = False)
# ## convert invalid to NaN first
# df.replace([""," ","NA","NaN"], np.nan, inplace=True)
# df = df.replace(r'^\s*$', np.nan, regex=True)
# df.isnull().sum()


# In[ ]:


## Hour 7

## Given a list
## return True if any duplicate exist or false otherwise

# lst = [1,2,3,4] # → False  
# lst1 = [1,2,3,1] # → True  
# def check_duplicate(lst):
#     return len(lst) != len(set(lst))
# print(check_duplicate(lst))


# In[140]:


## Hour 8
df = pd.read_csv("Telco_Customer_Churn.csv")
df.head()


# In[141]:


df.isnull().sum()


# In[142]:


df.info()


# In[147]:


## Converting TotalCharges to float

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")
# df.info()
df.duplicated().sum()

df.to_csv("cleaned_churn.csv",index=False)


# In[149]:


col = ["10", "20", "abc", "30"]
col = pd.to_numeric(col, errors="coerce")
col

