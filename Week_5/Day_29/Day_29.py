#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Decision Tree Implementation
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X, y)


# In[ ]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = DecisionTreeClassifier(max_depth=3)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(accuracy_score(y_test, pred))


# In[ ]:


# 1. Pruning Techniques
# 🔥 Goal
# Reduce overfitting by removing unnecessary branches.

# 🔹 Pre-Pruning
# Stop tree growth early.
# Important parameters
# max_depthmin_samples_splitmin_samples_leafmax_leaf_nodes
# Risk


# too aggressive → underfitting



# 🔹 Post-Pruning
# Build full tree first, then remove weak branches.
# Benefit


# better generalization



# 🔹 Cost Complexity Pruning
# ccp_alpha


# small alpha → larger tree


# large alpha → smaller tree



# 🌳 2. Depth & Leaf Nodes

# 🔹 Depth
# Controls tree complexity.
# More depth → lower bias → higher variance

# 🔹 Leaf Nodes
# Final prediction regions.
# More leaves → finer partitions → memorization risk

# 🔹 Important intuition
# 100 samples + 100 leaves→ likely memorization

# 🌳 3. Feature Importance

# 🔥 Meaning
# How much a feature reduces impurity across all splits.

# 🔹 High importance
# Feature contributes strong impurity reduction.

# 🔹 Important caution
# Importance ≠ causation

# 🔹 Correlated features
# One feature may dominate importance.

# 🔹 If feature never used
# importance = 0

# 🌳 4. Bias-Variance in Trees

# 🔹 Shallow Tree
# High biasUnderfitting

# 🔹 Deep Tree
# High varianceOverfitting

# 🔹 Core tradeoff
# Complexity ↑→ Bias ↓→ Variance ↑

# 🌳 5. Hyperparameter Tuning

# 🔥 Goal
# Find best generalization performance.

# 🔹 Important parameters
# max_depthmin_samples_splitmin_samples_leafmax_leaf_nodescriterion

# 🔹 Validation accuracy > training accuracy
# High train accuracy alone may indicate overfitting.

# 🔹 GridSearchCV
# GridSearchCV()
# tries multiple parameter combinations automatically.

# 🌳 6. Decision Tree vs KNN vs Naive Bayes
# ModelLearns UsingKNNsimilarity / distanceNaive BayesprobabilitiesDecision Treerules / splits

# 🔹 KNN
# lazy learning
# slow prediction
# scaling sensitive

# 🔹 Naive Bayes
# probabilistic
# very fast
# assumes feature independence

# 🔹 Decision Tree
# interpretable
# handles non-linear boundaries
# high variance

# 🌳 7. Important Concepts

# 🔹 Trees are greedy
# choose locally best split

# 🔹 Trees are high variance
# Small data changes can create different trees.

# 🔹 Trees handle non-linear boundaries
# Recursive splits create flexible regions.

# 🔹 Trees are white-box models
# Predictions are human-readable.

# 🌳 8. Overfitting Signals

# 🔹 Overfitting
# Train accuracy highTest accuracy low

# 🔹 Underfitting
# Train accuracy lowTest accuracy low

# 🌳 9. Final Mental Models

# 🔥 Tree Learning
# Question→ Split→ Purity→ Repeat→ Prediction

# 🔥 Complexity Tradeoff
# Simple tree → underfitBalanced tree → generalizeDeep tree → overfit

# 🔥 Feature Importance
# Useful feature→ better split→ more impurity reduction→ higher importance

# 🎯 One-Line Interview Definition

# “Decision Trees are supervised learning models that recursively partition data using impurity reduction measures to create interpretable rule-based predictions.”

