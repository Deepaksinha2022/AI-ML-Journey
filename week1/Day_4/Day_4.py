#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Day 4 

# Block 1

# lst = [10,15,20,25,30]
# for i in lst:
#     if i%2==0:
#         print(i)

## Numbers divisible by 5 but not by 10

# for i in lst:
#     if i%5==0 and i%10!=0:
#         print(i)


## Block 2

# data = {
#     "A": [45, 67, 89],
#     "B": [55, 60, 72],
#     "C": [30, 40, 50]
# }

# def results(data):
#     res = {}
#     for i in data:
#         total = 0
#         for j in data[i]:
#             total +=j 
#         avg = total/len(data[i])
#         if avg >=60:
#             res[i] = "Pass"
#         else:
#             res[i] = "Fail"
#     return res

# print(results(data))

## Task 2

# lst = [
#     {"name":"A","marks":[80,70,60]},
#     {"name":"B","marks":[40,50,45]},
#     {"name":"C","marks":[90,85,88]}
# ]

# # output - ["A","C"], average marks >=70

# def result(lst):
#     res = []
#     for i in lst:
#         total = 0
#         for j in i["marks"]:
#             total += j
#         average = total/len(i["marks"])
#         if average >=70:
#             res.append(i["name"])
#     return res
# print(result(lst))

## Task 3

# data = {
#     "math": {"A":90, "B":70},
#     "science": {"A":85, "B":60}
# }

# # Output - {"A":175, "B":130}

# def combine(data):
#     dc = {}
#     for subject in data:
#         for student in data[subject]:
#             if student in dc:
#                 dc[student] += data[subject][student]
#             else:
#                 dc[student] = data[subject][student]
#     return dc

# print(combine(data))


# In[ ]:


## Block 3

## Task 1 
data = [
    {"name":"A","scores":{"math":80,"eng":70}},
    {"name":"B","scores":{"math":40,"eng":50}},
    {"name":"C","scores":{"math":90,"eng":85}}
]

## Output

# {
#  "A":75,
#  "B":45,
#  "C":87.5
# }


# def score(data):
#     dc = {}
#     for student in data:
#             average = (student["scores"]["math"]+
#                        student["scores"]["eng"])/2
#             dc[student["name"]] = average
#     return dc

# print(score(data))  

## Task 2

## Output - ["A","C"]

# def average(data):
#     ls = []
#     for student in data:
#             average = (student["scores"]["math"]+
#                        student["scores"]["eng"])/2
#             if average >= 75:
#                   ls.append(student["name"])
#     return ls
# print(average(data))


## Task 3

# lst = [
#     {"dept":"IT","salary":50000},
#     {"dept":"HR","salary":40000},
#     {"dept":"IT","salary":60000},
#     {"dept":"HR","salary":45000}
# ]

## Output

# {"IT":55000, "HR":42500}

# def avg_salary(lst):
#     dc= {}
#     count = {}
#     for i in lst:
#         if i["dept"] in dc:
#             dc[i["dept"]] += i["salary"]
#             count[i["dept"]]+=1
#         else:
#             dc[i["dept"]] = i["salary"]
#             count[i["dept"]] = 1
#     for dept in dc:
#         dc[dept] = dc[dept]/count[dept]
#     return dc
# print(avg_salary(lst))


## Task 4

## Given
# data = ["apple","banana","apple","cherry","banana","apple"]

# ## output
# {"apple":3,"banana":2,"cherry":1}

# def fun(data):
#     dc = {}
#     for i in data:
#         if i in dc:
#             dc[i]+=1
#         else:
#             dc[i]=1
#     return dc
# print(fun(data))


# In[ ]:


## Block 4

## Task 1

# lst = ["apple","banana","apple","cherry","banana","apple"]

# d = {}

# for x in lst:
#     d[x] = d.get(x, 0) + 1

# print(d)

## Task 2

# Same input and output - most frequent item
#  one-pass max frequency

# lst = ["apple","banana","apple","cherry","banana","apple"]

# d = {}
# max_count = 0
# max_item = None

# for x in lst:
#     d[x] = d.get(x, 0) + 1
    
#     if d[x] > max_count:
#         max_count = d[x]
#         max_item = x

# print(max_item)


## Task - 3

# lst = [
#     {"dept":"IT","salary":50000},
#     {"dept":"HR","salary":40000},
#     {"dept":"IT","salary":60000},
#     {"dept":"HR","salary":45000}
# ]

# # Output - Average Salary per department

# def avg_salary(lst):
#     dc = {}
    
#     for i in lst:
#         dept = i["dept"]
#         salary = i["salary"]
        
#         if dept not in dc:
#             dc[dept] = [0,0]   # [sum, count]
        
