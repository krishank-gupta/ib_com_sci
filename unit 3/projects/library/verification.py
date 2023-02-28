def email_verify(email):
    if not email or not email.count('@') == 1:
        return False

    else:            
        name, domain = email.split('@')
        if not name or not domain.count('.') == 1:
            return False
        elif len(domain.split('.')[1]) == 0:
            return False
        else: 
            return True

def str_input_verify(str):
    if not str:
        return False
    else:
        return True

def pswds_verify(pswd1, pswd2):
    if pswd1 != pswd2 or not pswd1 or not pswd2:
        return False
    else:
        return True