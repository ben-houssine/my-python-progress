import datetime
import time
from datetime import timedelta
from multiprocessing.resource_sharer import stop
from sqlite3 import Timestamp

def get_time():
    return datetime.datetime.now()


print("__________________________________")
print("START YOUR TIME BY PRESSING [ENTER]")
input("__________________________________\n")
time_start = get_time()

print("TIMER HAS STARTED...")
input("PRESS [ENTER] TO END THE TIMER\n")
time_stop = get_time()


total_time = round(timedelta.total_seconds(time_stop - time_start))

print("TOTAL TIME: ", total_time, "seconds\n")

print("programm is closing soon...")

#end of programm in 2s
def wait():
    time.sleep(3)

wait()

