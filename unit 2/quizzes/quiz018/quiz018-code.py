import math

def numberMatches(l,s):
    return str(math.ceil((l * (100/s))/5)) + " matches"

case1 = (100,100)
case2 = (250,110)
case3 = (500,150)
case4 = (12345,123)

print(f"Case: {case1} Number of matches: {numberMatches(case1[0], case1[1])}")
print(f"Case: {case2} Number of matches: {numberMatches(case2[0], case2[1])}")
print(f"Case: {case3} Number of matches: {numberMatches(case3[0], case3[1])}")
print(f"Case: {case4} Number of matches: {numberMatches(case4[0], case4[1])}")

def numberMatchesAlgo(len,speed):
    matchesBurnt = 0

    while(len < 0):
        speed = speed * 100
        

