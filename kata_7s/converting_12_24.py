# Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030")
# sounds easy enough, right? Well, let's see if you can do it!
#
# You will have to define a function, which will be given an hour (always in the range of 1 to 12,
# inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either a.m. or p.m.) as input.
#
# Your task is to return a four-digit string that encodes that time in 24-hour time.
#
# Notes
#
# By convention, noon is 12:00 pm, and midnight is 12:00 am.
# On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example,
# 12:15 am. On 24-hour clock, this translates to 0015.

def to24hourtime(hour, minute, period):
    if period == 'am' and hour == 12:
        hour = 0
    elif period == 'pm' and hour != 12:
        hour += 12
    return f"{hour:02}{minute:02}"


def to24hourtime3(hour, minute, period):
    if hour == 12 and period == "am":
        hour = 0
    elif period == "pm" and hour != 12:
        hour += 12

    return f"{hour:02d}{minute:02d}"


def to24hourtime2(hour, minute, period):
    m = f"{minute}"
    if minute < 10:
        m = f"0{minute}"

    if period == 'am':
        if hour == 12:
            return f'00{m}'
        elif hour < 10:
            return f"0{hour}{m}"
        return f"{hour}{m}"

    h = ''
    if hour < 12:
        return f'{hour + 12}{m}'
    return f"{hour}{m}"