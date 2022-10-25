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

print(averageLength(caseOne))
print(averageLength(caseTwo))
print(averageLength(caseThree))
print(averageLength(caseFour))