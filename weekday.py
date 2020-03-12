#Program that outputs whether or not today is a weekday
# Ref: Week 5 lecture : What are dictionaries?  
# https://web.microsoftstream.com/video/77f26693-82ed-4006-8c22-c61d37e2f77f  (time 08.25)

import datetime
now = datetime.datetime.now()
# day_index 0-6 represent the days of the week, starting from Monday.
# i.e Monday = 0, Tuesday = 1 ... Saturday = 5 and Sunday = 6
day_index = now.weekday()
if day_index < 5:
   print ('Yes, unfortunately today is a weekday.')
else:
    print('It is the weekend, yay!')