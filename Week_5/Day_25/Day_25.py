#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Day 25
# KNN
# KNN predicts based on nearby data points
# KNN does not learn a model — it defers learning until prediction and uses distance to decide output.
# its called lazy learning as thers is no training - shift computation from training time to inference time


# In[ ]:


points = [1,2,8,9]
labels = ['Low','Low','High','High']

new_point = 7

distances = []

for i in range(len(points)):
    d = abs(points[i] - new_point)
    distances.append((d, labels[i]))

distances.sort()
print(distances)


# In[ ]:


# What is KNN?
# It is a instance based model which stores all the points and compare at predictions and then decides using neighbors

# it predicts using nearest data points and doesnot learn any explicit model
# it has core idea - similar inputs -  similar outputs
# it is reliant on distance = similarity

# Working steps are - new point - calculate distance from each point-- select k neighbors ---majority vote or average 
# its nature - lazy learning - stores entire dataset - computation happens at predictions

# Complexity - per prediction - O(N*d) , n = number of samples and d = feature
# it is slow for large dataset
# Small K - high variance (noise sensitive)
# Large k - high bias (stable but smooth)

# how does it fails
# random data - no pattern
# overlapping classes - unstable predictions
# irrelevant features - wrong distance
# large dataset - slow prediction

## KNN is a lazy distance based algorith that predicts by finding nearest neighbors using a distance metric and taking a majority vote


# In[ ]:


# Hour 2
# How to calculate distance
# uclidean Distance (L2)
# Straight-line distance
# d = sqrt((x1-x2)**2+(y1-y2)**2)
# Straight line distance - penalises long distance heavily due to square,sensitive to outliers, works well when features are smooth and dimensions are low

# Manhattan Distance (L1)
# Grid based distance d = |x1-x2| + |y1-y2|
# less sensitive to outliers and works better in high dimension

# Situation	                        Euclidean	                     Manhattan
# Large feature difference	    heavily penalized	               linear penalty
# High dimensions	                    weak	                       better
# Geometry	                           circular                     	diamond

# In euclidean - due to square all points at a same distance form a circle, nearest neighbors are points inside the circle
# in manhattan - all point at same distance form a diamond

# Curse of dimensionality
# when no. of feature incrases - distance becomes similarc- KNN cannot distinguish features well so performance decreases

# Scaling problem
# Features:
# Age → 20–60
# Salary → 20,000–200,000
# so distance formula here ignores age and model only uses salary as its value>>> age
# solution - standardisation - x' = (x-mean)/sd -----> mean = 0 ans sd = 1
           # - Normalisation --- x' = (x-min)/(max-min) ------> range 0 to 1 

# after feature scaling all feature now contribute equally to distance


# In[ ]:


## 
import numpy as np

A = np.array([25,30000])
B = np.array([40,50000])
C = np.array([35,150000])
P = np.array([30,40000])

def euclidean(a,b):
    return np.sqrt(np.sum((a-b)**2))

print(euclidean(A,P))
print(euclidean(B,P))
print(euclidean(C,P))


# In[ ]:


## Hour 3
# Selection of K
# if k is very less suppose 1 - model uses only nearest point - chances of overfitting - very sensitive to noise - also decision boundary becomes very irregular
## this is high variance and low bias
# if k becomes very large - ignored local structure , always predicts majority class - very smooth boundary = high bias and low variance

# Bias
# - over simplification - missing patterns - model too rigid

# Variance - error due to over sensitivity - model react to noise - unstable predictions


# In[ ]:


## Effect of K
from collections import Counter

neighbors = ['Low','Low','High']
print(Counter(neighbors).most_common(1))

# Large K is biased toward majority class
# too small data - large K meaningless

# Tie Situation
# Even K may cause tie

# Solution:
# Use odd K
# or distance-weighted voting

# K ↑ → smoother decision → more bias
# K ↓ → sharper decision → more variance


# In[2]:


# Scaling 
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([
    [25, 30000],
    [40, 150000]
])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X_scaled)


# In[5]:


## Apply KNN
# Step 1 - Distance function 

import numpy as np

def euclidean(a,b):
    return np.sqrt(np.sum(a-b) **2)

# Step 2 - KNN predict function

from collections import Counter

def knn_predict(X_train, y_train, x_new, k):
    
    distances = []
    
    # Step 1: compute distances
    for i in range(len(X_train)):
        d = euclidean(X_train[i], x_new)
        distances.append((d, y_train[i]))
    
    # Step 2: sort by distance
    distances.sort(key=lambda x: x[0])
    
    # Step 3: pick top K
    neighbors = distances[:k]
 
    # Step 4: extract labels
    labels = [label for _, label in neighbors]

    
    # Step 5: majority vote
    return Counter(labels).most_common(1)[0][0]

X_train = np.array([
    [1,2],
    [2,3],
    [8,8],
    [9,9]
])

y_train = ['Low','Low','High','High']

x_new = np.array([3,3])

print(knn_predict(X_train, y_train, x_new, k=3))


# In[11]:


