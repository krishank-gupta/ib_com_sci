# Function that takes in dict of alphabets and the message
def count_letters(dict, msg):
    # For every letter in the message
    for letter in msg:
        # If the letter is a key in the dictionary, increase the value of the key by 1
        if letter in dict.keys():
            dict[letter] += 1
    # Return the dictionary
    return dict

# Test case 1
case1 = count_letters({
    'w': 0,
    'l': 0,
    'c': 0
}, 'hello world')

# Test case 2
case2 = count_letters({
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}, 'Why did I choose CS')

# Print test cases
print(case1)
print(case2)
