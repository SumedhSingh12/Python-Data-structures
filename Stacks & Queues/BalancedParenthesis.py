class Stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
        
    def size(self):
        return len(self.items)

stack = Stack()

def balance_check(s):
    
    if len(s) % 2 != 0 or len(s) == 0:
        return False
    
    opening = set('({[')
    pair_set = set([('(',')'), ('{','}'), ('[',']')])
    
    for parenthesis in s:
        
        if parenthesis in opening:
            stack.push(parenthesis)
        else:
            if stack.size() == 0:
                False
            last_open = stack.pop()
            
            if (last_open, parenthesis) not in pair_set:
                return False
    return stack.size() == 0

balance_check('{([]({}))}')