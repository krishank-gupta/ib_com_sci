from library.library import hashLine,centerVal,colorCodes as cc

def signup(username, pswd):
    with open("credentials.csv", 'a') as f:
        f.write('\n')
        f.write(username + ',')
        f.write(pswd)
    f.close()

def login(username, pswd):
    with open("credentials.csv", 'r') as f:
        database = f.readlines()
        for line in database:
            stored_username, stored_pswd = line.strip().split(',')
            
            if username == stored_username and pswd == stored_pswd:
                return True

    f.close()

    print(f"{cc['red']}Username and password don't match!{cc['end_code']}")
    return False