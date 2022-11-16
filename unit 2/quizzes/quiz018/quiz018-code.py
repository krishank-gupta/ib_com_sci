# Import the math library to use the ciel function for rounding up
import math

# function that takes in the l and s
def numberMatches(l,s):
    # calculates output based on the question and returns from the function
    return math.ceil((l * (100/s))/5)

# Test cases
case1 = (100,100)
case2 = (250,110)
case3 = (500,150)
case4 = (12345,123)

# Outputs
print(f"Case: {case1} Number of matches: {numberMatches(case1[0], case1[1])} matches")
print(f"Case: {case2} Number of matches: {numberMatches(case2[0], case2[1])} matches")
print(f"Case: {case3} Number of matches: {numberMatches(case3[0], case3[1])} matches")
print(f"Case: {case4} Number of matches: {numberMatches(case4[0], case4[1])} matches")
