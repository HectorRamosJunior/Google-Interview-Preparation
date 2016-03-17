"""Write a method that takes in 2 int arrays of any size and returns an 
array that calculates the sum of both. 

for example, [1,2,3] and [2,3,4] will return [3,5,7] 

Or [1,2,3] and [2,3,5,5] will return [2,4,7,8] 

However, if it's like [9,9,2] and [0,1,3] you need to carry the sum so it 
returns as [1,0,0,5] 

** SINGLE DIGIT ONLY

https://www.careercup.com/question?id=5631950045839360
"""

class LinkedList(object):
    def __init__(self):
        self.headNode = None
        self.tailNode = None

    def add(self, value):
        if not self.headNode:
            self.headNode = LinkedList.Node(value)
            self.tailNode = self.headNode
        else:
            self.tailNode.next = LinkedList.Node(value)
            self.tailNode = self.tailNode.next

    def reverseList(self):
        prevNode = None
        currentNode = self.headNode

        # The current headNode will be the future tailNode
        self.tailNode = self.headNode

        while currentNode:
            nextNode = currentNode.next

            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode

        self.headNode = prevNode

    def printList(self):
        currentNode = self.headNode
        outputList = []

        while currentNode:
            outputList.append(str(currentNode.value))
            currentNode = currentNode.next

        print "".join(outputList)

    class Node(object):
        def __init__(self, value, next = None):
            self.value = value
            self.next = next

def sumArraysLikeDigits(a1, a2):
    linkedLi = LinkedList()

    # Algorithm assumes a1 >= a2
    if len(a1) < len(a2):
        a1, a2 = a2, a1

    a1Length = len(a1)
    a2Length = len(a2)

    # 0 Being the LSB
    count = 0
    carry = 0

    while count < a1Length:
        # Iterate from LSB to MSB
        index = a1Length - 1 - count 

        # Handle if both arrays still have digits to add
        if count < a2Length:
            digitSum = a1[index] + a2[index] + carry
        # Handle if only a1 has digits to add
        else:
            digitSum = a1[index] + carry

        # Carry over any extra digits
        carry = digitSum / 10
        digitSum = digitSum % 10

        linkedLi.add(digitSum)
        
        count += 1

    if carry > 0:
        linkedLi.add(carry)

    # Current order of linked list is from LSB to MSB
    linkedLi.reverseList()
    linkedLi.printList()

a1 = [9,9,2]
a2 = [0,1,3]

print a1, a2
sumArraysLikeDigits(a1, a2) 