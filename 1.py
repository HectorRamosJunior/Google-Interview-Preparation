"""Given an arbitrary tree starting at 'root' where each node contains a 
pair of values (x, y), write a boolean function find(Node root, int x, int y) 
that returns true iff:
* x is equal to a value "x" of any node n1 in the tree 
* and y is equal to a value "y" of any node n2 in the tree 
* and both n1 and n2 are at the same level in the tree 

boolean find(Node root, int x, int y) 

Example: 

(1,120) 
/ | \ 
/ | \ 
/ | \ 
(5,15) (30,70) (80,110) 
/ | \ | 
/ | \ | 
/ | \ | 
(35, 40) (45,50) (55, 65) (90, 100) 

boo == true 
find(root, 45, 100) == true 
find(root, 30, 100) == false 
find(root, 30, 70) == true 
find(root, 70, 30) == false

https://www.careercup.com/question?id=5691211923849216
"""

class Node(object):
    def __init__(self, x, y, edges = []):
        self.x = x
        self.y = y
        self.edges = edges

def find(root, x, y):
    currentDepthCount = 1
    nextDepthCount = 0
    q = [root]

    # BFS search through the tree
    while q:
        xFound = False 
        yFound = False

        # Extra while loop to seperate depth levels
        while currentDepthCount > 0:
            node = q.pop(0)

            if node.x == x:
                xFound = True
            if node.y == y:
                yFound = True

            # Handle if both values found on current depth
            if xFound and yFound:
                return True

            for n in node.edges:
                q.append(n)
                nextDepthCount += 1

            currentDepthCount -= 1

        # Swap depth counters for the next depth loop iteration
        currentDepthCount = nextDepthCount
        nextDepthCount = 0

    return False

n1 = Node(1, 120)
n2 = Node(5, 15); n3 = Node(30, 70); n4 = Node(80, 110)
n5 = Node(35, 40); n6 = Node(45, 100); n7 = Node(55, 65); n8 = Node(90, 100)

n1.edges = [n2, n3, n4]
n2.edges = [n5, n6, n7]
n3.edges = [n8]

print find(n1, 45, 100)
print find(n1, 30, 100)
print find(n1, 30, 70)
print find(n1, 70, 30)