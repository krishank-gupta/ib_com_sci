# imports
from library.library import hashLine,centerVal,colorCodes as cc
from library.validation import validate_int, validate_int_between, validate_str
from library.login import login, signup
# important variables

# prints
print(f"""{cc['purple']}{hashLine}
#{"Hello and welcome to Crypty. Please register or login to continue.".center(centerVal-2)}#
# 1. Register{"".center(centerVal-int(len(" 1. Register"))-2)}#
# 2. Login{"".center(centerVal-int(len(" 2. Login"))-2)}#
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
    else:
        loginMessage = f"""{cc['purple']}{hashLine}\n#{"Login".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal)
        # loginMessage = 'login'
        print(loginMessage)
        if login(getUsername(), getPswd()) == True:
            print(f"""{cc['green']}{hashLine}\n#{"Login Success".center(centerVal-2)}#\n{hashLine}{cc['end_code']}""".center(centerVal))

            return True

def menu():
    menuOptions = ["1. See description of USD Coin", "2. Enter"]
    print(f"""{cc['purple']}{hashLine}\n#{"Choose an option.".center(centerVal-2)}#\n# 1. See description of USD Coin{"".center(centerVal-int(len(" 1. See description of USD Coin"))-2)}#\n# 2. Enter a transaction{"".center(centerVal-int(len(" 2. Enter a transaction"))-2)}#\n# 3. Withdraw a transaction{"".center(centerVal-int(len(" 3. Withdraw a transaction"))-2)}#\n# 4. Profit/Loss calculator{"".center(centerVal-int(len(" 4. Profit/Loss calculator"))-2)}#\n# 5. Logout{"".center(centerVal-int(len(" 5. Logout"))-2)}#\n# 6. Exit{"".center(centerVal-int(len(" 6. Exit"))-2)}#\n{hashLine}{cc['end_code']}""")

    menuChoice = validate_int_between('Choose an option: ', 1,6, "blue")    

    print(menuChoice)


# MAIN
if(loginSystem() == True):
    menu()
