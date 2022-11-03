import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm # we'll use this when running regressions
import seaborn as sns
sns.set()
# load the .csv file
data = pd.read_csv('1.01. Simple linear regression.csv')
# it will be automatically converted into a data frame
# print(data.describe())
# defining the dependent and independent variables
y = data['GPA']
x = data['SAT']
# observing data points
# print(plt.scatter(x,y),plt.xlabel('SAT',fontsize=20),plt.ylabel('GPA',fontsize=20),plt.show())
b0 = sm.add_constant(x)
results = sm.OLS(y,b0).fit()
#print(results.summary())
yhat = 0.0017*x+0.275
fig = plt.plot(x,yhat,lw=4,c='yellow',label="regression line")
# print(plt.scatter(x,y),fig,plt.xlabel('SAT',fontsize=20),plt.ylabel('GPA',fontsize=20),plt.show())
