import re
import time
import random

print ("Hello ! Welcome to AliBaba Bank! Please enter your name ! ")
money = 2422

def restarting():
    while True:
        nameinput = input("You: ")
        pattern = "^[a-z-A-Z]+$"
        nameMatch = re.match(pattern, nameinput)
    if nameMatch:
        time.sleep(1)
        print ("Checking Database for Name... ! ")
        time.sleep(2)
        print ("Registered !")

        #Message
print ("Good to see you", nameinput, "!")
print ("Please enter your pin number for Faster Service !")
        #Validating Numbers for Pin !
pinnumber1 = input()
while pinnumber1.isdigit()==False:
    print("Numbers ! Not Letters !")
    pinnumber1 = input("You : ")
print ("Your pin number is ", pinnumber1, "!")
print ("What can I help you with? \n 1> Account Balance \n 2> Transfer of Money \n 3>Transferring of Account \n 4>Change of Pin Number \n 5>Opening of new Bank Account ")
#Seeing your Balance Amount
helpinginput = input("")
if helpinginput == "1":
    print ("You currently have", money, "dollars in your account!")
    print ("Is there any other things i cant help with? Y/N")
inputYN1 = input ("You: ")
if inputYN1 == "Y":
        print ("You can type 2 / 3/ 4 for further enquires !")
if inputYN1 == "N":
        print ("Have a nice day ! ")
        restarting()
#2 - Transferring to Another Account within the same bank
if helpinginput == "2":
    print ("Please type in the account Number of the person you are transferring to !")
    otherpinnumber = input("You: ")
    while otherpinnumber.isdigit()==False:
        print("Account Number in numerical form ! ")
        otherpinnumber = input("You : ")
    print ("Please State the amount of cash you want to transfer !")
    amountofmoneytransfer = input("You: ")
    while amountofmoneytransfer.isdigit()==False:
        print("State the amount of cash in numerical form")
        amountofmoneytransfer = input()
    print ("Transferring", amountofmoneytransfer, "dollars to Account Number ", otherpinnumber)
    print (" ... \n ... \n ... \n ...")
    time.sleep(1.5)
    print ("Success ! ")
    time.sleep(1)
    print ("You can safely exit this app ! \n And you can restart it if you need any more help ! ")
    #Transferring to another Account 
elif helpinginput == "3":
     print (" Please State the Bank Account that you want to transfer to  \n 1> DBS \n 2> OCBC \n 3> POSB ")
     time.sleep(0.1)
     choosingbank = input("You: ")
    #DBS ACCOUNT
     if choosingbank == "1":
         print ("Please type your DBS Bank Account Number !")
         DBSAccount = input("AccountNumber: ")
         print ("Warning ! We take a $10 processing Fee for transferring ! So you would have",money-10 , "dollars as balance ! Y / N ")
         agreeing = input("You: ")
         if agreeing == "Y":
            print ("Transferring", money-10, "dollars to DBS Account Number : ", DBSAccount, "!")
            print (" ... \n ... \n ... \n ...")
            time.sleep(2)
            print ("Success ! ")
            time.sleep(1.5)
            print (" You can safely exit this app ! \n And you can restart it if you need any more help ! ")
         if agreeing == "N":
            print ("See you later ! ")
    #OCBC ACCOUNT
     if choosingbank == "2":
         print ("Please type your OCBC Bank Account Number !")
         OCBCAccount = input("AccountNumber:  ")
         print ("Warning ! We take a $10 processing Fee for transferring ! So you would have",money-10 , "dollars as balance ! Y / N ")
         agreeing2 = input("You: ")
         if agreeing2 == "Y":
            print ("Transferring", money-10, "dollars to OCBC Account Number : ", OCBCAccount, "!")
            print (" ... \n ... \n ... \n ...")
            time.sleep(2)
            print ("Success ! ")
            time.sleep(1.5)
            print (" You can safely exit this app ! \n And you can restart it if you need any more help ! ")
         if agreeing2 == "N":
            print ("See you later !")
     #POSB ACCOUNT
     if choosingbank == "3":
         print ("Please type your POSB Bank Account Number !")
         POSBAccount = input("AccountNumber: ")
         print ("Warning ! We take a $10 processing Fee for transferring ! So you would have",money-10 , "dollars as balance ! Y / N ")
         agreeing3 = input("You: ")
         if agreeing3 == "Y":
            print ("Transferring", money-10, "dollars to POSB Account Number", POSBAccount, "!")
            print (" ... \n ... \n ... \n ...")
            time.sleep(2)
            print ("Success ! ")
            time.sleep(1.5)
            print (" You can safely exit this app ! \n And you can restart it if you need any more help ! ")
         if agreeing3 == "N":
            print ("See you later !")
       #Option 4
elif helpinginput == "4":
    print ("Please enter your existing Pin Number! ")
    pinnumber = input("Existing Pin Number : ")
    print ("Please type your new pin number you have in mind !")
    newpinnumber = input("New Pin Number : ")
    print ("Validating...")
    time.sleep(1)
    print ("Validating...")
    time.sleep(1)
    print ("Success ! You can safely exit the app now ! ")
elif helpinginput == "5":
    print ("Please select the type of account you want to create ! \n 1> Savings Account \n 2> Investment Bond Account \n 3> Joint Account")
    selectingaccount = input("")
        #Savings Account
    if selectingaccount == "1":
            print ("Please State the maximum amount of cash you can withdraw each time !")
            maximumcash = input("Maximum Amount Of Cash : ")
            print ("The maximum amount of cash you can withdraw each time is", maximumcash, "!")
            print ("Set this account up? Y / N")
            agreeing4 = input("You: ")
            if agreeing4 == "Y":
                print ("Setting Account Up ! Please wait !")
                time.sleep(3)
                print ("Success ! Your new Savings account have been set up ! ")
                time.sleep(1)
                print ("You can safely exit the app !")
            if agreeing4 == "N":
                print ("See you later ! You can safely exit the app !")
        #Investment Account
    if selectingaccount == "2":
            print ("Please State the maximum amount of cash you want to invest each time !")
            maximumcashinvest = input("Maximum Amount Of Cash To Invest : ")
            print ("The maximum amount of cash you can invest each time is", maximumcashinvest, "!")
            print ("Warning ! Only invest amount that you can lose freely ! All Investment moves are final and there would be no Undoing ! ")
            print ("Set this account up? Y / N")
            agreeing5 = input("You: ")
            if agreeing5 == "Y":
                print ("Setting Account Up ! Please wait !")
                time.sleep(3)
                print ("Success ! Your new Investment account have been set up ! ")
                time.sleep(1)
                print ("You can safely exit the app !")
            if agreeing5 == "N":
                print ("See you later ! You can safely exit the app !")
        #JOINTACCOUNT
    if selectingaccount == "3":
            print ("Please type in the account numbers to set up joint account ! ")
            firstjointaccount = input("Account Number 1 : ")
            print ("Account Number 1 is", firstjointaccount, "!")
            secjointaccount = input("Account Number 2 : ")
            print ("Account Number 2 is", secjointaccount, "!")
            print ("Set this account up? Y / N")
            agreeing5 = input("You: ")
            if agreeing5 == "Y":
                print ("Setting Account Up ! Please wait !")
                time.sleep(3)
                print ("Success ! Your new joint account have been set up ! ")
                time.sleep(1)
                print ("You can safely exit the app !")
            if agreeing5 == "N":
                print ("See you later ! You can safely ex
