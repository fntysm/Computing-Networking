import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm # we'll use this when running regressions

# load the .csv file
data = pd.read_csv('1.01. Simple linear regression.csv')
# it will be automatically converted into a data frame