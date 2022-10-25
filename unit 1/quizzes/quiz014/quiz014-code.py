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
    return (a*a) + b

print(f"The output is {mystery(inputA,inputB)}")

print(f"""
test cases:
37 and 3: {mystery(37,3)}
58 and 2: {mystery(58,2)}
60 and 5: {mystery(60,5)}
10 and 4: {mystery(10,4)}
""")