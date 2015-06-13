#!/usr/bin/python
import time
def isLeap(year):
    if (year % 400 == 0 or (year % 4 == 0 and (year % 100 != 0))):
        return True
    else:
        return False

def get_from_date(date, i):
    date_list = date.split('/')
    return int(date_list[i])

def days_to_date(month, day, year):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_in_months[0 : month -1 ]) + day + (isLeap(year) * (month >= 3)) 

def days_from_year(cur, pre):
    days = 0
    while pre != cur:
        days += 365 + isLeap(pre) 
        pre = pre + 1
    return days

# get current date and ask user's birthday 
current = time.strftime("%d/%m/%Y")
birth = raw_input("input your name in mm/dd/yy formate\n")

current_date = [get_from_date(current, 0), get_from_date(current, 1), get_from_date(current, 2)]
birth_date = [get_from_date(birth, 0), get_from_date(birth, 1), get_from_date(birth, 2)]

total_days = days_from_year(current_date[2], birth_date[2]) + days_to_date(current_date[0], current_date[1], current_date[2]) - days_to_date(birth_date[0], birth_date[1], birth_date[2]) 

print total_days
