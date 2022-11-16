# Random library to create random numbers
import random 
# Create a seed to initialize start of random numbers at 1234
random.seed(1234)

# function that takes in 3 parameters
def produce(n,m,s):

    # generate the random number between 0 and 100
    x = random.randint(0,100)

    # return solution based on description of quiz
    return (f"| {str(x).center(10)} | {(str(round(x ** ((1/2)*((m/s)**2)),2))).center(10)} |")

# output header
print(f"| {'x'.center(10)} | {'y(x)'.center(10)} |")
# output data
print(produce(5,3,2))
print(produce(5,3,2))
print(produce(5,3,2))
print(produce(5,3,2))
print(produce(5,3,2))