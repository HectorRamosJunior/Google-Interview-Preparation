"""Find the n-th smallest multiple given a set of numbers. 
For example, set = {4, 6}, n = 6: 

The sequence is:

4, 6, 8, 12, 16, 18, etc... 

Answer is 18

https://www.careercup.com/question?id=5686055997014016
"""

# Assumes n > 0
def findNthMultiple(number1, number2, n):
    multipleList = []

    number1Multiplier = 1
    number2Multiplier = 1
    count = 0

    while count < n:
        if number1Multiplier <= number2Multiplier:
            result = number1 * number1Multiplier
            number1Multiplier += 1
        else:
            result = number2 * number2Multiplier
            number2Multiplier += 1

        count += 1

    return result 


print findNthMultiple(4, 6, 6)

