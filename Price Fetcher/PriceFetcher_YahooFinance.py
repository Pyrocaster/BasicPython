# -*- coding: utf-8 -*-
"""
Created on Wed May 17 03:11:42 2017

@author: srini
"""
import pandas_datareader as pd
import pandas.io as io
import PriceFetcher_Utilities as util
import os

#Get start and end dates
print("Enter a start date: ")
dtStartDate = util.GetUserInputDate()
print("\nStart date = " + dtStartDate.strftime("%d, %b %Y") +"\n")
        
print("Enter an end date: ")
dtEndDate  = util.GetUserInputDate()
print("\nEnd date = " + dtEndDate.strftime("%d, %b %Y") +"\n")

#If the end date comes before the start date, prompt user to swap. Else, exit program
if(dtEndDate < dtStartDate):
    print("The input end date ("+ str(dtEndDate) +") is before the start date ("+ str(dtStartDate) +")")
    choice = raw_input("Press \'S\' to swap (or anything else to quit): ")
    #swap start and end date
    if(choice == "S"):
        dtTemp = dtStartDate
        dtStartDate = dtEndDate
        dtEndDate = dtTemp
        print("Dates are successfully swapped! new start date = " + str(dtStartDate) + " and new end date = " + str(dtEndDate))
    else:
        print("exiting program")
        exit(1)

#Retrieve stock price data
ticker = raw_input("Enter Stock Ticker: ")

try:
    stockData = pd.DataReader(ticker,'google',dtStartDate, dtEndDate)
except:
    print "ERROR getting data from Yahoo Finance. Can't access ticker: '" + ticker + "'"

#Write stock data to csv 
#Generate new filename
newFileName = "StockData_" + str(ticker) + "_" + str(dtStartDate) + "_to_" + str(dtEndDate)
folderName = "Downloaded Data"

#If folder does not exist, create it.
if(not os.path.isdir(folderName)):
    os.makedirs(folderName)
    
#Write file with stock data
stockData.to_csv("Downloaded Data\\"+newFileName+".csv")





        
        
