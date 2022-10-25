end_code = "\033[00m"
green = "\033[0;32m"

while True:
  userInput = input("Please enter a number to get a multiplication table: (2-9) ")
  try:
    userInput = int(userInput)
    if userInput >= 2 and userInput <= 9:
      break;
    else:
      print(f"You entered {userInput}. This is not a number between 2 and 9. Please enter a number between 2 and 9")
  except ValueError:
    try:
      float(userInput)
      print(f"You entered {userInput}. This is not a whole number. Please enter a whole number")
    except ValueError:
      print(f"You entered {userInput}. Please enter a number")

def multiplesOfTwo(num):
  outputArr = []
  for i in range(1, 10, 1):
    outputArr.append(f"{num} * {i} = {num*i}\n")
  outputStr = "".join(outputArr)
  return outputStr

title = f"Multiplication table of {userInput}"
print(f"""{green}{title}\n{multiplesOfTwo(userInput)}{end_code}""")