import pandas as pd

data = pd.read_csv('Lending-company.csv', index_col='LoanID')
lendingCoData = data.copy()
# print(lendingCoData.head())
# print(lendingCoData['StartDate'].head())
# to see the datatypes of different columns
# print(lendingCoData.info())
