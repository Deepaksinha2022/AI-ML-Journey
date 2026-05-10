#!/usr/bin/env python
# coding: utf-8

# In[14]:


## Bayes combines how common something is (belief) and what are the evidence for this
# a very rare disease belief or prior is low but strong evidence can increase probability
# We know:
# P(Data | Class)

# We want:
# P(Class | Data)

# We know:
# How likely data is for each class

# We want:
# How likely class is given data

# Complex joint probability
#         ↓
# Assume independence
#         ↓
# Multiply individual probabilities

# if we go for combined probability it would be computationaly expensive and will require large amount of data
# Naive Bayes assumes that feature are conditionally independent given the class which simplies joint probability into a product of individual probability

# Naive bayes still work even if the assumption is wrong beacuse we need relative comparison


# In[15]:


# gausian used for continous numbers beacuse it uses features with continous numbers - assumes data follow normal (bell curve) distribution

# multinomial NB- use frequency of feature 

# Gaussian NB estimates mean and variance for each feature per class, while Multinomial NB estimates word probabilities from counts.


# In[16]:


# Apply naive bayes
docs = [
    "win money now",
    "free money win",
    "hello friend",
    "let's meet tomorrow"
]

labels = ["spam", "spam", "not_spam", "not_spam"]

# build vocab
from collections import defaultdict

vocab = set()
for doc in docs:
    for word in doc.split():
        vocab.add(word)

# count per class
word_counts = {
    "spam": defaultdict(int),
    "not_spam": defaultdict(int)
}

class_counts = {"spam": 0, "not_spam": 0}

for doc, label in zip(docs, labels):
    class_counts[label] += 1
    for word in doc.split():
        word_counts[label][word] += 1

# compute probability
total_words = {
    "spam": sum(word_counts["spam"].values()),
    "not_spam": sum(word_counts["not_spam"].values())
}


# prediction function

import math

def predict(doc):
    scores = {}
    
    for cls in ["spam", "not_spam"]:
        # prior
        score = math.log(class_counts[cls] / len(docs))
        
        for word in doc.split():
            word_freq = word_counts[cls][word] + 1  # Laplace smoothing
            total = total_words[cls] + len(vocab)
            
            score += math.log(word_freq / total)
        
        scores[cls] = score
    
    return max(scores, key=scores.get)

# test

print(predict("win money"))


# In[17]:


# Using Sklearn

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)

model = MultinomialNB()
model.fit(X, labels)

test = vectorizer.transform(["win money"])
print(model.predict(test))


# In[18]:


# Log:
# - prevents underflow
# - keeps ranking same

# Smoothing:
# - prevents zero
# - keeps model alive


# In[19]:


# Mini task
docs = [
    "win money now",
    "free money win",
    "hello friend",
    "let's meet tomorrow"
]

labels = ["spam", "spam", "not_spam", "not_spam"]

print(predict("free money"))
print(predict("hello win"))
print(predict("lottery"))


# In[ ]:


docs = [
    "win money now",
    "free money win",
    "hello friend",
    "let's meet tomorrow"
]

labels = ["spam", "spam", "not_spam", "not_spam"]

# getting total words in data--- docs

vocab = set()

for sentence in docs:
    for word in sentence.split():
        vocab.add(word)

# getting word count and class count
from collections import defaultdict
word_count = {"spam": defaultdict(int),"not_spam": defaultdict(int)}
class_count = {"spam":0,"not_spam":0}

for doc, label in zip(docs, labels):
    class_count[label] += 1
    for word in doc.split():
        word_count[label][word] += 1

total_words = {
    "spam": sum(word_count["spam"].values()),
    "not_spam": sum(word_count["not_spam"].values())
}

def predict(doc):
    scores = {}

    for cls in ["spam","not_spam"]:
        score = math.log(class_count[cls]/len(docs))

        for word in doc.split():
            word_freq = word_count[cls][word] +1
            total = total_words[cls] + len(vocab) 

            score += math.log(word_freq / total)
        
        scores[cls] = score
    
    return max(scores, key=scores.get)


# In[14]:


# DSA

# Longest substring with at most k different characters

def longest_k_distinct(s, k):
    left = 0
    freq = {}
    max_len = 0
    
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

print(longest_k_distinct('eebce',2))

