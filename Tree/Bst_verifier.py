class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
def treeMax(node):
    if node:
        maxLeft = treeMax(node.left)
        maxRight = treeMax(node.right)
        return max(node.key, maxLeft, maxRight)
    else:
        return float("-inf")
    
def treeMin(node):
    if node:
        minLeft = treeMin(node.left)
        minRight = treeMin(node.right)
        return min(node.key, minLeft, minRight)
    else:
        return float("inf")
    
def verify_bst(node):
    if not node:
        return True
    else:
        if (treeMax(node.left) <= node.key <= treeMin(node.right) and verify(node.left) and verify(node.right)):
            return True
        else:
            return False

root= Node(10, "Ten")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

print(verify(root)) # prints True, since this tree is valid

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(verify(root)) # prints False, since 15 is to the left of 10