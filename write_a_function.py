##Logics for Leap Year:
##    1. Every 4th year is a leap year
##    2. Every 100th year is not a leap year
##    3. Every 400th year is a leap year

def is_leap(year):
    leap = False
    if (year % 400 == 0):
        leap = True
    elif year % 4 == 0 and year % 100 !=0:
        leap = True    
    return leap




##Way 2

def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


##Way3
## You can import the calendar and return the value

import calendar

def is_leap(year):
    return calendar.isleap(year)
