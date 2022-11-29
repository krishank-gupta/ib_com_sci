def count_letters(dict, msg):
    for letter in msg:
        if letter in dict.keys():
            dict[letter] += 1
    return dict

case1 = count_letters({
    'w': 0,
    'l': 0,
    'c': 0
}, 'hello world')
case2 = count_letters({
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}, 'Why did I choose CS')

print(case1)
print(case2)

# def count_letters(dict, msg):
#     for i in dict.keys():
#         dict[i] = msg.count(i)
#     return dict

# case1 = count_letters({
#     'w': 0,
#     'l': 0,
#     'c': 0
# }, 'hello world')
# case2 = count_letters({
#     'a': 0,
#     'e': 0,
#     'i': 0,
#     'o': 0,
#     'u': 0
# }, 'Why did I choose CS')

# print(case1)
# print(case2)