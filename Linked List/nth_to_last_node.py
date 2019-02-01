''' The function 'nth_to_last_node' takes a head node and an integer value n and then returns the nth to last node in the linked list.'''
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next_node = None
        
def nth_to_last_node(n,node):
    left_pointer = node
    right_pointer = node
    for i in range(n-1):
        print(i)
        if not right_pointer.next_node:
            raise LookupError('Error: n is larger than the linked list')
        right_pointer = right_pointer.next_node
    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node
    return left_pointer