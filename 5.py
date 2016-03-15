"""Define a function that can detect whether the characters of a string can
be shuffled without repeating the same characters as one other's neighbors.
EX:

apple >> alpep, so valid 
a >> a, valid 
aa >> aa, invalid/impossible 
aab >> aba, valid 
aaaabbcc >> acabacab, valid 
etc. 
You do not have to find one representation, just have to detect if it is 
possible or not!

https://www.careercup.com/question?id=5681030989086720
"""

def shuffleable(s):
    charDict = {}
    length = len(s)

    for c in s:
        if c not in charDict:
            charDict[c] = 1
        else:
            charDict[c] += 1

            if length % 2 == 0 and charDict[c] > length / 2:
                return False
            elif length % 2 == 1 and charDict[c] > (length / 2 + 1):
                return False

    return True

s1 = "apple"
s2 = "a" 
s3 = "aa"
s4 = "aab"
s5 = "aaaabbcc"

print shuffleable(s1)
print shuffleable(s2)
print shuffleable(s3)
print shuffleable(s4)
print shuffleable(s5)