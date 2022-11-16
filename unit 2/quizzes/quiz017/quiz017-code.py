# Function that takes in words and returns 
def averageLength(words):
    # Initialize sum variable that will be used to calculate average
    sum = 0

    # For every word that is inputted in the function
    for i in words:

        # Remove empty space from the word
        i = str(i).replace(" ", "")
        
        # Find length of the word and add it to sum
        sum += len(i)

    # average = sum / number of words
    return sum / len(words)

# The test cases
caseOne = ["hello", "main"]
caseTwo = ["Peru", "France", "Nepal"]
caseThree = ["Computer Science", "Art"]
caseFour = ["one", "two"]

# Outputs
print(f"Words: {caseOne} Average = {averageLength(caseOne)}")
print(f"Words: {caseTwo} Average = {averageLength(caseTwo)}")
print(f"Words: {caseThree} Average = {averageLength(caseThree)}")
print(f"Words: {caseFour} Average = {averageLength(caseFour)}")