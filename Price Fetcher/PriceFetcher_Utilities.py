# -*- coding: utf-8 -*-
"""
Created on Wed May 17 03:59:46 2017

@author: srini
"""
import datetime as dt
import calendar as cal


#Returns command line input for year
def PromptUserForYear():
    while True:
        inputYear = input("Enter a Year: ")
        #Check if input is in the correct range
        if ((inputYear >= dt.MINYEAR) and (inputYear <= dt.MAXYEAR)):
            return inputYear
        else:
            print("Incorrect input. Year must be a number between " + str(dt.MINYEAR) + " and " + str(dt.MAXYEAR))
            continue

#Returns command line input for month (1-12)
def PromptUserForMonth():
    while True:
        inputMonth = input("Enter a Month (1-12): ")
        #Check if input is in the correct range (1-12)
        if ((inputMonth >= 1) and (inputMonth <= 12)):
            return inputMonth
        else:
            print("Incorrect input. Month must be a number between 1 and 12")
            continue
        
#Returns command line input for day (1-31) based on the year and month input. It takes leap years into account
def PromptUserForDay(dtYear, dtMonth):
    while True:
        #Get the number of days in the input month & year
        daysInMonth = cal.monthrange(dtYear, dtMonth)
        inputDay = input("Enter day of the Month: ")
        #Check if input is in correct range
        if ((inputDay >= 1) and (inputDay <= daysInMonth)):
            return inputDay
        else:
            print("Incorrect input. Based on the input year and month, the day must be a number between 1 and " + str(daysInMonth))
            continue
                          
#Returns a command line input date
def GetUserInputDate():
    while True:
        dtYear = PromptUserForYear()
        dtMonth = PromptUserForMonth()
        dtDay = PromptUserForDay(dtYear, dtMonth)
        dtDate = dt.date(dtYear, dtMonth, dtDay)
        return dtDate
