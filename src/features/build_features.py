# -*- coding: utf-8 -*-
import sys
import io
import os
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
import yaml

# Test if the required parameters are received
if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write(
        "\tpython3 src/prepare/prepare_dataset.py data-dir-path"
        " features-dir-path\n"
    )
    sys.exit(1)

with open("params.yaml") as file:
    params = yaml.load(file, Loader=yaml.SafeLoader)
    params = params["dataset"]

# Configure Paths and Folders
input_data_folder, output_data_folder = sys.argv[1:]

train_in_path = Path(f"{input_data_folder}/train.csv").resolve()
test_in_path = Path(f"{input_data_folder}/test.csv").resolve()

train_out_path = Path(f"{output_data_folder}/train.csv").resolve()
test_out_path = Path(f"{output_data_folder}/test.csv").resolve()

# If doesn't exist, create the output data folder
os.makedirs(output_data_folder, exist_ok=True)

# Load train and test datasets
train_in = pd.read_csv(train_in_path, index_col=[0])
test_in = pd.read_csv(test_in_path, index_col=[0])

x_train_in, y_train_in = (
    train_in.drop(params["target"], axis=1),
    train_in[[params["target"]]],
)
x_test_in = test_in

## ======  Create a Pipeline to transform the data =============
preprocessor = ColumnTransformer(
    "", verbose_feature_names_out=False, remainder="passthrough"
)
# ==============================================================

# Fit & Transform the train data
x_train_out = preprocessor.fit_transform(x_train_in)

# Transform the test data
x_test_out = preprocessor.transform(x_test_in)

## Export the output data
# The index should be reconstituted.
# The columns' names should be reconstituted. In this example,
# the features of input are the same as the output. When you
# build a pipeline, make sure to rebuild the names of the columns
# correctly
cols = preprocessor.get_feature_names_out()
train_in_index = train_in.index
test_in_index = test_in.index

x_train_out = pd.DataFrame(x_train_out, index=train_in_index, columns=cols)
x_test_out = pd.DataFrame(x_test_out, index=test_in_index, columns=cols)

# Create the output dataset
train_out = pd.concat([x_train_out, y_train_in], axis=1)
test_out = x_test_out

# Export as .csv
train_out.to_csv(train_out_path)
test_out.to_csv(test_out_path)
