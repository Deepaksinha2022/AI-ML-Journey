#!/usr/bin/env python
# coding: utf-8

# In[3]:


## Day -14
import pandas as pd
df = pd.read_csv('Telco_Customer_Churn.csv')
df.head()

## Cleaning the data
#df.info()
df.isnull().sum().sum()

(df.isnull().sum() / len(df)) * 100

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("y_train.csv") 
y_test = pd.read_csv("y_test.csv")   

X_train["TotalCharges"] = pd.to_numeric(X_train["TotalCharges"], errors="coerce")
X_test["TotalCharges"] = pd.to_numeric(X_test["TotalCharges"], errors="coerce")

## Identifying the categorical and numerical columns
num_cols = X_train.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X_train.select_dtypes(include=["object"]).columns

## Handle missing values
## Handle numerical missing values using median imputation
from sklearn.impute import SimpleImputer

num_imputer = SimpleImputer(strategy="median")

X_train[num_cols] = num_imputer.fit_transform(X_train[num_cols])
X_test[num_cols] = num_imputer.transform(X_test[num_cols])

## Handle categorical missing values using mode imputation
cat_imputer = SimpleImputer(strategy="most_frequent")

X_train[cat_cols] = cat_imputer.fit_transform(X_train[cat_cols])
X_test[cat_cols] = cat_imputer.transform(X_test[cat_cols])

## Encoding 
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

# Align columns
X_train, X_test = X_train.align(X_test, join="left", axis=1, fill_value=0)
# print(X_train.head())


# In[4]:


X_train = X_train.apply(pd.to_numeric, errors="coerce")
X_test = X_test.apply(pd.to_numeric, errors="coerce")
print(X_train.isnull().sum().sum())
X_train = X_train.fillna(0)
X_test = X_test.fillna(0)
X_train = X_train.astype(float)
X_test = X_test.astype(float)

X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

X_train, X_test = X_train.align(X_test, join="left", axis=1, fill_value=0)

# 🔥 ADD THIS
X_train = X_train.apply(pd.to_numeric, errors="coerce").fillna(0)
X_test = X_test.apply(pd.to_numeric, errors="coerce").fillna(0)



# In[5]:


bad_cols = X_train.select_dtypes(include="object").columns
print("Object columns:", bad_cols)

print(y_train.head())
print(y_train.dtypes)

y_train = y_train.replace({"Yes": 1, "No": 0})
y_test = y_test.replace({"Yes": 1, "No": 0})


# In[6]:


## Day-14
## Hour - 5
## Practical Visualization code 

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np

degrees = [1, 2]

for d in degrees:
    model = Pipeline([
        ("poly", PolynomialFeatures(degree=d)),
        ("linreg", LinearRegression())
    ])
    
    model.fit(X_train, y_train)
    
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    
    train_error = mean_squared_error(y_train, train_pred)
    test_error = mean_squared_error(y_test, test_pred)
    
    print(f"Degree {d}: Train Error={train_error}, Test Error={test_error}")


# In[7]:


## Trying logostic regression 

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("accuracy_score",accuracy_score(y_test, y_pred))

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Classification Report
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)

## Probability Predictions
y_prob = model.predict_proba(X_test)
print("Predicted Probabilities:\n", y_prob)

## Coefficient
print("Coefficients:\n", model.coef_)



# In[ ]:


## Compare train and test 
y_train_pred = model.predict(X_train)

# print("Train Accuracy:", accuracy_score(y_train, y_train_pred))
# print("Test Accuracy:", accuracy_score(y_test, y_pred))

## Accuracy and test accuracy is both low so there are chances of underfitting
## to fix this and low recall value we use prbability 
## Model generally use probability like 0.5


## option 1
## Theshold tuning

print("y_test_shape",y_test.shape)
print("y_pred_shape",y_pred.shape)
y_prob = model.predict_proba(X_test)[:,1]

y_pred = (y_prob>0.3).astype(int)

## Calculate recall again

from sklearn.metrics import recall_score

recall = recall_score(y_test, y_pred)
print("Recall:", recall)

## Calssification report

from sklearn.metrics import classification_report

print("class report","\n",classification_report(y_test, y_pred))




# In[18]:


## Experiment 
for t in [0.5, 0.4, 0.3, 0.2]:
    y_pred = (y_prob > t).astype(int)
    recall = recall_score(y_test, y_pred)
    print(f"Threshold {t} → Recall: {recall}")


# In[ ]:


## Option 2
## Class Weights
# Model
model = LogisticRegression(max_iter=1000,class_weight="balanced")
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("accuracy_score",accuracy_score(y_test, y_pred))

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Classification Report
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)

# ## Probability Predictions
# y_prob = model.predict_proba(X_test)
# print("Predicted Probabilities:\n", y_prob)

# ## Coefficient
# print("Coefficients:\n", model.coef_)


# In[ ]:


##  Hour 7
## Find the length of longest substring without repeating chars

s='abcabcbb'
## Output = 2 ('abc)

def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1

        seen[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len
print(lengthOfLongestSubstring(s))

