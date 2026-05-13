#!/usr/bin/env python
# coding: utf-8

# In[8]:


import zipfile

with zipfile.ZipFile("credit_card_fraud.csv", "r") as zip_ref:
    zip_ref.extractall("fraud_data")

# Check extracted file

import os

print(os.listdir("fraud_data"))


# In[4]:


import pandas as pd
df = pd.read_csv("creditcard.csv")
df.head()

# Scale time and amount
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# Scaling 

from sklearn.preprocessing import StandardScaler

amount_scaler = StandardScaler()
time_scaler = StandardScaler()

X_train["Amount"] = amount_scaler.fit_transform(
    X_train[["Amount"]]
)

X_train["Time"] = time_scaler.fit_transform(
    X_train[["Time"]]
)

# transform test data only

X_test["Amount"] = amount_scaler.transform(
    X_test[["Amount"]]
)

X_test["Time"] = time_scaler.transform(
    X_test[["Time"]]
)

# Apply Logistics Regression

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(class_weight="balanced")

model.fit(X_train,y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

# Classification report

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# Confusion Matrix
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

from sklearn.metrics import roc_auc_score

print(roc_auc_score(y_test, y_prob))

# thrshold tuning

y_prob = model.predict_proba(X_test)[:,1]

y_pred_new = (y_prob > 0.8).astype(int)

# again checking confusion matrix and classification report

print(classification_report(y_test, y_pred_new))
print(confusion_matrix(y_test, y_pred_new))


# In[ ]:


# trying Random forest
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

rf_prob = rf_model.predict_proba(X_test)[:,1]

print(classification_report(y_test, rf_pred))

print(confusion_matrix(y_test, rf_pred))

print(roc_auc_score(y_test, rf_prob))

# threshold tuning again 

rf_prob = rf_model.predict_proba(X_test)[:,1]

rf_pred_new = (rf_prob > 0.3).astype(int)

print(classification_report(y_test, rf_pred_new))

print(confusion_matrix(y_test, rf_pred_new))


# In[ ]:


# Choosing Threshold Scientifically

rf_prob = rf_model.predict_proba(X_test)[:,1]

from sklearn.metrics import precision_recall_curve

precision, recall, thresholds = precision_recall_curve(
    y_test,
    rf_prob
)

# Plot curve

import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

plt.plot(recall, precision)

plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")

plt.show()


# In[ ]:


# Find usefull thresholds

for p, r, t in zip(precision, recall, thresholds):
    if p > 0.90 and r > 0.80:
        print(t, p, r)


# In[12]:


# Random Forest Feature Importance

import pandas as pd
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

importance.sort_values(
    by="Importance",
    ascending=False,
    inplace=True
)
print(importance.head(10))


# In[13]:


get_ipython().system(' pip install xgboost')


# In[15]:


# Trying XGBoost

from xgboost import XGBClassifier

xgb_model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    scale_pos_weight=len(y_train[y_train==0]) / len(y_train[y_train==1]),
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_pred = xgb_model.predict(X_test)

xgb_prob = xgb_model.predict_proba(X_test)[:,1]

print(classification_report(y_test, xgb_pred))

print(confusion_matrix(y_test, xgb_pred))

print(roc_auc_score(y_test, xgb_prob))

# Tune Threshold
xgb_prob = xgb_model.predict_proba(X_test)[:,1]

for t in [0.3,0.4,0.5,0.6,0.7]:
    pred = (xgb_prob > t).astype(int)

    print(t)
    print(classification_report(y_test, pred))


# In[17]:


# Hyperparameter tuning

params = {
    "max_depth": [3,4],
    "learning_rate": [0.05,0.1],
    "n_estimators": [100,200]
}

from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

grid = GridSearchCV(
    XGBClassifier(
        scale_pos_weight=len(y_train[y_train==0]) / len(y_train[y_train==1]),
        random_state=42
    ),
    params,
    cv=3,
    scoring="roc_auc",
    n_jobs=-1
)

grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)

