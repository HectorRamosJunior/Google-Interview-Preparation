"""Write the function READ, which is passed two double pointers pointing 
to the head pointers of two linked lists. 

One list will hold even integers, the other one will hold odd integers. 
READ reads a series of integers. It separates odd integers to the 
first list, and even ones to the second, all in sorted order.

https://www.careercup.com/question?id=5655354869284864
"""
from random import shuffle

class BST(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        nodeToAdd = BST.Node(value)

        if not self.root:
            self.root = nodeToAdd
        else:
            currentNode = self.root

            while currentNode:
                if value > currentNode.value:
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = nodeToAdd
                        break
                elif value <= currentNode.value:
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = nodeToAdd
                        break

    class Node(object):
        def __init__(self, value, left = None, right = None):
            self.value = value
            self.left = left 
            self.right = right


    def convertToList(self):
        outputList = []

        BST.__convertToList(self.root, outputList)

        return outputList

    @staticmethod
    def __convertToList(root, outputList):
        if not root:
            return None

        BST.__convertToList(root.left, outputList)

        outputList.append(root.value)

        BST.__convertToList(root.right, outputList)


# This function first puts the input list into even and odd BST's.
# This is to save runtime by making insertions O(n) instead of O(n^2)
# It then returns the BST's to lists and returns both odd and even lists
def seperateEvensOdds(inputList):
    oddBST = BST()
    evenBST = BST()

    while inputList:
        value = inputList.pop(0)

        if value % 2 == 0:
            evenBST.add(value)
        elif value % 2 == 1:
            oddBST.add(value)

    evenList = evenBST.convertToList()
    oddList = oddBST.convertToList()

    return evenList, oddList


inputList = range(20)
shuffle(inputList)
print inputList

evenList, oddList = seperateEvensOdds(inputList)

print evenList
print oddList
