#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
# import numpy as np
 
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
 
from sklearn.svm import SVC, NuSVC
from sklearn.pipeline import make_pipeline
 
    
class ROIsFeatureExtractor(BaseEstimator, TransformerMixin):
    """Select only the 284 ROIs features:"""
 
    def fit(self, X, y):
        return self
 
    def transform(self, X):
        return X[:, :284]
 
 
def get_estimator():
    """Build your estimator here."""
    estimator = make_pipeline(
      ROIsFeatureExtractor(),
      StandardScaler(),
      VotingClassifier(estimators=[
          ('logreg', LogisticRegression(max_iter=1000, penalty='elasticnet', solver='saga', l1_ratio=0.8, C=0.1)),  
          ('nu_svc', NuSVC(kernel = 'rbf', class_weight="balanced", nu=0.6, gamma=0.00005, probability=True)), 
          ('svm', SVC(class_weight = 'balanced', kernel = 'poly', gamma='scale', C=8, probability=True))
      ], voting='soft')
  )
    return estimator
