import pytz
from datetime import datetime
import pandas as pd
# converting between timezones
mydateTime = datetime(year=2022, month=11, day=5, hour=17, minute=57, tzinfo=pytz.UTC)
tzTime = mydateTime.astimezone(pytz.timezone('US/Central'))
# print(tzTime)
# print(pytz.all_timezones)
tzUSpd = pd.to_datetime(tzTime)
tzUTC = tzUSpd.tz_convert('UTC')
print(tzUTC)