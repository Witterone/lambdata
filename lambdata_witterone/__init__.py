#!/usr/bin/env python
'''
lambdata - a collection of Data Science helper functions
'''

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import category_encoders as ce

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import test_train_split

from sklearn.pipeline import make_pipeline

from . import example_module

TEST = pd.DataFrame(np.ones(10))

Y = example_module.increment(example_module.x)
