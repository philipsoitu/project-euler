"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def isLeapYear(year):
    return ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)))


def daysInMonth(year, month):
    table = {
        0 : 30,
        1 : 29 if isLeapYear(year) else 28,
        2 : 31,
        3 : 30, 
        4 : 31,
        5 : 30,
        6 : 31,
        7 : 30, 
        8 : 30,
        9 : 31,
        10 : 30,
        11 : 31
        }
    return table[month]


def isSunday(daysSince01Jan1900):
    return ((daysSince01Jan1900+1)%7==0)


daysSince01jan1900 = 1

for year in range(1900, 1901):
    for month in range(12):
        daysSince01jan1900 += daysInMonth(year, month)
        print(year, month, isSunday(daysSince01jan1900))