roman_dict = {
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I'
}

def to_roman(num):
    num = int(num)
    output = ''

    i = roman_dict
    while num > 0:
        
        if num - i >= 0:
            output += roman_dict[i]
            num -= i
        i += 1
    
    if num > 100:
        raise ValueError("Error. Maximum Value 100")

    return output


print(to_roman(1))
print(to_roman(10))
print(to_roman(60))
print(to_roman(70))