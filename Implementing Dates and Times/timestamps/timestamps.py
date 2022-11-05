from datetime import datetime
import pandas as pd
import numpy as np
myTimeStamp = 154782356.2541
# to datetime
# print(datetime.fromtimestamp(myTimeStamp))
# to UTC (universal)
# print(datetime.utcfromtimestamp(myTimeStamp))
mydateTime = datetime(year=2022, month=11, day=5, hour=17, minute=57)
# print(mydateTime.timestamp())
currentTime = datetime.now()
currentTimeStamp = datetime.timestamp(currentTime)
currentTimeD = datetime.fromtimestamp(currentTimeStamp)
# print(currentTimeStamp,currentTimeD)
numpyTimeStamp = np.datetime64('2022-11-05 18:34:36')
print(numpyTimeStamp)