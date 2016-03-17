"""How many Fibonacci numbers exists less than a given number n.
Can you make a function in terms of n , to get the number of 
fibonacci numbers less than n. 

Example : n = 6 
Answer: 6 as (0, 1, 1, 2, 3, 5)

https://www.careercup.com/question?id=5713892824055808
"""

def getFibCount(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev = 0
    current = 1

    count = 2

    while prev + current < n:
        count += 1
        
        temp = prev
        prev = current
        current += temp

    return count

print getFibCount(6)
print getFibCount(1000)
print getFibCount(1000000)
