# Using random library to get a random number
import random

# Ask user for length of password
pswdLength = input("Please enter the length of the passwords: ")

# Validate input is a number
if not pswdLength.isdigit():
  pswdLength = input('Please enter a numeric value: ')
pswdLength = int(pswdLength)

# Ask user if the user wants symbols in the password
symbolsBool = input("Do you want symbols on the password?: (yes or no) ")

# Variables for characters and symbols
characters = 'abcdefghijklmnopwrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
symbols = "!@#$%^&*()"

# Codes for color in the terminal output
endCode = "\033[00m"
redPrint = "\33[0;31m"

# validate if user said yes or no and turn it into a boolean
if symbolsBool == 'yes':
  symbolsBool = True
elif symbolsBool == 'no':
  symbolsBool = False
else:
  symbolsBool = input('Please enter "yes" or "no": ')

# If true, add symbols string to characters string
if symbolsBool == True:
  characters += symbols

# Function that generates the password. This function can be called multiple times to get multiple passwords.
def pswdGenerator(passwordLength):

  # Empty string where the password will be stored
  pswd = ''

  # Loop through the length of the password
  for i in range(0, passwordLength-1, 1):
    # rand is a random characacter generated from the characters list
    rand = characters[random.randint(0, len(characters)-1)]
    # Add the random character to the password
    pswd += rand

  # Return the password
  return pswd

# For loop to print multiple passwords
for n in range(10):
  print(f"Generated passwords are " + f"{redPrint} {pswdGenerator(pswdLength)} {endCode}")



