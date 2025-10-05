balance = 1000

print ( "`````````````Welcome to the ATM \n Your balance is: ") 
print(balance) 

while True:
    
    print(" \n 1. Check Balance \n 2. Deposit Money \n 3. Withdraw Money \n 4. Exit")
    menuselect = input("Choose an option :")


    if menuselect == "1":
        print("your balance is: ")
        print(balance)

    elif menuselect == "2" :
        print("Enter amount to deposit: ")
        deposit = int(input())
        balance = balance +  deposit
        print ("Deposit successful. New balance = ") 
        print (balance) 

    elif menuselect == "3" :
        print("Enter amount to withdraw: ")
        withdraw = int(input())

        if withdraw > balance:
            print ("Insufficient funds!")

        else :
            balance = balance - withdraw
            print ("Withdrawal successful. New balance = ") 
            print (balance)

    elif menuselect == "4" :
            print("Goodbye")
            break
    
    else:
        print("You must choose a valid option from the Menu!")