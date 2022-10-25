# Get user input and validate first element is number and second element exists
while True:
  userInput = input("Please enter the value and units: (Ex: 1 gram of salt) ")
  try:
    userInputNum = int(userInput[0])
    if len(userInput) > 1:
      break
    else:
      print(f"Please enter a unit as well.")
  except ValueError:
    print(f"You entered '{userInput}'. Please enter a quantity. The quantity must be a number.")

# Turn input into a list
userInputArr = userInput.split(" ")
# First element of list is the quantity
num = userInputArr[0]

# Function that prints the table
def unitsfunc(num, txt):
  a = f"""
  {num} 000 000 000 000 Tera{txt}
  {num} 000 000 000 Giga{txt}
  {num} 000 000 Mega{txt}
  {num} 000 Kilo{txt}
  {num} {txt}
  0.00{num} Mili{txt}
  0.000 00{num} Micro{txt}
  0.000 000 00{num} Nano{txt}
  0.000 000 000 00{num} Pico{txt}
  """
  return a

# Remove first element so the unit is left
userInputArr.pop(0)

# Print the function with params num and unit 
print(unitsfunc(num, " ".join(userInputArr)))

