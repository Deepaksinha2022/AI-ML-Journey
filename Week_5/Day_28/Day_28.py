#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Decision Tree 

from sklearn.tree import DecisionTreeClassifier

X = [
    [22], [23], [45], [46]
]

y = ["Yes", "Yes", "No", "No"]

model = DecisionTreeClassifier(
    max_depth=3,
    min_samples_split=4,
    min_samples_leaf=2
)


# In[1]:


from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier

X = [[22], [23], [45], [46]]
y = ["Yes", "Yes", "No", "No"]

model = DecisionTreeClassifier(max_depth=2)
model.fit(X, y)

plt.figure(figsize=(8,5))

plot_tree(
    model,
    feature_names=["Age"],
    class_names=["No", "Yes"],
    filled=True
)

plt.show()


# In[ ]:




