import random
import datetime
import time

database = {}

def init():
    print("WELCOME TO BANK ZURI\n")
    
    start()

def start():     
    print("What would you like to do?\nCreate a new account or login to existing account?")
    options = input(f"Select 1 to create an account\n"
                    f"Select 2 to login\n"
                    f"Select 3 to exit application\n"
                    f"Enter option here: ")
    if options.isdigit():
        if int(options) == 1:
            createAccount()
        elif int(options) == 2:
            logIn()
        elif int(options) == 3:
            exit
        else:
            print("Error!!! Invalid Selection!\n")
            
            start()
    else:
        print("Error!!! Invalid Selection!\n")
        
        start()

###login function
def logIn():
    print("\nLogin to your account")
    print("=====ENTER YOUR LOGIN DETAILS HERE=====")
    userAccount = input("Enter your account number: ")
    userPass = input("Enter your password: ")
    
    ###Login validation loop
    if userAccount.isdigit():
        UserAccount = int(userAccount)
        if UserAccount in database.keys():
            for key, value in database.items():
                if UserAccount == key:
                    if userPass == value[3] in database[key]:
                        print("Login Successful!\n")
                        timeStamp = datetime.datetime.now().timestamp()
                        logInTime = time.ctime(timeStamp)
                        print(f"Welcome {value[1]} {value[2]}\n{logInTime}")
                        print("\n")
                        
                        bankOperations(UserAccount)
                    else:
                        print("The account number and/or password entered is incorrect\n")
                        
                        logIn() 
        elif UserAccount not in database.keys() and len(userAccount) != 10:
            print("The account number and/or password entered is incorrect\n")

            logIn()
        else:
            print("The account number entered does not exist\n")
            
            start()      
    else:
        print("Error!!! Account number must contain only digits\n")
        
        logIn()


def createAccount():
    print("\nCreate an account.")
    print("*****REGISTER HERE*****")
    
    ###entering account info and loops for validatiing each input
    firstName = input("What is your First Name?: ")
    while len(firstName) == 0 or firstName.isspace() == True or firstName.isalpha() == False:
        print('Error! First name cannot be empty or contain digits or spaces\n')
        firstName = input("What is your First Name?: ")
    
    lastName = input("What is your Last Name?: ")
    while len(lastName) == 0 or lastName.isspace() == True or lastName.isalpha() == False:
        print('Error! Last name cannot be empty or contain digits or spaces\n')
        lastName = input("What is your Last Name?: ")
    
    email = input("Enter your email address?: ")
    while len(email) == 0 or email.isspace() == True:
        print('Error! email cannot be empty\n')
        email = input("Enter your email address?: ")
    
    print(f"Create your unique password\n"
        f"#Hint: password should be at least 8 characters, alphanumeric and must contain at least one lower and one uppercase letter\n")
    
    ###Password validation loop
    validPassword = False
    while validPassword == False:
        password = input("Enter password here: ")
        if len(password) >= 8:
            isalphanum = not password.isdigit() and not password.isalpha()
            if isalphanum == True:
                validChar = not password.isupper() and not password.islower()
                if validChar == True:
                    validPassword = True
                    break
        print("Invalid password combination, please see hint above")

    ###generates account number and stores account details in database
    accountNumber = generateAccountNumber()
    print("\nYour account has been successfully created.")
    print(f"Your account number is {accountNumber}. Please copy and store it safely\n")
    database[accountNumber] = [email, firstName, lastName, password, 0]

    logIn()
    
###banking transaction function
def bankOperations(account):
    print("How can we help you today?")
    print('The available options are: \n')
    print('1. Cash Deposit\n')
    print('2. Withdrawal\n')
    print('3. Check Balance\n')
    print('4. Complaints\n')

    options = [1, 2, 3, 4]
    select = input('Please select an option...: ')
    
    ###validates user input
    if select.isdigit() == False:
        print('ERROR! Invalid option selected, please try again\n')
        
        bankOperations(account)
    
    elif(int(select) > 0 and int(select) <= len(options)):
        optionChoosen = int(select)
        if optionChoosen == 1:
            cashDeposit = int(input('How much would you like to deposit?: '))
            
            updateBalance(account, cashDeposit, optionChoosen)
            
            redoOperation(account)

        elif optionChoosen == 2:
            cashWithdrawn = int(input('How much would you like to withdraw?: '))
            
            updateBalance(account, cashWithdrawn, optionChoosen)
            
            redoOperation(account)

        elif optionChoosen == 3:
            balance = 0
            
            updateBalance(account, balance, optionChoosen)
            
            redoOperation(account)

        else:
            print('What issue will you like to report?')
            complaint = input('Please enter your complaint here: ')
            print('Your complaint has been forwarded to our customer care agents. We will get back to you shortly.')
            print('Thank you for contacting us.\n')
            
            redoOperation(account)
    else:
        print('ERROR! Invalid option selected, please try again\n')
        
        bankOperations(account)

###updates balance per bank transaction for each customer
def updateBalance(acct_number, amount, opt):
    for key, value in database.items():
        if key == acct_number:
            if value[4] in database[key] and opt == 1:
                    value[4] += amount
                    print('Deposit successful!')
                    print(f'Your current balance is: ${value[4]}\n')
            elif value[4] in database[key] and opt == 2:
                if amount <= value[4]:
                    value[4] -= amount
                    print(f'Take your cash: ${amount}\n')
                    print(f'Your current balance is: ${value[4]}\n')
                else:
                    print(f"Sorry, your account balance is insufficient for this transaction. Please deposit funds\n"
                        f'Your current balance is: ${value[4]}\n')
            elif value[4] in database[key] and opt == 3:
                value[4] += amount
                print(f'{value[1]}, your current balance is: ${value[4]}\n')


def redoOperation(acct):
    other = int(input('Enter 1 to perform another operation or 2 to logout: \n'))
    if other == 1:
        bankOperations(acct)
    
    elif other == 2:
        logOut()
    
    else:
        print("Invalid selection!")

        redoOperation(acct)

def logOut():
    init()

def generateAccountNumber():
    return random.randint(1111111111, 9999999999)


##### INITIALIZED BANKING SYSTEM #####
init()