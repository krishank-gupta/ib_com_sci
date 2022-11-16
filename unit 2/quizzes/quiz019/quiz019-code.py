# Function that takes in the message and returns message with changes as per the quiz description
def get_l3tt3r(msg):

    # Dictionary with the required changes to message
    syntax = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        " ": "_"
    }

    # Initialize empty str for output. Will append output to this str later. 
    output = ""

    # For every character in the msg
    for i in msg:
        # If there is a letter that is a key in syntax dictionary
        if i in syntax:
            # Append the value pair of that key to output
            output += (str(syntax[i]))
        else:
            # If not then append char without formatting
            output += (str(i))
    # Return the output
    return output

# Test cases
case1 = ("Hello World")
case2 = ("Why did I choose CS")
case3 = ("Remember the Figure Caption")

# Outputs
print(f"Case: {case1}. output: {get_l3tt3r(case1)}")
print(f"Case: {case2}. output: {get_l3tt3r(case2)}")
print(f"Case: {case3}. output: {get_l3tt3r(case3)}")