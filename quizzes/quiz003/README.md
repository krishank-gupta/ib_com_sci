# Quiz 003

```.py

# Initialize variables: Input in the form of a string, empty string to store output
proteinInput = 'CGATAGCTAGCTGATCGATCGATCGGTCAGTCGAT'
proteinOutput = ""

# Loop through every character in string, replace using description from the problem
for proteinStr in proteinInput:    
  # If input character is A, replace with T
  if(proteinStr == 'A'):
    proteinOutput += 'T'
  # If input character is G, replace with C
  elif(proteinStr == 'G'):
    proteinOutput += 'C'
  # If input character is T, replace with A
  elif(proteinStr == 'T'):
    proteinOutput += 'A'
  # If input character is C, replace with G
  elif(proteinStr == 'C'):
    proteinOutput += 'G'
  else:
    # Return error if input character doesn't match the description
    proteinOutput += 'ERROR'

# Print Output 
print(f"The Input was {proteinInput} and the output is {proteinOutput}")

```

Here are the results of the test case. CGATAGCTAGCTGATCGATCGATCGGTCAGTCGAT

![quiz003-results](./quiz003-results.png)
