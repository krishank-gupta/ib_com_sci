# Function that will create the truth table
def get_truth():
    # Print heading
    print("| A | B | C |")

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
        
        # Print the combination of a,b,c. Int() converts true false to 0s and 1s
        print(f"| {int(a)} | {int(b)} | {int(c)} |")

# run the function
get_truth()