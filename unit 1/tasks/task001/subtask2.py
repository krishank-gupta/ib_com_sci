from subtask1 import lockerColors

while True:
    userInp = input("Please enter a student number to check their locker color: ")
    try:
        userInp = int(userInp)
        if userInp > 0 and userInp <= 2400:
            break
        else:
            print(f"You entered {userInp}. This is not a number between 1 and 2400. Please enter a number between 1 and 2400")
    except ValueError:
        try:
            float(userInp)
            print(f"You entered {userInp}. This is not a whole number. Please enter a whole number")
        except ValueError:
            print(f"You entered {userInp}. Please enter a number")

print(lockerColors[userInp-1])