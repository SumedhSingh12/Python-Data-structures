'''Returns a boolean value indicating if the singly linked list contains a cycle.
A cycle is present when a node actually points back to a previous node in the list. Also known as curcularly linked list. '''

class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

def cycle_check(node):
    marker1, marker2 = node, node
    while marker2 != None and marker2.nextnode != None:
        marker2 = marker2.nextnode
        if marker2 == marker1:
            return True
        marker2 = marker2.nextnode
        marker1 = marker1.nextnode
    return False

# CREATE A CYCLIC LIST
a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
c.nextnode = a
cycle_check(a)
