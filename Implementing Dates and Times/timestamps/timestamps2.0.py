import pytz
from datetime import datetime
import pandas as pd
# converting between timezones
mydateTime = datetime(year=2022, month=11, day=5, hour=17, minute=57)
print(mydateTime.tzinfo)
