"""Given an array of words (i.e. ["ABCW", "BAZ", "FOO", "BAR", "XTFN", "ABCDEF"])
find the max value of length(s) * length(t), where s and t are words from 
the array. The catch here is that the two words cannot share any characters. 

Assume that there are many words in the array (N words) and average length of 
word is M. 

Answer for the example above is "ABCW" and "XTFN" as the result is 4 * 4 = 12. 

"ABCW" and "ABCDEF" do not work since they share similar characters.

https://www.careercup.com/question?id=5113734827606016
"""
from sys import maxint

# Make a character hash set for each word, compare words in N^2 time.
# Assumes list contains strings with only capital english letters
def getMaxUniqueCombination(l):
    # Dictionary stores the character sets for each string in the list
    stringSetDict = {}
    
    for s in l:
        stringSetDict[s] = getCharSet(s)

    maxLengthCombination = -1 * maxint

    for i in xrange(len(l)):
        # Assumes strings only have all english capital letters
        if len(l[i]) > 26:
            continue

        for j in xrange(i + 1, len(l)):
            # Assumes strings only have all english capital letters
            if len(l[j]) > 26:
                continue

            # Compare the character hash sets of both strings to see if
            # They don't share any characters in common
            if setsUnique(stringSetDict[l[i]], stringSetDict[l[j]]):
                lengthCombination = len(l[i]) * len(l[j])

                if lengthCombination > maxLengthCombination:
                    maxLengthCombination = lengthCombination

    return maxLengthCombination

# Return character hash set for a given string
def getCharSet(s):
    charSet = set()

    for c in s:
        if c not in charSet:
            charSet.add(c)

    return charSet

# Return True if both sets have no keys in common
def setsUnique(s1, s2):
    # Code assumes s1 is the shorter set
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    for c in s1:
        if c in s2:
            return False

    return True

stringList = ["ABCW", "BAZ", "FOO", "BAR", "XTFN", "ABCDEF"]

print getMaxUniqueCombination(stringList)