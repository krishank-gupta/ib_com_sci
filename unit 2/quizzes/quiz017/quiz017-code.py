def averageLength(words):
    leng = len(words)
    sum = 0
    for i in words:
        i = str(i).replace(" ", "")
        sum += len(i)
    return sum / leng

caseOne = ["hello", "main"]
caseTwo = ["Peru", "France", "Nepal"]
caseThree = ["Computer Science", "Art"]
caseFour = ["one", "two"]

print(f"Words: {caseOne} Average = {averageLength(caseOne)}")
print(f"Words: {caseTwo} Average = {averageLength(caseTwo)}")
print(f"Words: {caseThree} Average = {averageLength(caseThree)}")
print(f"Words: {caseFour} Average = {averageLength(caseFour)}")