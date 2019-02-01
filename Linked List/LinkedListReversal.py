'''Reversal of a singly Linked List'''

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None

def print_list(node):
    while node != None:
        print(node.value)
        node = node.next_node
        
def reverse(node):
    current = node
    next_pointer = None
    previous = None
    while current:
        next_pointer = current.next_node
        current.next_node = previous
        previous = current
        current = next_pointer
    return previous

a = Node('a')
b = Node('b')
c = Node('c')
a.next_node = b
b.next_node = c
print_list(a)
reverse(a)
print_list(c) 