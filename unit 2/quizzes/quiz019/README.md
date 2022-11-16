# Quiz 019: Create a function that changes the vowels in a string to numbers such as a=4,e=3,i=1,o=0 and space by _. [HL] Libraries or methods not allowed for this quiz. You can use dictionaries. Create a Boolean circuit for: AB + not(B+C) + B(notC notA)

Since we were not allowed to use the replace method, I created a dictionary with all the key value pairs. I then used a loop for each character and checked to see if character is a key in the dictionary. If it is then change that position to the value of that key. If not then no changes.

# Code: (remember to scroll)

https://github.com/krishank-gupta/ib_com_sci/blob/97b000adbca4756a294bb20c49120ae43b00b0ea/unit%202/quizzes/quiz019/quiz019-code.py#L1-L36
# Results

![quiz019-results](./quiz019-results.png)

# Boolean Circuit

AB + not(B+C) + B(notC notA)

![quiz019-boolean-circuit](./quiz019-boolean-circuit.png)