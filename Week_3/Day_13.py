#!/usr/bin/env python
# coding: utf-8

# In[5]:


## Day 13
## Hour 1
## block 1
import pandas as pd
df = pd.read_csv('Telco_Customer_Churn.csv')
df.head()
df.columns
y = df["Churn"]
X = df.drop("Churn", axis=1)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y   # VERY IMPORTANT for churn
)


# In[6]:


print(X.shape)
print(X_train.shape)
print(X_test.shape)


# In[ ]:


print(y.value_counts(normalize=True))
print(y_train.value_counts(normalize=True))
print(y_test.value_counts(normalize=True))


# In[13]:


## Hour 6

## Block 1
## Target distribution check
print(y_train.value_counts(normalize=True))
print(y_test.value_counts(normalize=True))


# In[ ]:


## Numerical features Disribution
import matplotlib.pyplot as plt

X_train["tenure"].hist()
plt.title("Train")
plt.show()

X_test["tenure"].hist()
plt.title("Test")
plt.show()

## for MonthlyCharges
X_train["MonthlyCharges"].hist()
plt.title("Train_MonthlyCharges")
plt.show()

X_test["MonthlyCharges"].hist()
plt.title("Test_MonthlyCharges")
plt.show()


# In[18]:


print(X_train.describe())
print(X_test.describe())


# In[19]:


## Categorical features distribution
print(X_train["Contract"].value_counts(normalize=True))
print(X_test["Contract"].value_counts(normalize=True))


# In[20]:


## Compare churn distribution
print(y_train.value_counts(normalize=True))
print(y_test.value_counts(normalize=True))


# In[25]:


## selecting columns with only numerical features
numerical_cols = [col for col in X_train.columns if X_train[col].dtype in ["int64", "float64"]]
print(numerical_cols)
print(X_train.columns)
X_train.head()


# In[26]:


## Compare Categorical features distribution
train_dist = X_train["Contract"].value_counts(normalize=True)
test_dist = X_test["Contract"].value_counts(normalize=True)

compare = pd.concat([train_dist, test_dist], axis=1)
compare.columns = ["Train", "Test"]

print(compare)


# In[27]:


compare.plot(kind="bar")
plt.title("Contract Distribution")
plt.show()


# In[ ]:


## Hour 7
## leetCode
nums=[2,7,11,15]
target=9    
output = [0,1]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print([i,j])

def two_sum(nums, target):
    seen={}
    for i,num in enumerate(nums):
        if target-num in seen:
            return [seen[target-num],i]
        seen[num]=i
print(two_sum(nums, target))


# In[46]:


lst = ["eat","tea","tan","ate","nat","bat"]

# 👉 Output:
# [["eat","tea","ate"], ["tan","nat"], ["bat"]]

def group_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return list(anagram_dict.values())

print(group_anagrams(lst))


# In[ ]:


## hour 8
## Block 1
X = df.drop("Churn", axis=1)
y = df["Churn"]

print(X.columns)

## Remove useless features
X = X.drop(["customerID"], axis=1)
print(X.columns)

## Block 3
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

