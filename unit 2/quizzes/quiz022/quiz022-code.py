import random 
random.seed(1234)

def produce(n,m,s):
    n = int(n)
    m = int(m)
    s = int(s)
    x = random.randint(0,100)

    return (f"| {str(x).center(10)} | {(str(round(x ** ((1/2)*((m/s)**2)),2))).center(10)} |")

print(f"| {'x'.center(10)} | {'y(x)'.center(10)} |")
print(produce(5,3,2))
print(produce(5,3,2))
print(produce(5,3,2))
print(produce(5,3,2))
print(produce(5,3,2))