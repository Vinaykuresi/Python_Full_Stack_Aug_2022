
# time module

import time
import datetime

# start time
print(time.gmtime(0))

print(time.time())

print(time.ctime(1663731732.9727519))

# for num in range(5):
#     time.sleep(2)
#     print(num)

print(time.gmtime())
print(time.localtime())

print(datetime.date.today())

print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))

