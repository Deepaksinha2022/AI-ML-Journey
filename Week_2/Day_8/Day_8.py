#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Hour 1
## Block 1
import pandas as pd
df=pd.read_csv("house_price_cleaned_v2.csv")
df.head()
# df['Neighborhood'].unique()

# ## Block 2
# ## Label Encoding
# ## ordered 2>1>0

# from sklearn.preprocessing import LabelEncoder
# le=LabelEncoder()
# df['Neighborhood']=le.fit_transform(df['Neighborhood'])

# ## One Hot Encoder
# ## Creates new column
# from sklearn.preprocessing import OneHotEncoder
# ohe=OneHotEncoder()
# dummies = pd.get_dummies(df['Neighborhood'])

# # convert only dummy columns
# dummies = dummies.astype('int64')
# df = df.drop('Neighborhood', axis=1)
# df = pd.concat([df, dummies], axis=1)
# df.head()

# ## Block 3
# ## Normal encoding - no order
# ## Ordinal data - has some order, meaningfull ranking
# cat_cols = df.select_dtypes(include='object').columns
# cat_cols
# for col in cat_cols:
#     print("Column:", col)
#     print(df[col].unique())
#     print("-"*40)


# In[2]:


# ## Out of 37 col lets first decide which are ordinal and normal
# ## to find the ordinal cols - general concept - cols haveing 'Qual','Cond' or QC in their names
# [col for col in cat_cols if 'Qual' in col or 'Cond' in col or 'QC' in col]
# ## not ordinal - condition1,condition2,sale condition
# ## Ordinal but not in cat_cols - FireplaceQu, GarageFinish,PoolQC,Fence
ordinal_cols = ['ExterQual',
 'ExterCond',
 'BsmtQual',
 'BsmtCond',
 'HeatingQC',
 'KitchenQual',
 'GarageQual',
 'GarageCond',
 'GarageFinish',
 'FireplaceQu'
 ]
nominal_list=[]
for i in df.columns:
    if i not in ordinal_cols:
        nominal_list.append(i)
# print(nominal_list)
# print(len(nominal_list))
# print(len(ordinal_list))
# print(df.shape)
# print(set(ordinal_list).intersection(set(df.columns)))
print('FirePlaceQu'in df.columns)
remove_cols=['OverallQual','OverallCond',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
              ,16,17,18,19,20,21,22,23,24]
nominal_cols = [col for col in nominal_list if col not in remove_cols]
len(nominal_cols)

# print(len(ordinal_cols),len(nominal_cols))


# In[3]:


import pandas as pd
df=pd.read_csv("house_price_cleaned_v2.csv")
df.head()
miss = df.isnull().sum()
# print(miss.shape)
# print(miss[miss>0])
missing_per= (df.isnull().sum())/len(df)
# for i in missing_per:
#     print(i)
#     print()
# print(missing_per)
ordinal_cols = ['ExterQual',
 'ExterCond',
 'BsmtQual',
 'BsmtCond',
 'HeatingQC',
 'KitchenQual',
 'GarageQual',
 'GarageCond',
 'GarageFinish',
 'FireplaceQu']

## Befor mapping fill values
for col in ordinal_cols:
    df[col] = df[col].astype(str).str.strip()

## Fillna with None in ordinal_cols
df[ordinal_cols] = df[ordinal_cols].replace('nan', 'None')
df[ordinal_cols] = df[ordinal_cols].fillna('None')


## Appl Mapping
qual_map = {
    'None':0,
    'Po':1,
    'Fa':2,
    'TA':3,
    'Gd':4,
    'Ex':5
}

for col in ordinal_cols:
    df[col] = df[col].map(qual_map)

## Handle special cols
df['GarageFinish'] = df['GarageFinish'].astype(str).str.strip()
df['GarageFinish'] = df['GarageFinish'].replace('nan','None')

df['GarageFinish'] = df['GarageFinish'].map({
    'None':0,
    'Unf':1,
    'RFn':2,
    'Fin':3
})
df[ordinal_cols].isnull().sum()

print(df['GarageFinish'].unique())

