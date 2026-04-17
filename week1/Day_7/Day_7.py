# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: ai_mastery
#     language: python
#     name: python3
# ---

# %%
## Day 7
## Block 1
import pandas as pd
df=pd.read_csv("House_price_train.csv")
df.head()
# df.shape
# df.info()
# missing = df.isnull().sum().sort_values(ascending=False)
# # print(missing)
# miss = missing[missing>0]
# miss
# df['PoolQC'].value_counts()

## Missing percentage
missing_percent = (df.isnull().sum())/len(df)
missing_percent = missing_percent[missing_percent>0].sort_values(ascending=False)
# print(missing_percent*100)

## Block 3
## Visualisation missing

# import seaborn as sns
# import matplotlib.pyplot as plt
# plt.figure(figsize=(12,6))
# sns.heatmap(df.isnull(),cbar=False)
# plt.show()

## Block 4
# decide drop vs keep

# Rule 1 = drop very high missing>80%
col_to_drop = missing_percent[missing_percent>0.80].index
# print(col_to_drop)
df.drop(columns=col_to_drop,inplace=True)
df.head()

# Block 5

## First cleaning step
## Fill Categorical Missing
cat_cols = df.select_dtypes(include='object').columns
df[cat_cols] = df[cat_cols].fillna('None')

