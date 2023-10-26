import datetime
import time

start_time = datetime.datetime.now()

for i in range(5):
    print(start_time.strftime("%H:%M:%S"))
    time.sleep(1)
    start_time = datetime.datetime.now()