df_original = pd.read_csv("house_price_cleaned_v2.csv")
df['GarageFinish'] = df_original['GarageFinish']
df['GarageFinish'] = df['GarageFinish'].astype(str).str.strip()
df['GarageFinish'] = df['GarageFinish'].replace('nan', 'None')
df['GarageFinish'] = df['GarageFinish'].fillna('None')
df['GarageFinish'] = df['GarageFinish'].map({
    'None':0,
    'Unf':1,
    'RFn':2,
    'Fin':3
})
df['GarageFinish'].isnull().sum()
df[ordinal_cols].isnull().sum()


# In[4]:


df[ordinal_cols]
df.head()
# for col in df.columns:
#     if df[col].nunique() > 50:
#         print(col, df[col].nunique())


nominal_cols = list(df.select_dtypes(include='object').columns)
nominal_cols = [
    col for col in nominal_cols if df[col].nunique() < 20
]
nominal_cols
df = pd.get_dummies(df, columns=nominal_cols, dtype=int)
df.shape
print(df.select_dtypes(include='object').columns)
print(df.isnull().sum().sum())      
# df = pd.get_dummies(df, columns=['Neighborhood'], dtype=int)  
df.shape  
df.head()


# In[5]:


## Hour 3
df.describe()


# In[6]:


## Hour 4
## Block 1
# Exclude target column
y=df['SalePrice']
X=df.drop('SalePrice',axis=1)
print(X.shape)
y.shape


# In[7]:


## How to identify column to scale
# for col in df.columns:
#     print(col,df[col].unique())
#     print("-"*40)

# # Select Binary column
# binary_cols = [col for col in X.columns if X[col].nunique()==2]
# binary_cols

# ## Select continous columns
# continous_cols = [col for col in X.columns if col not in binary_cols]
# continous_cols

# ## Block 2
# ## Only scale continous columns
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X[continous_cols] = scaler.fit_transform(X[continous_cols])
# X[continous_cols].mean().head()

# ## Check standard deviaiton
# X[continous_cols].std().head()



# In[8]:


X = df.drop('SalePrice', axis=1)
nominal_cols = list(X.select_dtypes(include='object').columns)

X = pd.get_dummies(X, columns=nominal_cols, dtype=int)


# In[9]:


X.select_dtypes(include='object').columns


# In[10]:


#df = df.drop('Id', axis=1)

binary_cols = [col for col in X.columns if X[col].nunique() == 2]
continuous_cols = [col for col in X.columns if col not in binary_cols]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X[continuous_cols] = scaler.fit_transform(X[continuous_cols])
X.head()


# In[11]:


## Check mean
X[continuous_cols].mean().head

X[continuous_cols].std().head

df_scaled=X.copy()
df_scaled["SalePrice"]=y

## Save Dataset
df_scaled.to_csv("house_price_scaled.csv",index=False)
df_scaled.head()


# In[12]:


## Hour 5
df_final=pd.read_csv("house_price_scaled.csv")
df_final.select_dtypes(include='object').columns
df_final.to_csv("house_price_v3_ml_ready.csv")


# In[13]:


## Hour 7
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['GrLivArea'], kde=True)
plt.title("Before Scaling")
plt.show()


# In[14]:


sns.histplot(X['GrLivArea'], kde=True)
plt.title("After Scaling")
plt.show()


# In[15]:


## Block 2
## Boxplot review
sns.boxplot(x=df['GrLivArea'])
plt.title("Before Scaling")
plt.show()


# In[16]:


sns.boxplot(x=X['GrLivArea'])
plt.title("After Scaling")
plt.show()


# In[17]:


## Block 3
cols = ['LotArea','GrLivArea','TotalBsmtSF']

X[cols].hist(bins=30, figsize=(10,6))
plt.show()


# In[18]:


## Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df_final.corr(), cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


# In[19]:


X.describe().T.head()


# In[20]:


## Hour 7
## Find the longest common prefix
Output="fl"
strs = ["flower","flow","flight"]
prefix = strs[0]
for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]
print(prefix)


# In[21]:


## Hour 8

df_final.head()


# In[22]:


x=df_final.drop('SalePrice',axis=1)
y=df_final['SalePrice']



# In[23]:


x.select_dtypes(include='object').columns
x.shape


# In[24]:


## Final Sanity Check
print("Shape:", df_final.shape)
print("Missing:", df_final.isnull().sum().sum())
print("Object cols:", len(df_final.select_dtypes(include='object').columns))

