import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm # we'll use this when running regressions
import seaborn as sns
sns.set()
# load the data
data = pd.read_csv('1.02. Multiple linear regression.csv')
# GPA = b0 + b1*SAT + b2*Rand
y = data['GPA']
x = data[['SAT','Rand 1,2,3']]