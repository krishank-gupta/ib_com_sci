from subtask1 import colors, lockerColors


while True:
    inputCol = input("Please enter a color (red, white, yellow, blue):")
    inputCol = inputCol.lstrip().rstrip().lower()
    if inputCol in colors:
        break
    elif inputCol.isdecimal() or inputCol.isspace() or inputCol.isdigit():
        print("Please enter a string")
    else:
        print("Please enter a correct color")

lockersWithColor = []
for idx,i in enumerate(lockerColors):
    if i == inputCol:
        lockersWithColor.append(idx+1)

print(lockersWithColor)
