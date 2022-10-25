# Initialize variables: Input in the form of a string, empty string to store output
proteinInput = 'CGATAGCTAGCTGATCGATCGATCGGTCAGTCGAT'
proteinOutput = ""

inputList = ['A', 'G', 'T', 'C']
outputList = ['T', 'C', 'A', 'G']

# Loop through every character in string, replace using description from the problem
for proteinStr in proteinInput:    
  proteinOutput += outputList[inputList.index(proteinStr)]

# Print Output 
print(f"The Input was {proteinInput} and the output is {proteinOutput}")
