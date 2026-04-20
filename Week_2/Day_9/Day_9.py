#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Day 9
## Hour 1
## Block 1
import pandas as pd
df = pd.read_csv('House_price_train.csv')
df.head()


# In[3]:


## Block 1
df.groupby('Neighborhood')['SalePrice'].mean()
df.columns


# In[6]:


## Block 2
## Multiindex - grouping within group
## Group with multiple columns
df.groupby(['Neighborhood','HouseStyle'])['SalePrice'].mean()


# In[15]:


df.groupby(['Neighborhood','HouseStyle'])['SalePrice'].mean().loc['NAmes']


# In[24]:


## Hour 2
## Block 1
## Basic Multiple Aggregation
df.groupby('Neighborhood')['SalePrice'].agg(['mean','max','min'])

## Diff aggregations for different columns
df.groupby('Neighborhood').agg({'SalePrice':['mean','max'],'GrLivArea':['mean','sum']})

## Named Aggregations
df.groupby('Neighborhood').agg(avg_price = ('SalePrice','mean'),
                               max_price=('SalePrice','max'),
                               avg_area = ('GrLivArea','mean'))

## Sort Results
df.groupby('Neighborhood')['SalePrice'].mean().sort_values(ascending=False)

df.groupby('Neighborhood').size()
df.groupby('Neighborhood').agg(
    avg_price=('SalePrice','mean'),
    count=('SalePrice','count')
)


# In[37]:


## Block 2
## Transform

df['Neighborhood_Avg_Price'] = df.groupby('Neighborhood')['SalePrice'].transform('mean')
df['price_diff'] = df['SalePrice'] - df.groupby('Neighborhood')['SalePrice'].transform('mean')
df['price_diff']
df['area_rank'] = df.groupby('Neighborhood')['GrLivArea'].transform('rank')
df['avg_area'] = df.groupby('Neighborhood')['GrLivArea'].transform('mean')
df.head(20)


# In[46]:


## Hour 3
## Block 1
df1 = df[['Neighborhood','SalePrice']]
df2 = df.groupby('Neighborhood')['SalePrice'].mean().reset_index()
df2.rename(columns={'SalePrice':'AvgPrice'},inplace=True)
merged = pd.merge(df1,df2,on='Neighborhood',how='left')
print("left",merged.head(),merged.shape)
merged = pd.merge(df1,df2,on='Neighborhood',how='right')
print('right',merged.head(),merged.shape)
merged = pd.merge(df1,df2,on='Neighborhood',how='inner')
print('inner',merged.head(),merged.shape)
merged = pd.merge(df1, df2, on='Neighborhood', how='outer')
print('outer',merged.head(),merged.shape)
print(df1.shape)
print(df2.shape)


# In[ ]:


## Block 2
## Merge vs Join vs Concat
## Axis = 0 -- increases row, Axis =1 ----increases coloumns
## Join is used to attach using index


# In[ ]:


## Hour 4
## Feature Transformation


# In[52]:


## Block 3
## Binning
df['price_category'] = pd.cut(
    df['SalePrice'],
    bins=[0,150000,300000,1000000],
    labels=['Low','Medium','High']
)
## Area Binning
df['area_category'] = pd.cut(df['GrLivArea'],bins=3, labels=['small','medium','large'])

## Quantile Binning
df['price_quantile']=pd.qcut(df['SalePrice'],q=4,labels=['Q1','Q2','Q3','Q4'])

df['area_bin'] = pd.qcut(df['GrLivArea'], q=4)
df['area_bin'].value_counts()


# In[57]:


## Hour 5 
## Mini Project
## feature Segmentation

df['price_segment'] = pd.qcut(df['SalePrice'],q=3,labels=['Low','Medium','High'])
df['area_segment'] = pd.qcut(df['GrLivArea'],q=3,labels=['Small','Medium','Large'])
df['quality_segment'] = pd.cut(df['OverallQual'],bins=[0,4,7,10],labels=['Low','Medium','Large'])


## Block 2
## Average price per segment
df.groupby('price_segment')['SalePrice'].mean()

## Area vs price
df.groupby(['area_segment','price_segment'])['SalePrice'].mean()

## Quality Vs Price
df.groupby('quality_segment')['SalePrice'].mean()