#         dc[dept][0] += salary
#         dc[dept][1] += 1
    
#     return {k: v[0]/v[1] for k,v in dc.items()}

# print(avg_salary(lst))


# In[24]:


## Hour 2

## block 1
## Task 1 - Fibonacci

# def fibinacci(n):
#     res = [0,1]
#     if n==0:
#         return []
#     if n==1:
#         return [0]
#     for i in range(2,n):
#         next_value = res[-1] + res[-2]
#         res.append(next_value)

#     return res

# print(fibinacci(6))

## Task 2

## Sum of digits
# input = number, output = sum and product of digits

# def sum_prod(n):
#     sum = 0
#     prod = 1
#     while n>0:
#         mod = n%10
#         sum+= mod
#         prod = mod*prod
#         n=n//10
#     return sum,prod

# print(sum_prod(124))


## Block 3

## Task 3

# lst = [10, 3, 45, 2, 99, 23]
# max1 = float('-inf')
# max2 = float('-inf')
# for x in lst:
#     if x>max1:
#         max2=max1
#         max1=x
#     elif x>max2:
#         max2=x
# print(max1,max2)

## Task 4

## Given string
# str = "mississippi"

# Find:
# frequency of each char
# most frequent char

# dct= {}
# count = 0
# max_char = ""
# for s in str:
#     dct[s] = dct.get(s,0)+1
#     if dct[s]>count:
#         count=dct[s]
#         max_char = s
# print(dct)
# print("max_char",max_char)


## Block 3
## nth fibonacci only
# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     if n==2:
#         return 1
#     for i in range(2,n+1):
#         fibo = fib(n-1)+fib(n-2)

#     return fibo
# print(fib(10))

#0,1,2,3,5,8,13,21,34,55

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     a, b = 0, 1
    
#     for i in range(2, n+1):
#         a, b = b, a + b
    
#     return b
# print(fib(6))

## Task 7
# Largest subarray sum
# lst = [-2,1,-3,4,-1,2,1,-5,4]
# current_sum = lst[0]
# max_sum = lst[0]

# for i in range(1, len(lst)):
#     current_sum = max(lst[i], current_sum + lst[i])
#     max_sum = max(max_sum, current_sum)
# print(max_sum)

## Task 8
## input - "aabcccccaaa"
## Output - "a2b1c5a3"
# st = "aabcccccaaa"
# res = ""
# count = 1
# for i in range(1,len(st)):
#     if st[i] == st[i-1]:
#         count +=1
#     else:
#         res+= st[i-1]+str(count)
# res+= st[-1]+str(count)
# print(res)

# Task 9
# 1
# 2 1
# 3 2 1
# 4 3 2 1

for i in range(4):
    for j in range(i+2,1,-1):
        print(j-1,end=" ")
    print()


# In[ ]:


## Hour 3

## Block1
# Task 1
import math

math.sqrt(25)
math.ceil(3.2)
math.floor(3.1)

## Task2
math.factorial(6)



# In[ ]:


## Block 2

## Task 1
import random
# nums = [random.randint(1,100) for _ in range(5)]
# print(nums)

## Task 2
# lst = ["apple","banana","cherry","mango"]
# random.sample(lst,2)
# random.choice(lst)

# TASK 3 (INTERMEDIATE)

# Simulate:

# dice roll (1–6)
# run 10 times
# store results in list

# lst=[random.randint(1,6) for _ in range(10)]
# print(lst)
# dct={}
# for i in lst:
#     dct[i] = dct.get(i,0)+1
# dct


# In[ ]:


## Hour3 - Block 3

# def generate_numbers(n):
#         lst = [random.randint(1,100) for _ in range(n)]
#         return lst

# print(generate_numbers(8))

## Task 2
nums = [25,99,36,85,74,81,47,76]
# def analyze(nums):
#         total = 0
#         for num in nums:
#                 total = total+num
#         average = total/len(nums)
#         return max(nums), min(nums),average
# print(analyze(nums))

## Task 4
# nums = [25,99,36,85,74,81,47,76]
# def analyze(nums):
#         total = 0
#         count_odd = 0
#         count_even = 0
#         for num in nums:
#                 total = total+num
#                 if num%2==0:
#                         count_even+=1
#                 else:
#                         count_odd+=1
#         average = total/len(nums)
#         return max(nums), min(nums),average,count_even,count_odd
# print(analyze(nums))


# In[ ]:


## Block 4

## Task 1

# Random Simulation (Mini Project)
# 👉 Simulate:
# 100 dice rolls
# 👉 Store results
# import random
# lst = [random.randint(1,6) for _ in range(100)]
# print(lst)

