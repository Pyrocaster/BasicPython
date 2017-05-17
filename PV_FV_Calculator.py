# -*- coding: utf-8 -*-
"""
Created on Thu May 11 07:27:23 2017

@author: srini
"""
import locale
import PV_FV_Utilities
#Set locale for formatting
locale.setlocale(locale.LC_ALL,'')

#Calculate Present Value, given some input parameters in params
def CalculatePV(params):
    r = params.fRate
    P = params.fAmount
    n = params.iNumPeriods
    pv = P/((1+r)**n)
    return pv

#Calcuate Future Value, given some input parameters in params
def CalculateFV(params):
    r = params.fRate
    P = params.fAmount
    n = params.iNumPeriods
    fv = P*((1+r)**n)
    return fv
    
#Get user input (PV vs FV), keep prompting user till a valid input is given, or allow user to terminate program
pvFvChoice = 0
while True:
    pvFvChoice = input("Please choose one of the following options\n 1: Present Value\n 2: Future  Value\n-1: Exit Program\nYour Input = ")
    if pvFvChoice == -1:
        print("exiting program")
        sys.exit(1) 
    elif pvFvChoice == 1:
        print("You have chosen to compute Present Value")
        params = PV_FV_Utilities.GetInputParameters()
        fPV = CalculateFV(params)
        print("\nPresent Value = " + locale.currency(fPV))
        break
    elif pvFvChoice == 2:
        print("You have chosen to compute Future Value")
        params = PV_FV_Utilities.GetInputParameters()
        fFV = CalculatePV(params) 
        print("\nFuture Value = " + locale.currency(fFV))
        break
    else:
        print("I dont understand the input, please enter '1' for present value, '2' for future value, or '-1' to exit")
        continue




