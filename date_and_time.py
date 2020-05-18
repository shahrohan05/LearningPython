import time
import calendar

print("Seconds elapsed since January 1, 1970 :" + str(time.time()))

print("System local time : ", time.localtime(time.time()))

print("Formatted time : ", time.asctime(time.localtime(time.time())))

print("Current year and month : ", time.localtime(
    time.time()).tm_year,  time.localtime(time.time()).tm_mon)

print("Current month calender :")
print(calendar.month(time.localtime(time.time()).tm_year,
                     time.localtime(time.time()).tm_mon))