## try with k -1 ,k=3,k=4
# k=4
#, k=3, k=4
X_train = np.array([
    [1,2],
    [2,3],
    [3,3],
    [8,8],
    [9,9]
])

y_train = ['Low','Low','High','High','High']
print(knn_predict(X_train, y_train, x_new, k=4))


# In[12]:


# using partial sort
import heapq


def knn_predict(X_train, y_train, x_new, k):
    
    distances = []
    
    # Step 1: compute distances
    for i in range(len(X_train)):
        d = euclidean(X_train[i], x_new)
        distances.append((d, y_train[i]))
    
    # Step 3: pick top K
    neighbors = heapq.nsmallest(k, distances, key=lambda x: x[0])
 
    # Step 4: extract labels
    labels = [label for _, label in neighbors]

    
    # Step 5: majority vote
    return Counter(labels).most_common(1)[0][0]

X_train = np.array([
    [1,2],
    [2,3],
    [8,8],
    [9,9]
])

y_train = ['Low','Low','High','High']

x_new = np.array([3,3])

print(knn_predict(X_train, y_train, x_new, k=3))


# In[14]:


# Giving nearer points more weights
from collections import defaultdict

def knn_weighted(X_train, y_train, x_new, k):
    
    distances = []
    
    for i in range(len(X_train)):
        d = euclidean(X_train[i], x_new)
        distances.append((d, y_train[i]))
    
    # get K nearest
    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]
    
    # weighted voting
    weights = defaultdict(float)
    
    for dist, label in neighbors:
        if dist == 0:
            return label  # exact match
        
        weights[label] += 1 / dist
    
    # pick label with highest weight
    return max(weights, key=weights.get)

X_train = np.array([
    [1,2],
    [2,3],
    [8,8],
    [9,9]
])

y_train = ['Low','Low','High','High']

x_new = np.array([3,3])

print(knn_predict(X_train, y_train, x_new, k=3))


# In[16]:


# using Kneighbors classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np

# Data
X = np.array([
    [1,2],
    [2,3],
    [8,8],
    [9,9]
])

y = ['Low','Low','High','High']

# Scaling (IMPORTANT)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_scaled, y)

# New point
x_new = np.array([[3,3]])
x_new_scaled = scaler.transform(x_new)

print(knn.predict(x_new_scaled))


# In[ ]:


# uniform' assigns equal weight to all neighbors, while 'distance' assigns higher weight to closer neighbors and lower weight to farther ones, making predictions more influenced by nearby points.”


# In[ ]:


# Hour 7 - Mini Task - Try different K and to derive the best K

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

X = np.array([
    [1,2],[2,3],[3,3],
    [8,8],[9,9],[10,10]
])

y = ['Low','Low','Low','High','High','High']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

for k in range(1, len(X_train)+1):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    
    y_pred = knn.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"K={k}, Accuracy={acc}")


# In[19]:


# Using weights = distance in above mini task
X = np.array([
    [1,2],[2,3],[3,3],
    [8,8],[9,9],[10,10]
])

y = ['Low','Low','Low','High','High','High']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

for k in range(1, len(X_train)+1):
    knn = KNeighborsClassifier(n_neighbors=k,weights= 'distance')
    knn.fit(X_train, y_train)
    
    y_pred = knn.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"K={k}, Accuracy={acc}")


# In[ ]:


## trying without scaling
X = np.array([
    [1,2],[2,3],[3,3],
    [8,8],[9,9],[10,10]
])

y = ['Low','Low','Low','High','High','High']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

# scaler = StandardScaler()
#X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

for k in range(1, len(X_train)+1):
    knn = KNeighborsClassifier(n_neighbors=k,weights= 'distance')
    knn.fit(X_train, y_train)
    
    y_pred = knn.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"K={k}, Accuracy={acc}")


# In[ ]:


# When KNN works well
# ✅ Small dataset
# ✅ Clear clusters
# ✅ Low dimensions
# ✅ Proper scaling

# when KNN doesnt works well
# Imbalance data
# large data
# high dimensions
# Many irrelevant features

# KNN is a lazy, instance-based learning algorithm that makes predictions by computing distances to training samples and selecting the majority label among the nearest neighbors, with performance heavily dependent on distance metric, feature scaling, and choice of K.”


# In[27]:


# DSA
# Problem 1 — Subarray Sum Equals K
nums = [1,2,-5,5,4,1,3,2]
k = 5
def subarr_sum(nums,k):
    hashmap = {0:1}
    prefix_sum = 0
    count =0

    for num in nums:
        prefix_sum+= num

        if prefix_sum -k in hashmap:
            count+= hashmap[prefix_sum-k]
        hashmap[prefix_sum] = hashmap.get(prefix_sum,0)+1
    return count
print(subarr_sum(nums,k))


# In[30]:


# Sliding window example
# Longest subarray with sum ≤ K
nums = [1,2,-5,5,4,1,3,2]
k = 4
def longest_subarray(nums, k):
    left = 0
    curr_sum = 0
    max_len = 0
    
    for right in range(len(nums)):
        curr_sum += nums[right]
        
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
print(longest_subarray(nums,k))

