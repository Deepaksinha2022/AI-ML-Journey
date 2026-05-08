#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Hour 1
# Decision Boundary
# - a line or surface that separates different classes in feature space
# Boundary emerges from data
# new point gets lable of majority nearest neighbor
# Value of K controls the boundary shape - small k - jagged boundary  large K - smooth boundary
# data disribution - clustered - clean boundary ,mixed - messy boundary
# euclidean - circular and manhattan - diamond influence
# overlapping data - boundary becomes - unclear and unstable
# sparse data - boundary becomes unreliable and large empty regions

# In KNN, the decision boundary is not explicitly learned but emerges from the distribution of training data and the choice of K, and its shape depends on how many neighbors are considered and how they are distributed in space.”

# Increasing K averages the influence of multiple nearby points, reducing sensitivity to individual noisy points and resulting in a smoother, more stable decision boundary.

# When data is highly overlapping, neighbors from different classes are mixed, causing inconsistent majority voting and resulting in an unstable and poorly defined decision boundary.

# KNN boundary is completely data-driven — if data changes, boundary changes instantly.

# if k = data points thers is no real boundary, model predicts majority class, entire space becomes one region

# When K equals the number of training samples, KNN degenerates into a majority class classifier with no meaningful decision boundary


# In[ ]:


# Effect of Noise -------> Hour 2
# “KNN is highly sensitive to noisy data because it relies on local neighborhoods, and while increasing K can reduce variance, it cannot fully eliminate the impact of noisy or overlapping data.”


# In[ ]:


## Curse of dimentionality
# Number of features = dimension
# in high dimension - all points alomst equally distant and nearest neighbor is no longer meaningful

# higher dimensions accumulates noise which destroys similarity, unreliable neigbors

# More dimensions → distance differences shrink → neighbors unclear → KNN fails

# More irrelevant features → noisy distance → bad neighbors
# Fewer relevant features → clean distance → good neighbors



# In[ ]:


# Hour 4 - performance limitation

# more distance calculation - O(nxd) - more time taken
# more memory usage as it stores the data
# high dimension data - distance becomes meaningless 
# scaling requirement - not scaling lead to wrong prediction and bad prediction
# Sensitive to noise

# KNN shifts computational burden from training to inference, which is why it struggles in latency-sensitive application

# reducing data size may improve the speed of prediction but accuracy may decrease as less data means less knowledge


# In[ ]:


# optimisation ideas

# 1. use kD tree
 #---- split data along one dimension and then split again - build heirarchical structure
 #---- instead of checking all points , it search only relevant regions
 #---- faster neighbor search - but works only in lower dimensions

# 2. Ball Tree
 #---- group data into clusters (balls) 
 #---- works better in higher dimensions

# 3. Approximate KNN
 #---- dont find exact neighbors - find close enough ones - speed increases but accuracy decreases

# 4. Dimentionality reduction
 #---- use PCS 
 #---- feature selection

# 5. data Reduction

# Low dimensions → KD-tree works
# Medium → Ball tree helps
# High dimensions → brute-force often better

# For large, high-dimensional datasets, we first reduce dimensionality using PCA or feature selection and then use approximate nearest neighbor methods instead of brute-force to achieve scalable and efficient predictions.”


# In[9]:


# Applying KNN
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
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

for k in range(1, len(X_train)+1):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    
    y_pred = knn.predict(X_test)
    print(k, accuracy_score(y_test, y_pred))


# In[14]:


## add noise
X_noisy = np.append(X, [[5,5]], axis=0)
y_noisy = y + ['Low']  # wrong label

X_noisy_train, X_noisy_test, y_noisy_train, y_noisy_test = train_test_split(
    X_noisy, y_noisy, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_noisy_train = scaler.fit_transform(X_noisy_train)
X_noisy_test = scaler.transform(X_noisy_test)

for k in range(1, len(X_noisy_train)+1):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_noisy_train, y_noisy_train)
    y_noisy_pred = knn.predict(X_noisy_test)
    print(k, accuracy_score(y_noisy_test, y_noisy_pred))


# In[15]:


# removing scaler
X = np.array([
    [1,2],[2,3],[3,3],
    [8,8],[9,9],[10,10]
])

y = ['Low','Low','Low','High','High','High']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

for k in range(1, len(X_train)+1):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    
    y_pred = knn.predict(X_test)
    print(k, accuracy_score(y_test, y_pred))


# In[16]:


# add irrelevant
random_feature = np.random.randint(0,100,(len(X),1))
X_bad = np.hstack((X, random_feature))

X_bad_train, X_bad_test, y_train, y_test = train_test_split(
    X_bad, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_bad_train = scaler.fit_transform(X_bad_train)
X_bad_test = scaler.transform(X_bad_test)

for k in range(1, len(X_train)+1):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_bad_train, y_train)
    
    y_pred = knn.predict(X_bad_test)
    print(k, accuracy_score(y_test, y_pred))


# In[25]:


# Minimum Size Subarray Sum >=k

nums = [1,1,1,0,1]
k = 4
def min_sub_arr(nums,target):
    current_sum = 0
    left = 0
    min_len = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum>=target:
            min_len=min(min_len,right-left+1)
            current_sum-= nums[left]
            left+=1
        
    return 0 if min_len == float('inf') else min_len

print(min_sub_arr(nums,k))

