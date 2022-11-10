def validate_int(msg):
    while True:
        try:
            val = int(input(msg))
            return val
        except ValueError:
            print(f"Please enter an integer")

def validate_int_between(msg, startNum, endNum):
    while True:
        try:
            val = int(input(msg))
            if val >= startNum and val <= endNum:
                return val
            else:
                print(f"Please enter a number between {startNum} and {endNum}")
        except ValueError:
            print(f"Please enter an integer")


def validate_str(msg):
    while True:
        str = input(msg)
        if str.isalnum():
            return str
        else:
            print(f"Please enter a string")