# Fill Numeric
num_cols= df.select_dtypes(include=['int64','float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

df.isnull().sum()

# %%
## Hour 2

## Outlier Detection
df["SalePrice"].describe()

#Block 2
# Boxplot
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x=df["SalePrice"])
plt.show()


# %%
# Boxplot for GrLivArea
sns.boxplot(x=df['GrLivArea'])
plt.show()

# %%
# Boxplot for LotArea
sns.boxplot(x=df['LotArea'])
plt.show()

# %%
## Block 3

## IQR Method
Q1 = df["SalePrice"].quantile(0.25)
Q3 = df["SalePrice"].quantile(0.75)
IQR = Q3-Q1
lower = Q1-1.5*IQR
upper = Q3+1.5*IQR

# # Detect Outlier on SalePrice
# outliers_sale_price = df[(df["SalePrice"]<lower) | (df["SalePrice"]>upper)]
# outliers_sale_price.shape

## detect outlier on GrLivArea
# Q1 = df["GrLivArea"].quantile(0.25)
# Q3 = df["GrLivArea"].quantile(0.75)
# IQR = Q3-Q1
# lower = Q1-1.5*IQR
# upper = Q3+1.5*IQR
# outlier_GrLivArea = df[(df["GrLivArea"]<lower) | (df["GrLivArea"]>upper)]
# outlier_GrLivArea.shape

## Block 4
## Scatter Plot
# plt.scatter(df['GrLivArea'], df['SalePrice'])
# plt.xlabel('GrLivArea')
# plt.ylabel('SalePrice')
# plt.show()


## Block 5
## Remove Outlier based on a number - that must be jugded carefully
df = df[df["GrLivArea"]<4000]
## Removing Outlier using IQR
df = df[(df["SalePrice"]>=lower) & (df["SalePrice"]<=upper)]

# %%
## Hour 3
## Block 3
df['LotFrontage'] = df.groupby('Neighborhood')['LotFrontage'].transform(
    lambda x: x.fillna(x.median()))
## Zero Filling
df["MasVnrArea"].fillna(0,inplace= True)

## Mode for Categorical
df['Electrical'].fillna(df['Electrical'].mode()[0], inplace=True)

## Domain-based fill
df['GarageYrBlt'].fillna(0, inplace=True)

# %%
## Block 4

## Categorical Columns 

cols = ['GarageType', 'GarageFinish', 'GarageQual']
df[cols] = df[cols].fillna('None')
## Block 5
df.isnull().sum().sort_values(ascending=False)

# %%
## Hour 4
## Block 1

## Boolean Indexing
df[(df["SalePrice"]>200000) & (df['GrLivArea']>1500)]
df[(df['SalePrice']>300000) & (df["GrLivArea"]>2000)]

## Block 2

df.loc[0:4,["SalePrice","GrLivArea"]]
df.iloc[0:5,0:3]
## First 10 rows
df.iloc[:10,:]
df[["SalePrice","Neighborhood"]]
df.head()

## Block 3
df.loc[df['SalePrice'] > 300000, ['SalePrice', 'Neighborhood']]

df.loc[df["SalePrice"] >300000,"Luxury"] = 1
df[["SalePrice","Luxury"]]

## Create new column if Luxury = 1 if price>300k else 0
df["Luxury"]=0
df.loc[df["SalePrice"]>300000, "Luxury"]=1
df["Luxury"] = df["SalePrice"].apply(lambda x: 1 if x>300000 else 0) 

## Block 4
## isin() - Multi-Value Filtering
df[df["Neighborhood"].isin(['NAmes',"CollgCr"])]

## Block 5 - Query Method

df.query("SalePrice>300000 and GrLivArea>2000")
df.query("SalePrice>329000") 

## Block 5 - Assignand Apply 
df["price_per_sqft"] = df['SalePrice']/df['GrLivArea']
df.head()

## Apply Function
df['HighPrice'] = df['SalePrice'].apply(lambda x: 1 if x>200000 else 0)
df.head()

# %%
## Hour 5

## block 1
## Q1 - Average House Price
df['SalePrice'].mean()
df['SalePrice'].max()
df['SalePrice'].min()

## Block 2
df.groupby('Neighborhood')['SalePrice'].mean().sort_values(ascending=False)

## Block 3
df[['GrLivArea','SalePrice']].corr()

# %%
import matplotlib.pyplot as plt

plt.scatter(df['GrLivArea'], df['SalePrice'])
plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
plt.show()

df['Luxury'].value_counts()
df.groupby('Luxury')['SalePrice'].mean()
df.groupby('Luxury').count()

# %%
## Block 5
df.corr(numeric_only=True)['SalePrice'].sort_values(ascending=False)

# %%
## Hour 6
## Block 1
## Distribution of SalePrice
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(df['SalePrice'], bins=30, kde=True)
plt.title("Distribution of SalePrice")
plt.show()

# %%
## Block 2
## Outlier Visualisation

## SalePrice
sns.boxplot(x=df['SalePrice'])
plt.title("SalePrice Boxplot")
plt.show()

## GrLivArea
sns.boxplot(x=df['GrLivArea'])
plt.show()

# %%
## Block 3
plt.figure(figsize=(12,6))
sns.boxplot(x='Neighborhood', y='SalePrice', data=df)
plt.xticks(rotation=45)
plt.show()

# %%
## Block 4
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm')
plt.show()

# %%
## Block 5
## Scatter plot

plt.scatter(df['GrLivArea'], df['SalePrice'])
plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
plt.show()
df.head()

# %%
## Block 6
sns.histplot(df['price_per_sqft'], bins=30, kde=True)
plt.show()

# %%
## Hour 7
## Block 1
## Check anagram
s1='listen'
s2='silent'
from collections import Counter
def anagram(s1,s2):
    return Counter(s1)==Counter(s2)
print(anagram(s1,s2))

# %%
## Hour 8

df=pd.read_csv('House_price_train.csv')
df.shape

## Cols to drop
missing_percent=(df.isnull().sum()/len(df))
col_to_drop=missing_percent[missing_percent>0.8].index
df.drop(columns=col_to_drop,inplace=True)
df.shape

## HAndle missing value
cat_cols = ['Alley', 'Fence', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
            'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2']

for col in cat_cols:
    if col in df.columns:
        df[col].fillna('None', inplace=True)

## Numerical (Domain-Based)
df['MasVnrArea'].fillna(0, inplace=True)
df['GarageYrBlt'].fillna(0, inplace=True)

# Group Based
df['LotFrontage'] = df.groupby('Neighborhood')['LotFrontage'].transform(
    lambda x: x.fillna(x.median())
)

## Remainig numerical
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

df[num_cols] = df[num_cols].fillna(df[num_cols].median())

## Remianing Categorical
cat_cols = df.select_dtypes(include='object').columns
df[cat_cols]=df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

## Outlier handling
df = df[df['GrLivArea'] < 4000]

## Feature engineering
df['Luxury'] = (df['SalePrice'] > 300000).astype(int)

df['Price_per_sqft'] = df['SalePrice'] / df['GrLivArea']

## FInal checks

df.isnull().sum().sum()
df.shape
df.describe()

# %%
df.to_csv("house_price_cleaned_v2.csv", index=False)
