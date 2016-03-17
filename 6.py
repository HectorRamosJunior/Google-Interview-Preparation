"""Find consecutive integers in a list that give you the biggest sum 

EX: Input: [-2, 5, -1, 7, -3] 
    Output: [5, -1, 7]

    20, -10, -8, -5, -2, 80, 5 = 

https://www.careercup.com/question?id=5764750370668544
"""
from sys import maxint

# Brute Force
def maxSumConsecutive(l):
    maxList = []
    maxSum = None
    
    currentIndex = 0

    while currentIndex < len(l):
        currentList = []
        currentSum = 0

        for i in xrange(currentIndex, len(l)):
            currentList.append(l[i])
            currentSum += l[i]

            if not maxList:
                maxList.append(l[i])
                maxSum = l[i]
            elif currentSum > maxSum:
                maxList = list(currentList)
                maxSum = currentSum

        currentIndex += 1

    return maxList


# Kadane's Algorithm
def maxSumConsecutive2(l):
    maxSum = -1 * maxint
    maxList = []

    currentSum = -1 * maxint
    currentList = []

    for i in xrange(len(l)):
        if l[i] > currentSum + l[i]:
            currentSum = l[i]
            currentList = [l[i]]
        else:
            currentSum += l[i]
            currentList.append(l[i])

        if currentSum > maxSum:
            maxSum = currentSum
            maxList = list(currentList)

    return maxList


array = [-2, 5, -1, 7, -3]
print maxSumConsecutive(array)
print maxSumConsecutive2(array)

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print maxSumConsecutive(array)
print maxSumConsecutive2(array)