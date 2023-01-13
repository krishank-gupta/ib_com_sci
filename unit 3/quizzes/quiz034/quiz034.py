roman_dict = {
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I'
}

def to_roman(num):
    num = int(num)
    output = ''

    while num > 0:
        for i in roman_dict:
            if num - i >= 0:
                output += roman_dict[i]
                num -= i
        # if num - 100 >= 0:
        #     output += roman_dict[100]
        #     num -= 100
        # elif num - 50 >= 0:
        #     output += roman_dict[50]
        #     num -= 50
        # elif num - 10 >= 0:
        #     output += roman_dict[10]
        #     num -= 10
        # elif num - 5 >= 0:
        #     output += roman_dict[5]
        #     num -= 5
        # elif num - 1 >= 0:
        #     output += roman_dict[1]
        #     num -= 1

    if num > 100:
        raise ValueError("Error. Maximum Value 100")
    else:
        return output

print(to_roman(1))
print(to_roman(5))
print(to_roman(10))
print(to_roman(20))
print(to_roman(80))
print(to_roman(90))