## Block 4
## Combine Segments
df.groupby(['area_segment','quality_segment'])['SalePrice'].mean()


# In[58]:


df['price_segment'].value_counts()


# In[61]:


df['premium_flag'] = (df['SalePrice'] > df['Neighborhood_Avg_Price']).astype(int)

df.to_csv("house_price_v4_features.csv", index=False)
df2= pd.read_csv("house_price_v4_features.csv")
df2.head()


# In[63]:


import pandas as pd

# Load cleaned dataset (v2)
df = pd.read_csv("house_price_cleaned_v2.csv")

# --- Feature Engineering ---

# Neighborhood average price
df['Neighborhood_Avg_Price'] = df.groupby('Neighborhood')['SalePrice'].transform('mean')

# Price difference from neighborhood average
df['price_diff'] = df['SalePrice'] - df['Neighborhood_Avg_Price']

# Area rank within neighborhood
df['area_rank'] = df.groupby('Neighborhood')['GrLivArea'].transform('rank')

# Average area per neighborhood
df['avg_area'] = df.groupby('Neighborhood')['GrLivArea'].transform('mean')

# Price per sqft
df['price_per_sqft'] = df['SalePrice'] / df['GrLivArea']

# Total square footage
df['TotalSF'] = df['TotalBsmtSF'] + df['GrLivArea']

# Overall score
df['overall_score'] = df['OverallQual'] * df['GrLivArea']

# Premium flag
df['premium_flag'] = (df['SalePrice'] > df['Neighborhood_Avg_Price']).astype(int)

# --- Segmentation ---

# Price segments
df['price_segment'] = pd.qcut(df['SalePrice'], q=3, labels=['Low','Medium','High'])

# Area segments
df['area_segment'] = pd.qcut(df['GrLivArea'], q=3, labels=['Small','Medium','Large'])

# Quality segments
df['quality_segment'] = pd.cut(df['OverallQual'], bins=[0,4,7,10], labels=['Low','Medium','High'])

# --- Save v4 dataset ---
df.to_csv("house_price_v4_features.csv", index=False)


# In[68]:


## Hour 6
## Correlation Heatmap
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('house_price_v4_features.csv')
numeric_df = df.select_dtypes(include='number')
plt.figure(figsize=(12,8))
sns.heatmap(numeric_df.corr(),cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


# In[70]:


corr = numeric_df.corr()['SalePrice'].sort_values(ascending=False)
print(corr.head(10))


# In[ ]:


## Violin Plot
sns.violinplot(x='quality_segment', y='SalePrice', data=df)
plt.title("Price Distribution by Quality")
plt.show()


# In[72]:


# Block 4 — Area vs Price
sns.violinplot(x='area_segment', y='SalePrice', data=df)
plt.title("Price vs Area Segment")
plt.show()


# In[73]:


sns.boxplot(x='price_segment', y='SalePrice', data=df)
plt.show()


# In[74]:


sns.boxplot(x='quality_segment', y='price_per_sqft', data=df)
plt.show()


# In[76]:


## Hour 7
## Pallindrome
import re

s = "A man, a plan, a canal: Panama"
s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
print(s == s[::-1])


# In[ ]:


## Block 2
## Length of last word
s="hello word"
# count=0
# for i in s[::-1]:
#     if i==' ':
#         break
#     else:
#         count+=1
# print(count)
# print(s[::-1])

# print(len(s.strip().split()[-1]))

## Block 3
## find first non-repeating character index
j=0
for i in s.strip():
    if i not in s[j+1:len(s)]:
        print(i)
        break
    j+=1

## Other Solutions
from collections import Counter
count = Counter(s)
for i in count:
    if count[i]==1:
        print(i)
        break


# In[96]:


## Hour 8
df=pd.read_csv('house_price_v4_features.csv')
df.head()
df.isnull().sum().sum()
df.dtypes
df.describe().T


# In[100]:


cols = [
    'price_per_sqft',
    'Neighborhood_Avg_Price',
    'price_diff',
    'area_rank',
    'premium_flag'
]

df[cols].head()

df['price_segment'].value_counts()
df['area_segment'].value_counts()
# df['quality_segment'].value_counts()

df.to_csv('house_price_v4_final.csv')

