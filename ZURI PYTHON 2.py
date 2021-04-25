# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:40:35 2021

@author: OLUWABUSUYI
"""

import datetime

from datetime import datetime,date, time
import random


    
import random    
database = {}
def login():
            print ("Please login")
        
def accountNumGen():
            #print ("Account number generator")
            return random.randrange [1111111111,9999999999]
            
def register():
            #print ("this is the register function")
             
             email = input ("what is your email address \n")
             name = input ("what is your name? \n")
             password = input ("Please create a password \n")
                   
             accountNumber = accountNumGen()
             database[accountNumber] = [name, email, password]
             
             #return database
             print ("Account created")
    
    
def init():
        isValidOption = False
        print ("Welcome to bankPHP")
        
        while isValidOption == False:
            
            haveAccount = int(input("Do you have an account? 1(yes) 2(no) \n"))
            
            if haveAccount == 1:
                isValidOption = True
                login()
                
            elif (haveAccount == 2):
                isValidOption = True
                register()
                
            else:
              print ("you have selected an invalid option")
              
              
name = input ('What is your name?')

allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if (name in allowedUsers):
    password = input('your password? /n')
    userId = allowedUsers.index(name)
    
    if (password == allowedPassword[userId]):
        
        currentDatetime = datetime.now()
        print (currentDatetime)
        print ('Welcome %s' % name)
        print ('These are the available options')
        print ('1. Withdrawal')
        print ('2. Cash deposit')
        print ('3. Complaint')
        
        previousBalance = random.randint(1000, 100000)
        
        selectedOption = input ('Please select an option')
        if (selectedOption == '1'):
            withdrawal = input('how much would you like to withdraw?')
            print ('Take your cash')
            
        elif (selectedOption == '2'):
                cashDeposit = input ('How much will you like to deposit')
                cashDeposit = int(cashDeposit)
                currentBalance = int(cashDeposit + previousBalance)
                print('Your current balance is %s' % currentBalance)
                
        elif (selectedOption == '3'):
                    Complaint = input ('What issue will you like to report')
                    print ('Thank you for contacting us')
        else:
                    print ('Wrong input')
    else:
        print ('password incorrect, please try again')
        
else:
    print ('Name not found. Please try again')
               
               
 
    
                   
                
        

        