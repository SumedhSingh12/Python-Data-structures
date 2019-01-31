class DoublyLinkedList(object):
    """docstring for Node"""
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.previous = a

b.next = c
c.previous = b

print(a.value)
print(a.next.value)


print(b.value)
print(b.next.value)
print(b.previous.value)

print(c.value)
print(c.previous.value)
print(c.previous.previous.value)
