# digits = input("Enter the digits: ").split(" ")
digits = ["s1","s2","s3"]
exp = f"{digits[0]} and {digits[1]}"
def get_truth():
    print(f"| {digits[0].center(10)} | {digits[1].center(10)} | {digits[2].center(10)} |")

    a = 1
    b = 1
    c = 1

    for i in range(0, 8, 1):         
        if i % 4 == 0:
            a = not a
            
        if i%2 == 0:
            b = not b
        
        c = i%2
    
        print(f"| {str(int(a)).center(10)} | {str(int(b)).center(10)} | {str(int(c)).center(10)} |")

    print(exp)
    print(exp.split(" "))
    

get_truth()