def division(a,b):
    
    if not isinstance(a, int) or not isinstance(b,int): 
        raise TypeError("Error. Inputs must be integers")
    
    if b == 0:    
        raise ValueError("Error. Cannot divide by zero")
    
    return a/b