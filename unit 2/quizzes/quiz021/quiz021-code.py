def get_truth():
    print(f"| A | B | C | {'AB + notB + notB C'.center(20)} |")

    a = 1
    b = 1
    c = 1

    for i in range(0, 8, 1):         
     
        if i % 4 == 0:
            a = not a
            
        if i%2 == 0:
            b = not b
        
        c = i%2

        operator = (a and b) or (not b) or ((not b) and c)

        print(f"| {int(a)} | {int(b)} | {int(c)} | {str(int(operator)).center(20)} |")

get_truth()