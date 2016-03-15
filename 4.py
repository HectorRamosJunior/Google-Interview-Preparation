"""Given a specific type of DAG that forms a pyramid (the links have up down 
direction), in which the node values are integer, find the path that has the 
maximum sum of node values. What is the time/space complexity of this algorithm?

e.g: 
            3 
           / \ 
          9   4 
         / \ / \ 
        1   8   2 
       / \ / \ / \ 
      4   5   8   2 
answer: <3,9,8,8>, sum = 3+9+8+8=28

https://www.careercup.com/question?id=5732736959512576
"""

class Node(object):
    def __init__(self, data, left = None, right = None):
        self.data = data 
        self.left = left
        self.right = right

def maxSumNodes(root):
    if not root:
        return None

    left = maxSumNodes(root.left)
    if left:
        left.insert(0, root.data)

    right = maxSumNodes(root.right)        
    if right:
        right.insert(0, root.data)

    if not (left and right):
        return [root.data]
    elif left and right:
        if sum(left) > sum(right):
            return left
        else:
            return right
    elif left:
        return left
    elif right:
        return right

n1 = Node(3); n2 = Node(9); n3 = Node(4)
n4 = Node(1); n5 = Node(8); n6 = Node(2)
n7 = Node(4); n8 = Node(5); n9 = Node(8); n10 = Node(2)

n1.left = n2; n1.right = n3
n2.left = n4; n2.right = n5; n3.left = n5; n3.right = n6
n4.left = n7; n4.right = n8; n5.left = n8; n5.right = n9; n6.left = n9; n6.right = n10


print maxSumNodes(n1)
