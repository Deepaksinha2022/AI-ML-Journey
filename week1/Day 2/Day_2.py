#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Hour 1 ------> Block 1


# In[3]:


""" print 
1 2 3
1 2 3
1 2 3"""

for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()


# In[4]:


for i in range(1,4):
    for j in range(1,4):
        print(i, end=" ")
    print()


# In[5]:


for i in range(1,4):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


# In[6]:


for i in range(1,4):
    for j in range(i,i+3):
        print(j, end=" ")
    print()


# In[7]:


for i in range(1,4):
    for j in range(3,0,-1):
        print(j, end=" ")
    print()


# In[8]:


## Block 2------> Functions

def square(n):
    return n**2

print(square(5))


# In[9]:


## Function returning multiple values

def fun(n):
    return n**2,n**3

print(fun(4))


# In[10]:


def even_odd(n):
    if n%2 ==0:
        return "even"
    else:
        return "odd"
    
print(even_odd(24))


# In[11]:


## Factorial of a number

def fact(n):
    fct=1
    for i in range(1,n+1):
        fct = i*fct
    return fct

print(fact(5))


# In[12]:


## Reverse a number
def rev_num(n):
    rev = 0
    while n>0:
        mod = n%10
        rev = rev*10 + mod
        n= n//10
    return rev

print(rev_num(123))


# In[13]:


## Sum of digits

def sum_digits(n):
    sum = 0
    while n>0:
        mod = n%10
        sum += mod
        n=n//10
    return sum

print(sum_digits(123))


# In[14]:


## Count of Digit

def count_digit(n):
    count = 0
    while n>0:
        n = n//10
        count+= 1
    return count
print(count_digit(1238963))


# In[15]:


## Count number of Vowels

def count_vowels(str):
    vow = ["a","e","i","o","u"]
    count = 0
    for i in str:
        if i in vow:
            count+=1
    return count

print(count_vowels("Anvi Pritha"))


# In[16]:


## Count number of Consonants

def count_vowels(str):
    vow = ["a","e","i","o","u"]
    count = 0
    for i in str:
        if i not in vow:
            count+=1
    return count

print(count_vowels("Jyoti"))


# In[17]:


## Count of each vowel

def count_vow(s):
    dct = {}
    vowels = ["a","e","i","o","u"]
    
    for ch in s:
        if ch in vowels:
            if ch in dct:
                dct[ch] += 1
            else:
                dct[ch] = 1
                
    return dct

print(count_vow("hellouiiuo"))


# In[18]:


## BLOCK 2

## Write Lambda return square

square = lambda x: x*x

print(square(5))


# In[19]:


## Max Value

max_value = lambda a,b: a if a>b else b

print(max_value(17,89))


# In[20]:


## Lambda with map

lst = [1,2,3,4]
result = list(map(lambda x:x *x ,lst))
print(result)


# In[21]:


## Check prime or not

def is_prime(n):
    if n ==0 or n == 1:
        return "invalid"
    if n == 2:
        return "prime"
    for i in range(2,n+1):
        if n%i == 0:
            return "not prime"
        else:
            return "Prime"
        
print(is_prime(79))


# In[22]:


## Count of Divisor

def divisor_count(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count+= 1
    return count

print(divisor_count(17))
        


# In[23]:


## Sum of All Divisors
def divisor_sum(num):
    sum = 0
    for i in range(1, num+1):
        if num % i == 0:
            sum+= i
    return sum

print(divisor_sum(10))


# In[24]:


## HOUR 4 ---- NumoPy

import numpy as np

ar = np.arange(2,9)
print(ar)
print(ar[0],ar[5])

print(ar[1:4])


# In[25]:


## 2D array

a2 = np.arange(5,11).reshape(3,2)
print(a2)
print(a2[0])
print(a2[:,1])


# In[26]:


## Boolean Indexing

a3 = np.arange(1,8)
print(a3)
print(a3[a3>4])

a4 = np.arange(5,35,5)
print(a4)
print(a4[(a4%5==0) & (a4>15)])


# ## HOUR 5 ----------- Pandas 
# 

# In[59]:


# import pandas as pd
# df = pd.read_csv("Telco_Customer_Churn.csv")
# # df.head()
# # df[["PhoneService","MonthlyCharges"]]
# ## First Five Rows
# #df.head(5)

# ## Only two specific column
# df[["SeniorCitizen" , "Partner"]].head()


# In[60]:


#df.loc[:4, ["SeniorCitizen", "Partner"]]


# In[58]:


#df.head()


# In[30]:


## Filter rows where column value is greater than some value

# df[df["MonthlyCharges"]>30]


# In[57]:


## Task 2 ---- Filter rows where one condition 
# and another condition is met
# df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")
# df[(df["tenure"] >5) & (df["TotalCharges"]>100)].head()


# In[56]:


## Task 3 

#df[(df["MonthlyCharges"] == 56.95) | (df["TotalCharges"]>800)]


# In[55]:


## Loc and iloc

#df.loc[:5, ["PaperlessBilling","PaymentMethod"]]

## iloc

#df.iloc[:6,2:7]


# In[53]:


## Select iloc from rows 10 to 20 and columns 2 to 4

#df.iloc[10:21,2:5]


# In[35]:


## Hour 6 

## Filter customer where tenure>12

#df[df["tenure"]>12].head()

# df[(df["tenure"] > 12 ) & (df["MonthlyCharges"] > 50)]

## How many custmoers satisfy above condition

# len(df[(df["tenure"] > 12 ) & (df["MonthlyCharges"] > 50)])



# In[ ]:


## LeetCode problems 

## Move Zeroes

lst = [0,1,0,3,12]
j = 0
for i in range(len(lst)):
    if lst[i]!=0:
        lst[j],lst[i] = lst[i],lst[j]
        j+=1
print(lst)


# In[37]:


#### Hour 8 


# In[52]:


#df.isnull().sum()


# In[51]:


#df.isnull().sum()[df.isnull().sum()>0]


# In[61]:


#df.dtypes


# In[49]:


#df.select_dtypes(include = "number")


# In[48]:


#df.select_dtypes(include ="object")


# In[62]:


#df["tenure"].mean()


# In[63]:


#df["MonthlyCharges"].mean()


# In[64]:


## Find average tebure of customer who churn

#df[df["Churn"] == "Yes"]["tenure"].mean()

