import numpy as np
import pandas as pd


def identify_deck(X, fill_missing="UNK"):
    X = X.apply(
        lambda s: s[0] if s.str.contains("^[A-Za-z]").any() else fill_missing,
        axis=1,
    )
    return np.array(X).reshape(-1, 1)


def fill_by_group(X, group_by, fill_by="median"):
    X["Age"] = X["Age"].fillna(X.groupby(group_by)["Age"].transform(fill_by))
    return np.array(X["Age"]).reshape(-1, 1)


def count_features(X, offset=0):
    X = X.apply(lambda x: x.sum(), axis=1) + offset
    return np.array(X).reshape(-1, 1)


def discretize_feature(X, bins=[0, 1], labels=None):
    if isinstance(X, np.ndarray):
        X = pd.DataFrame(X)
    X = X.apply(
        lambda x: pd.cut(x, bins=bins, include_lowest=True, labels=labels)
    )
    return np.array(X).reshape(-1, 1)


def boolean_feature(X):
    X = X.apply(lambda x: x.sum() == 0, axis=1).astype(int)
    return np.array(X).reshape(-1, 1)


def extract_titles(X):
    X = X.apply(lambda x: x.str.extract(" ([A-Za-z]+)\.", expand=False))
    return np.array(X).reshape(-1, 1)
