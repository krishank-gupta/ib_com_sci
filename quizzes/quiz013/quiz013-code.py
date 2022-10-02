while True:
  inputA = input("Please enter a number: ")
  inputB = input("Please enter another number: ")
  
  try:
    inputA = int(inputA)
    inputB = int(inputB)
    break
  except ValueError:
    print(f"You entered {inputA} and {inputB}. Please make sure both entries are numbers")

def mystery(a, b):

    multiplication = a * b

    if a != b:
        return multiplication - abs(a - b)
    else:
        return multiplication - a

print(mystery(inputA,inputB))