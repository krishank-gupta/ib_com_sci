# Quiz 022: 22. Create a program that produces n random values from the equation below, where m and s are the other inputs of the function $(y = {x^{{-1 \over 2} * ({m \over s})^2}})$

I learnt about seed in this quiz. Seed initializes the start number of a random number generator. It can be used by importing random and then using random.seed(num) with num being the desired start of the random number generator. If we use the same seed twice, we get the same random number.

# Code: (remember to scroll)

https://github.com/krishank-gupta/ib_com_sci/blob/834ecd975f425d24ae39daaa66d39203255c8cbf/unit%202/quizzes/quiz022/quiz022-code.py#L1-L17

# Results

![quiz022-results](./quiz022-results.png)

# Proof

A (A+B) = A

| A | B | A+B | A (A+B) |
|:-:|:-:|:---:|:-------:|
| 0 | 0 |  0  |    0    |
| 0 | 1 |  1  |    0    |
| 1 | 0 |  1  |    1    |
| 1 | 1 |  1  |    1    |

A (A+B) is the same as A. Therefore, A and (A or B) = A proven.