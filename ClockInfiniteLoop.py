#Infinite Loop clock program custumized to operate on Mountain Standard Time

import datetime
import time
from pytz import timezone

timeout = True
while timeout:
    currentDate = datetime.datetime.now(timezone('MST'))
    print (currentDate.strftime("%m-%d-%Y %H:%M:%S"))
    timeout += 1
    time.sleep(1)
