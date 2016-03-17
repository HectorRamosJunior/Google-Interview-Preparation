"""You are given a function bool rand_bit_p() that returns true with some 
unknown probability p and false with probability 1 - p. 

Write function rand_bit() using rand_bit_p that will return true and 
false with equal probability (that is, implement a fair coin, given unfair coin)

https://www.careercup.com/question?id=5678403979051008
"""
from random import randint 

def rand_bit_p():
    probabilityTrue = 75

    r = randint(1,100)

    if r >= 100 - probabilityTrue:
        return True
    else:
        return False

def rand_bit():
    bit1 = rand_bit_p()
    bit2 = rand_bit_p()

    # Implement XOR for loop condition
    while not (bit1 != bit2):
        bit1 = rand_bit_p()
        bit2 = rand_bit_p()

    # Both have the same chance of coming up the unfair side
    # So use that to restore fairness
    if bit1 and not bit2:
        return True
    elif not bit1 and bit2:
        return False


answerList = []
for x in xrange(10):
    answerList.append(rand_bit())

print answerList


