import time

seconds = 0
minutes = 0
hours = 0
days = 0
years = 0

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def zero_out():
    hours = 0
    minutes = 0
    seconds = 0

run = True
while run == True:
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    if hours == 24:
        days += 1
        hours = 0
        minutes = 0
        seconds = 0
    if days == 365:
        years += 1
        days = 0
        zero_out()
    day_name = days_of_week[days]
    print(day_name + " " + "Days: " + str(days) + " Years: " + str(years) + " | " + str(hours) + ":" + str(minutes) + ":" + str(seconds), end="\r")
    time.sleep(1)
