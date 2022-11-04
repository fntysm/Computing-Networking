from datetime import date
myDate = date(2022,11,4)
bDate = date(2004, 9,22)
# print(type(myDate))
# print(f'month: {myDate.month}, year: {myDate.year}, weekday: {myDate.weekday()}, day: {myDate.weekday()}')
delta = myDate-bDate
print(myDate + delta)