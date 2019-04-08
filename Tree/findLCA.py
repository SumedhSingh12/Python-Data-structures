class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findLCA(root, n, m):
    if root == None:
        return None
    elif root.value == n or root.value == m:
        return root
    left_lca = findLCA(root.left, n, m)
    right_lca = findLCA(root.right, n, m)
    if left_lca and right_lca:
        return root
    if left_lca:
        return left_lca
    else:
        return right_lca

  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
print("LCA(4,5) = ", findLCA(root, 4, 5).value )
