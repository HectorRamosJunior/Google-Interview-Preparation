"""Given an input BST, find the minimum value difference between
any two nodes in the tree.

EX:
  10
5   16
   12 20
      17 28
answer: 2 (12 and 10)

Describe the test cases you would use here?

https://www.careercup.com/question?id=5692398626668544
"""

class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def minDifference(root):
    if not root:
        return None

    global prevNode
    global minDiff

    minDifference(root.left)

    if prevNode:
        localDiff = root.value - prevNode.value

        if minDiff == None or minDiff > localDiff:
            minDiff = localDiff

    prevNode = root

    minDifference(root.right)


prevNode = None
minDiff = None

root = Node(10, 
                Node(8),
                Node(16,
                        Node(13), Node(20))
          )

minDifference(root)
print minDiff