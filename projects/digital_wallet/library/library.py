import datetime

colorCodes = {
    # NORMAL
    'black': '\33[0;30m',
    'red': '\33[0;31m',
    'green': '\33[0;32m',
    'yellow': '\33[0;33m',
    'blue': '\33[0;34m',
    'purple': '\33[0;35m',
    'cyan': '\33[0;36m',
    'white': '\33[0;37m',
    # BOLD
    'black_bold': '\33[1;30m',
    'red_bold': '\33[1;31m',
    'green_bold': '\33[1;32m',
    'yellow_bold': '\33[1;33m',
    'blue_bold': '\33[1;34m',
    'purple_bold': '\33[1;35m',
    'cyan_bold': '\33[1;36m',
    'white_bold': '\33[1;37m',
    # UNDERLINE
    'black_underline': '\33[4;30m',
    'red_underline': '\33[4;31m',
    'green_underline': '\33[4;32m',
    'yellow_underline': '\33[4;33m',
    'blue_underline': '\33[4;34m',
    'purple_underline': '\33[4;35m',
    'cyan_underline': '\33[4;36m',
    'white_underline': '\33[4;37m',
    # BACKGROUND
    'black_background': '\33[40m',
    'red_background': '\33[41m',
    'green_background': '\33[42m',
    'yellow_background': '\33[43m',
    'blue_background': '\33[44m',
    'purple_background': '\33[45m',
    'cyan_background': '\33[46m',
    'white_background': '\33[47m',
    'end_code': '\033[00m',
    'reset': '\33[0m'
}

cc = colorCodes

def validate_int(msg, inputColor):
    while True:
        try:
            val = int(input(f"{cc[inputColor]}{msg}{cc['end_code']}"))
            return val
        except ValueError:
            print(f"{cc['red_background']}Please enter a integer{cc['end_code']}")

def validate_int_between(msg, startNum, endNum, inputColor):
    while True:
        try:
            val = int(input(f"{cc[inputColor]}{msg}{cc['end_code']}"))
            if val >= startNum and val <= endNum:
                return val
            else:
                print(f"{cc['red']}Please enter a number between {startNum} and {endNum}{cc['end_code']}")
        except ValueError:
            print(f"{cc['red']}Please enter an integer{cc['end_code']}")


def validate_str(msg,inputColor):
    while True:
        str = input(f"{cc[inputColor]}{msg}{cc['end_code']}")
        if str.isalnum():
            return str
        else:
            print(f"{cc['red']}Please enter a string{cc['end_code']}")

def validate_date(msg, inputColor):
    while True:

        try:
            date_text = input(f"{cc[inputColor]}{msg}{cc['end_code']}")
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            break
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")

    return date_text

centerVal = int(80)
hashLine = '#'*centerVal