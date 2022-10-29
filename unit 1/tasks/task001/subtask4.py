from subtask1 import lockerColors, colors

names = ["Gupta", "Krishank", "Doe", "John", 'World', 'Hello']

for i in range(0,len(names),2):
    lastName = names[i]
    firstName = names[i + 1]
    email = f"{firstName}.{lastName}@uwcisak.jp"
    locker = str(int(i/2)+1)

    print(lastName)
    print(firstName)
    print(email)
    print(locker)

    with open("lockerData.csv", 'a') as f:
        f.write('\n')
        f.write(lastName + ',')
        f.write(firstName + ',')
        f.write(email + ',')
        f.write(locker)
    f.close()
