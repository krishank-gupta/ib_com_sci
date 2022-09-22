# Initialize variables: Input in the form of a list, empty list to chunk first list into two elements
inputList = [20]
chunkedList = list()

# Check to see if list contains atleast two elements, else send error
if len(inputList) < 2:
  print('Please input atleast two elements in list')

# Split input list after every 2 elements and add to chunkedList
for i in range(0, len(inputList), 2):
    chunkedList.append(inputList[i:i+2])

# Loop through list of chunks in chunkedList
for inums in chunkedList:
  
  # Initialize a variable for output, change value to 'true' in case if matches the description of the problem
  output = 'false'
  
  # Loop through each element in the sublist in chunkedList
  for x in range(0,len(inums)-1):

    # See if elements equals to 20 or their sum equals to 20
    if (inums[x] == 20) or (inums[x+1] == 20) or (inums[x] + inums[x+1] == 20):
      output = 'true'

    # Print the output
    print(f"Numbers {inums} have an output of {output}")
