import numpy as np
import pandas as pd

# Define transformers
def count_features(X, offset=0):
    X = X.apply(lambda x: x.sum(), axis=1) + offset
    return np.array(X).reshape(-1, 1)


def discretize_feature(X, quantiles=4, labels=None):
    flattened_X = X.values.flatten()
    if labels is None:
        labels = np.arange(quantiles)
    X = pd.qcut(flattened_X, q=quantiles, labels=labels)
    return np.array(X).reshape(-1, 1)


def boolean_feature(X):
    X = X.apply(lambda x: x.sum() == 0, axis=1).astype(int)
    return np.array(X).reshape(-1, 1)


def extract_titles(X):
    X = X.apply(lambda x: x.str.extract(" ([A-Za-z]+)\.", expand=False))
    return np.array(X).reshape(-1, 1)
