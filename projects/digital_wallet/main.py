# imports
from library.library import hashLine,centerVal,colorCodes as cc, validate_int, validate_int_between, validate_str
from library.login import login, signup
# important variables

# prints
loginOptions = ['1. Register', '2. Login']

print(f"""{cc['purple']}{hashLine}
#{"Hello and welcome to Crypty. Please register or login to continue.".center(centerVal-2)}#
# {loginOptions[0]}{"".center(centerVal-int(len(loginOptions[0]))-3)}#
# {loginOptions[1]}{"".center(centerVal-int(len(loginOptions[1]))-3)}#
{hashLine}{cc['end_code']}""")

def getUsername():
    return validate_str(f"{cc['blue']}Please enter username: {cc['end_code']}", "blue")

def getPswd():
    return validate_str(f"{cc['blue']}Please enter password: {cc['end_code']}", "blue")

def loginSystem():

    loginChoice = validate_int_between('Press 1 to register, 2 to login: ', 1,2, "blue")    

    if loginChoice == 1:
        registerMessage = f"""{cc['purple']}{hashLine}\n#{"Register".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal)
        # registerMessage = 'register'
        print(registerMessage)
        signup(getUsername(), getPswd())
        
        print(f"""{cc['green']}{hashLine}\n#{"Register Success".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal))

        return True
    
    elif loginChoice == 2:
        loginMessage = f"""{cc['purple']}{hashLine}\n#{"Login".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal)
        # loginMessage = 'login'
        print(loginMessage)
        while(login(getUsername(), getPswd()) == False):
            login(getUsername(), getPswd())

        print(f"""{cc['green']}{hashLine}\n#{"Login Success".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal))

        return True

def menu():
    menuOptions = ["1. See description of USD Coin", "2. Enter a transaction", "3. Withdraw a transaction", "4. see all transaction", "5. Profit/loss calculator", "6. Exit"]

    menuOptionsPrint = (f"""{cc['purple']}{hashLine}\n#{"Choose an option.".center(centerVal-2)}#\n# {menuOptions[0]}{"".center(centerVal-int(len(menuOptions[0]))-3)}#\n# {menuOptions[1]}{"".center(centerVal-int(len(menuOptions[1]))-3)}#\n# {menuOptions[2]}{"".center(centerVal-int(len(menuOptions[2]))-3)}#\n# {menuOptions[3]}{"".center(centerVal-int(len(menuOptions[3]))-3)}#\n# {menuOptions[4]}{"".center(centerVal-int(len(menuOptions[4]))-3)}#\n# {menuOptions[5]}{"".center(centerVal-int(len(menuOptions[5]))-3)}#\n{hashLine}{cc['end_code']}""")

    print(menuOptionsPrint)
    menuChoice = validate_int_between('Choose an option: ', 1,6, "blue")    

    while(True):

        if menuChoice == 1:
            print("usd coin is a bs")

        if menuChoice == 2:
            


            print("enter a transaction")

            categories = ['Expenses', 'incomes']


        if menuChoice == 3:
            print("withdraw transaction")

        if menuChoice == 4:
            print('see all transactions')
            with open("data/transactions.csv", 'r') as file:
                transactionDb = file.readlines()
                for line in transactionDb:
                    print(line.strip().split(','))
            file.close()

        if menuChoice == 5:
            print('profits and loss')

        if menuChoice == 6:
            quit()
        
        break

        # print(menuOptionsPrint) 
        # menuChoice = validate_int_between('Choose an option: ', 1,6, "blue")    
        

# MAIN
# if(loginSystem() == True):
    # menu()

menu()