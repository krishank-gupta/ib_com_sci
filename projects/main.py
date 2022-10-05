# imports
from library.library import hashLine,centerVal,colorCodes as cc
from library.validation import validate_int, validate_int_between, validate_str
from library.login import login, signup
# important variables

# prints
print(f"""{cc['purple']}{hashLine}
#{"Hello and welcome to Crypty. Please register or login to continue.".center(centerVal-2)}#
# 1. Register{"".center(centerVal-14)}#
# 2. Login {"".center(centerVal-12)}#
{hashLine}{cc['end_code']}""")


def getUsername():
    return validate_str(f"{cc['blue']}Please enter username: {cc['end_code']}", "blue")

def getPswd():
    return validate_str(f"{cc['blue']}Please enter password: {cc['end_code']}", "blue")

loginChoice = validate_int_between('Press 1 to register, 2 to login: ', 1,2, "blue")    

if loginChoice == 1:
    print(f"""{cc['purple']}{hashLine}
#{"Register".center(centerVal-2)}#
{hashLine}{cc['end_code']}""".center(centerVal))

    signup(getUsername(), getPswd())
else:
    print(f"""{cc['purple']}{hashLine}
#{"Login".center(centerVal-2)}#
{hashLine}{cc['end_code']}""".center(centerVal))

    login(getUsername(), getPswd())

