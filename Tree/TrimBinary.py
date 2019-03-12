class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def TrimBinary(node, minValue, maxValue):
    
    if not node:
        return 
    else:
        left_subtree = TrimBinary(node.left, minValue, maxValue)
        right_subtree = TrimBinary(node.right, minValue, maxValue)
        
        if minValue <= node.value <= maxValue:
            return node
        elif minValue > node.value:
            return right_subtree
        else:
            return left_subtree

root = Node(1)
a = Node(2)
b = Node(3)
root.left = a
root.right = b
node = TrimBinary(root, 2,10)