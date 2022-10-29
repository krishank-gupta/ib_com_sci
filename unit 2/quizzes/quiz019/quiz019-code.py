def get_l3tt3r(msg):
    syntax = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        " ": "_"
    }
    output = ""
    for i in msg:
        if i in syntax:
            output += (str(syntax[i]))
        else:
            output += (str(i))
    return output

case1 = ("Hello World")
case2 = ("Why did I choose CS")
case3 = ("Remember the Figure Caption")

print(f"Case: {case1}. output: {get_l3tt3r(case1)}")
print(f"Case: {case2}. output: {get_l3tt3r(case2)}")
print(f"Case: {case3}. output: {get_l3tt3r(case3)}")