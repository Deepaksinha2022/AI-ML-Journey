#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Ensemble Learning
# Definition

# Combining multiple ML models to produce stronger final prediction.

# Core Idea

# Many imperfect learners together can outperform one unstable learner.

# Key Requirement
# Diversity among models

# If all models make same mistakes:
# → ensemble weakens.

# 2. Why Decision Trees Need Ensemble
# Decision Trees
# Low bias
# High variance
# Highly unstable
# Sensitive to small data changes
# Overfit easily

# Small data change:
# → completely different tree structure.

# 3. Bagging (Bootstrap Aggregation)
# Full Form
# Bootstrap + Aggregation
# Bootstrap

# Random sampling WITH replacement.

# Effects:

# repeated rows
# missing rows
# different datasets for different trees

# Creates:

# row diversity
# Aggregation

# Combine predictions.

# Classification

# Majority Voting

# Regression

# Averaging

# 4. Bootstrap Sampling
# Important Result

# Probability a row is NOT selected after n draws:

# (1−n)n 1

# n
# ≈0.368

# Meaning:

# ~36.8% rows absent
# ~63.2% rows appear at least once
# OOB (Out-of-Bag) Samples

# Rows not seen by particular tree.

# Used as:

# hidden validation/test data

# 5. Variance Reduction
# Variance Meaning

# Sensitivity to small data changes.

# High variance:

# unstable predictions
# overfitting
# Random Forest Main Goal
# Reduce variance
# Why Averaging Works

# Different trees:

# overfit differently
# make different mistakes

# Averaging:
# smooths fluctuations
# stabilizes prediction

# 6. Random Feature Selection
# Problem With Only Bagging
# Dominant features can make trees similar.
# Example:

# Salary
# chosen repeatedly as root split.

# This creates:
# correlated trees
# RF Solution
# At every split:
# only random subset of features visible
# Creates:
# feature diversity
# decorrelated trees
# Common Default

# For classification:

# p
# 	​


# Where:

# p = total features
# 7. Random Forest Workflow
# Step 1

# Create bootstrap sample.

# Step 2

# Train deep decision tree.

# Step 3

# At every split:

# choose random subset of features
# Step 4

# Repeat for many trees.

# Step 5

# Aggregate predictions:

# voting
# OR
# averaging

# 8. Bias–Variance Behavior
# Decision Trees
# Property	Value
# Bias	Low
# Variance	High
# Random Forest
# Property	Effect
# Bias	stays low mostly
# Variance	reduces strongly
# Core RF Success
# Low Bias + Lower Variance
# 9. Why Random Forest Works

# Random Forest combines:

# Mechanism	Purpose
# Deep Trees	Low bias
# Bootstrap Sampling	Row diversity
# Feature Randomness	Decorrelation
# Averaging	Variance reduction
# 10. Correlation Is Dangerous

# If trees become highly similar:

# same mistakes repeat
# averaging weakens

# Thus:

# decorrelation is critical
# 11. Important Tradeoff
# More Randomness

# ✅ More diversity
# ✅ Lower correlation

# BUT
# ❌ Weaker trees
# ❌ Slightly higher bias

# Random Forest balances:

# strength vs diversity
# 12. Important Hyperparameters
# n_estimators

# Number of trees.

# More trees:

# lower variance
# more stability
# max_features

# Features visible per split.

# Small value:

# more randomness
# more diversity

# Too small:

# weak trees
# higher bias
# max_depth

# Controls tree depth.

# Deep trees:

# low bias
# high variance

# RF safely uses deep trees because averaging stabilizes them.

# 13. RF Advantages

# ✅ Strong generalization
# ✅ Handles nonlinear patterns
# ✅ Robust to noise
# ✅ Less overfitting than single trees
# ✅ Little preprocessing needed
# ✅ Works well out-of-box

# 14. RF Limitations

# ❌ Less interpretable
# ❌ Large forests slower
# ❌ Can still overfit noisy data
# ❌ Too much randomness weakens trees

# 15. Most Important Concepts To Remember
# Ensemble learning needs:
# Diverse learners
# RF mainly reduces:
# Variance
# Randomness is intentionally injected:
# bootstrap sampling
# feature randomness
# Averaging stabilizes:
# unstable deep trees
# RF success depends on:
# Strong Trees + Low Correlation
# 16. One-Line Summary
# Random Forest = Deep diverse trees trained on randomized data/features whose averaged predictions reduce variance and improve generalization.

