def to_roman(num):
    if num > 100:
        raise ValueError()
    
    roman_dict = [
        [100, 'C'],
        [90, 'XC'],
        [50, 'L'],
        [40, 'XL'],
        [10, 'X'],
        [9, 'IX'],
        [5, 'V'],
        [4, 'IV'],
        [1, 'I']
    ]

    output = ''

    while num > 0:
        for n,r in roman_dict:
            if n <= num:
                output += r
                num -= n
                break
        

    return output

print(to_roman(87))