## TAsk 2
# Frequency of each number (1-6)
# Most frequent number

# dct= {}
# for i in lst:
#     dct[i] = dct.get(i,0)+1
# count = 0
# max_num = None
# print(dct)
# for j in dct:
#     if dct[j]>count:
#         count = dct[j]
#         max_num = j
# print(" most frequent number", max_num)

## Task 4

# import random
# def roll_dice(n):
#     lst = [random.randint(1,6) for _ in range(n)]
#     return lst
# lst = roll_dice(50)
# print(lst)

# def analyze_dice(lst):
#     dct= {}
#     for i in lst:
#         dct[i] = dct.get(i,0)+1
#     count = 0
#     max_num = None
#     for j in dct:
#         if dct[j]>count:
#             count = dct[j]
#             max_num = j
#     return dct,max_num

# print(analyze_dice(lst))


# In[ ]:


## HOur 4

## Block 1

## Task 1
import numpy as np
arr = np.array([10,20,30,40,50])
# print(arr.mean())
# print(arr.sum())
# print(arr.std())

## Task 2

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.sum(axis = 0))
# print(arr.sum(axis = 1))

## Task 3
# arr = np.array([[10,20,30],
#                 [40,50,60],
#                 [70,80,90]])

# print(arr.max(axis=1))
# print(arr.min(axis=0))

## Task 4

## Normalize Array
# print((arr-(arr.mean()))/arr.std())


# In[208]:


## Block 2

## Task 1
# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.mean(axis=1))
# print(arr.mean(axis=0))

## Task 2

arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])

print(arr.sum(axis = 1))
print(arr.sum(axis = 0))


# In[211]:


## Block 3

## Task 1
# arr = np.array([10,20,30,40,50])

## Normalise

# print((arr-(arr.mean()))/arr.std())


## Task 2
arr = np.array([[10,20,30],
                [40,50,60]])

print((arr-(arr.mean()))/arr.std())

## Task 3
## Normalise Columnwise
print((arr-(arr.mean(axis =0)))/arr.std(axis=0))


# In[215]:


## Hour 5

## Block 1
## Task 1

import pandas as pd

df1 = pd.DataFrame({
    "id":[1,2,3],
    "name":["A","B","C"]
})

df2 = pd.DataFrame({
    "id":[1,2,4],
    "salary":[1000,2000,3000]
})

##
pd.merge(df1,df2, on='id')


# In[220]:


## Block 2

## Task 1
## Inner join
print(pd.merge(df1, df2, on="id", how="inner"))

## Task 2
## Left join
print(pd.merge(df1, df2, on="id", how="left"))

## task 3
## Right join
print(pd.merge(df1, df2, on="id", how="right"))

## Task 4
## Outer Join
pd.merge(df1, df2, on="id", how="outer")


# In[228]:


## Block 3
## Task 1

df1 = pd.DataFrame({
    "name":["A","B"],
    "marks":[80,90]
})

df2 = pd.DataFrame({
    "name":["C","D"],
    "marks":[70,60]
})

# pd.concat([df1,df2])

# Horizontal Concat
pd.concat([df1,df2],axis=1)
# print(pd.concat([df1,df2],ignore_index="True"))


# In[231]:


# Hour 6
# Block 1
# Task 1

df1 = pd.DataFrame({
    "name":["A","B"],
    "marks":[80,90]
})

df2 = pd.DataFrame({
    "name":["C","D"],
    "marks":[70,60]
})

## Block 2
## Inner merge

pd.merge(df1,df2,on = "name",how="inner")

## Left merge
pd.merge(df1,df2,on = "name",how="left")


# In[ ]:


## Hour -5 
## Given prices , maximise profit, buy at minimum, sell at max

prices= [7,1,5,3,6,4]
def max_prof(prices):
    min_price= prices[0]
    max_profit= 0
    for i in prices:
        if i<min_price:
            min_price=i
        profit = i-min_price
        if profit>max_profit:
            max_profit = profit
    return max_profit
print(max_prof(prices))


# In[234]:


## Hour 8
import pandas as pd

df = pd.read_csv("Telco_Customer_Churn.csv")
df.head()


# In[237]:


## Block 1

# df.groupby("Churn")["MonthlyCharges"].mean()

## Task 2
df.groupby("Churn")["tenure"].mean()


# In[ ]:


## Visual Representataion
df.boxplot(column="MonthlyCharges", by="Churn")


# In[239]:


df.boxplot(column="tenure", by="Churn")


# In[ ]:


## Insights
## Tenure differentiate better as monthly charges overlap for churn 
# and non churn but in tenure the differentiation is quite high
## churn customers have less tenure but similar monthly charges
## than non churn.

