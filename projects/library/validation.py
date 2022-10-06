from library.library import colorCodes as cc

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
