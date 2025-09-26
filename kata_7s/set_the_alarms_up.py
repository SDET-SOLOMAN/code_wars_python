# We all love to have some rest. Also we all hate the sound of our alarms but it's inevitable at the end of the day. However, one is definitely not enough to wake you up. You set multiple alarms, just to force yourself to get up and go back to work/studies or just anything. It is getting annoying, setting those up manually, so you decide to write a script for this task.


# Task
# Given the time to be set to wake up and the amount of alarms needed to be set, return an array of all timestamps for the alarms. The typical interval between the alarms is 5 minutes (at least, I think so).


# Examples
# set_the_alarms_up("08:00", 5) # Should return ["08:00", "08:05", "08:10", "08:15", "08:20"]
# set_the_alarms_up("07:45", 8) # Should return ["07:45", "07:50", "07:55", "08:00", "08:05", "08:10", "08:15", "08:20"]
# set_the_alarms_up("23:55", 2) # Should return ["23:55", "00:00"]
# Input
# time - a string, representing the time. Will always be valid. (no 25:30, 08:65 and etc.)

# n - a number of alarms, needed to be set up. (n > 1, simply cause noone wakes up to one alarm)

# Output
# An array, consisting of all timestamps, an alarm is going to ring.

def set_the_alarms_up(time, n):
    
    hour, minute = (int(x) for x in time.split(":"))
    re = []
    
    for num in range(n):
        
        if minute >= 60:
            hour += 1
            minute = minute % 60
        if hour > 23:
            hour = 0
        h = str(hour) if hour > 9 else f'0{hour}'
        m = str(minute) if minute > 9 else f'0{minute}'
        re.append(f'{h}:{m}')
        minute += 5

    return re

def set_the_alarms_up2(time, n):
    
    hour, minute = (int(x) for x in time.split(":"))
    re = []
    
    for num in range(n):
        re.append(f"{hour:02d}:{minute:02d}")
        
        minute += 5
        if minute >= 60:
            hour += 1
            minute = minute % 60
        if hour > 23:
            hour = 0
        
    return re