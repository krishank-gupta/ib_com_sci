# Main function
def get_truth():

    # Create variable with header
    initMsg = f"| A | B | C | {'AB + notB + notB C'.center(20)} |"
    
    # Create a boundry using the header variable's length
    print(f"{'-'*len(initMsg)}")

    # Print the header
    print(initMsg)

    # boundry beneath the header
    print(f"{'-'*len(initMsg)}")

   # Initialize three variables that will be the value of A B C
    a = 1
    b = 1
    c = 1

    # For loop in range 0 to 2^3 (since we have three variables) with 1 increment
    for i in range(0, 8, 1):         
        
        # Switch value of a after 4 increments
        if i % 4 == 0:
            a = not a
        
        # Switch value of b after 2 increments
        if i%2 == 0:
            b = not b
        
        # Switch value of c after every increment
        c = i%2

        # variable for result of operation according to description of quiz
        operator = (a and b) or (not b) or ((not b) and c)

        # print a,b,c and the solution
        print(f"| {int(a)} | {int(b)} | {int(c)} | {str(int(operator)).center(20)} |")
        
    # print a border at the bottom
    print(f"{'-'*len(initMsg)}")

# call the function
get_truth()