from library.library import hashLine,centerVal,colorCodes as cc

def signup(username, pswd):
    with open("credentials.csv", 'w') as f:
        f.write(username + '\n')
        f.write(pswd)
    f.close()

def login(username, pswd):
    with open("credentials.csv", 'r') as f:
        stored_username, stored_pswd = f.read().split('\n')
    f.close()

    if username == stored_username and pswd == stored_pswd:
        return True
    else:
        print(f"{cc['red']}Username and password don't match!{cc['end_code']}")
    