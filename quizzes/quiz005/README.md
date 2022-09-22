# Quiz 005

```.py

# Initialize variables
# Get input number to find the factors
num = input("Enter a number to find the factors: ")

# factors is a list. It contains 1 since 1 is a factor of every number. If num has factors, they will be added to this list
factors = [1]

# To find sum of the factors. It's one since current sum is 1
sum = 1

# Iterator to find the numbers. Begins at 2 because 1 is already written as a factor.
i = 2

# Check if input is a number 
if not num.isdigit():
  num = input('Please enter a numeric value: ')

num = int(num)

# Run through all numbers smaller than half of num 
while i <= num/2:
  # Check if i is a factor
  if num % i == 0:
    # If yes than add to factors list
    factors.append(i)

    # Add i to sum
    sum += i

  # Increment i
  i += 1

# If only 1 is in the factors list, print number is prime
if(sum == 1):
  print(f"{num} has no factors. It is a prime number")
# If sum is equal to the number, print num is perfect
elif sum == num:
  print(f"{num} has the factors: {factors}. The number is a perfect number.")
# Show factors list, print not perfect
else:
  print(f"{num} has the factors: {factors}. The number is not a perfect number.")


```

Here are the results of the test case. CGATAGCTAGCTGATCGATCGATCGGTCAGTCGAT

![quiz003-results](./quiz003-results.png)
