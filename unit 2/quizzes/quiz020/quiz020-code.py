def get_truth():
    print("| A | B | C |")

    a = 1
    b = 1
    c = 1

    for i in range(0, 8, 1):         
        if i % 4 == 0:
            a = not a
            
        if i%2 == 0:
            b = not b
        
        c = i%2
    
        print(f"| {int(a)} | {int(b)} | {int(c)} |")

get_truth()