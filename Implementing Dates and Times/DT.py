import pandas as pd
from datetime import date, datetime
data = pd.read_csv('Lending-company.csv', index_col='LoanID')
lendingCoData = data.copy()
print(lendingCoData.head())
print(lendingCoData['StartDate'].head())
# to see the datatypes of different columns
# print(lendingCoData.info())
mydateTime = datetime(year=2022, month=11, day=5, hour=17, minute=57)
# print(mydateTime)
mydateTime = mydateTime.replace(hour=18)
# print(mydateTime)
# converting datetime objects into strings
# print(mydateTime.strftime("the year is %Y, and it was awful"))
# converting strings into datetime objects
strDateTime = "18:08:36 2022-11-05"
# print(datetime.strptime(strDateTime, "%H:%M:%S %Y-%m-%d"))
# converting Data into datetime objects
# print(pd.to_datetime(strDateTime))
lendingCoData['StartDate'] = pd.to_datetime(lendingCoData['StartDate'])
print(lendingCoData.head())