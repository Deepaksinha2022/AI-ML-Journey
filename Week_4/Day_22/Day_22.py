#!/usr/bin/env python
# coding: utf-8

# 1. What is Precision?
# Precision tells: “Out of all predicted positives, how many are actually correct?”
# 
# precision = TP /(TP+FP)
# 
# Spam filter , Hiring - high precision needed

# Hour 4
# F1 Score
# = 2*P*R/(P+R)
# 
# When to Use F1 - harmonic mean on precision and recall
# When:
# Both FP and FN matter
# F1 forces model to perform well on both precision and recall
# 
# Why do we need F1 Score?
# Problem:
# Precision alone ❌
# Recall alone ❌
# We need balance
# 
# why harmonic mean - beacuse it punishes the imbalance
# F1 represents the balance between precision and recall in a single metric.”
# “F1 is used when both false positives and false negatives are important.

# In[3]:


## Hour 5 - Implementation
from sklearn.metrics import precision_score, recall_score, f1_score

y_true = [1,0,1,1,0,1]
y_pred = [1,1,1,0,0,1]

print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1:", f1_score(y_true, y_pred))


# In[11]:


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

X = [[1],[2],[3],[4],[5],[6]]
y = [0,0,0,1,1,1]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1:", f1_score(y_test, y_pred))

# Edge case handling
y_pred = [0,0]
precision_score(y_test, y_pred, zero_division=0)


# Case 1
y_true = [1,1,1,1]
y_pred = [1,1,1,1]

# Testing
y_true = [1,1,1,1]
y_pred = [1,1,1,1]

print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1:", f1_score(y_true, y_pred))

# Case 2
y_true = [1,1,1,1]
y_pred = [0,0,0,0]

print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1:", f1_score(y_true, y_pred))


# In[14]:


# Hour 7
y_true = [1,0,1,1,0,1,0,0,1,0]
y_prob = [0.95,0.6,0.8,0.4,0.3,0.7,0.2,0.1,0.65,0.5]
from sklearn.metrics import confusion_matrix

thresholds = [0.3,0.5,0.7]
for i in thresholds:
    y_pred = [1 if x>=i else 0 for x in y_prob]
    
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel() 
    print(f"Threshold:{i} y_pred:- {y_pred} TP: {tp} FP: {fp} FN: {fn} TN: {tn}")
    print(f"Precision_Score : {precision_score(y_true, y_pred)} Recall_score:{recall_score(y_true, y_pred)}")
    print(f"F1 score: {f1_score(y_true, y_pred)}")


# In[16]:


## DSA
# Check if there exists a subarray of length ≥ 2 whose sum is a multiple of k
nums = [23,2,4,6,7]
k = 6

Output: True
# (subarray [2,4] → sum = 6)

def checkSubarraySum(nums, k):
    prefix_map = {0: -1}
    current_sum = 0
    
    for i, num in enumerate(nums):
        current_sum += num
        remainder = current_sum % k
        
        if remainder in prefix_map:
            if i - prefix_map[remainder] > 1:
                return True
        else:
            prefix_map[remainder] = i
    
    return False


# In[35]:


def sumarr(nums,k):
    prefix_sum =0
    hashmap ={0:-1}
    for i , num in enumerate(nums):
        prefix_sum+=num
        remainder = prefix_sum%k

        if remainder in hashmap:
            if i - hashmap[remainder]>1:
                return True
        else:
            hashmap[remainder] = i
    return False
# print(sumarr(nums,k))

# nums = [23,2,6,4,7] 
# k=6  
# nums = [1,2,3]
# k=5  
# nums = [0,0]
# k=0
nums = [2,3,1,2,4,3]
k = 6
print(sumarr(nums,k))


# In[36]:


## Pivot Index
# Find index where:
# left sum == right sum
nums = [1,7,3,6,5,6] 
# - at index = 3 left sum = 11 = right sum
def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0
    
    for i, num in enumerate(nums):
        right_sum = total - left_sum - num
        
        if left_sum == right_sum:
            return i
        
        left_sum += num
    
    return -1
nums = [2,1,-1]
print(pivotIndex(nums))


# In[34]:


def pivotindex(nums):
    total = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        right_sum = total - left_sum - num

        if left_sum == right_sum:
            return i
        left_sum+=num
    return -1

print(pivotindex(nums))

