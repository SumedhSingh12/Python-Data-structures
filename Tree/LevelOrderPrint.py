import collections

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def level_order_print(node):
    if node == None:
        return
    else:
        current_count, next_count = 1,0
        nodes = collections.deque([node])
        while len(nodes) != 0:
            currentNode = nodes.pop()
            current_count -= 1
            print(currentNode.val, end =" ")
            
            if currentNode.left:
                nodes.append(currentNode.left)
                next_count += 1
            if currentNode.right:
                nodes.append(currentNode.right)
                next_count += 1
            if current_count == 0:
                print("\n")
                current_count, next_count = next_count, current_count

root = Node(1)
a = Node(2)
b = Node(3)
root.left = a
root.right = b
level_order_print(root)
