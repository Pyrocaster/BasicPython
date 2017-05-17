# -*- coding: utf-8 -*-
"""
Created on Thu May 11 08:55:00 2017

@author: srini
"""
class PvFvParameters:
    def __init__(self):
        fRate = 0.0
        fAmount = 0.0
        iNumPeriods = 0


#Gets a positive integer input from user, will display prompt text to user
def inputPositiveInteger(inputPromptText, errorPromptText):
    while True:
        iInput = input(str(inputPromptText))
#       check if input is an integer and greater than 0. If true return value, else ask for resubmission
        if ((type(iInput) == int) and (iInput > 0)):
               return iInput
        else:
            print(str(errorPromptText))
            continue

#Gets any integer input, will display prompt text to user
def inputInteger(inputPromptText, errorPromptText):
    while True:
#       check if input is an integer. If true return the integer else ask for resubmission
        iInput = input(str(inputPromptText))
        if (type(iInput) == int):
               return iInput
        else:
            print(str(errorPromptText))
            continue

#Gets a positive floating point input, will display the promptText to the user
def inputPositiveNumber(inputPromptText, errorPromptText):
    while True:
#       check if input is an int/float and greater than 0. If true return value, else ask for resubmission
        fInput = input(str(inputPromptText))
        if (((type(fInput) == int) or (type(fInput) == float)) and (fInput > 0)):
               return fInput
        else:
            print(str(errorPromptText))
            continue

#Gets any floating point input, will display prompt text to the user
def inputNumber(inputPromptText, errorPromptText):
    while True:
#       check if input is an int/float. If true return value, else ask for resubmission
        fInput = input(str(inputPromptText))
        if ((type(fInput) == float) or (type(fInput) == int)):
               return fInput
        else:
            print(str(errorPromptText))
            continue

#Returns a PvFVParameters object containg user set parameters for calculation
def GetInputParameters():
    userInputs = PvFvParameters()
    sTimeInputPrompt = "Enter: number of time periods (n) = "
    sTimeErrorPrompt= "Input Error: The number of periods MUST be a positive integer"
    sRateInputPrompt = "Enter: interest rate (r) = "
    sRateErrorPrompt= "Input Error: The interest rate MUST be a number"
    sAmountInputPrompt = "Enter: amount (P) = "
    sAmountErrorPrompt= "Input Error: The Amount MUST be a positive number"
    userInputs.iNumPeriods = inputPositiveInteger(sTimeInputPrompt, sTimeErrorPrompt) 
    userInputs.fRate = inputNumber(sRateInputPrompt, sRateErrorPrompt)
    userInputs.fAmount = inputPositiveNumber(sAmountInputPrompt, sAmountErrorPrompt)
    return userInputs
