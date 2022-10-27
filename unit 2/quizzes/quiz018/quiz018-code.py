import math

def numberMatches(l,s):
    return str(math.ceil((l * (100/s))/5)) + " matches"

print(numberMatches(100,100))
print(numberMatches(250,110))
print(numberMatches(500,150))
print(numberMatches(12345,123))

def numberMatchesAlgo(len,speed):
    matchesBurnt = 0

    while(len < 0):
        speed = speed * 100
        

