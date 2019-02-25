class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None
        
    def insertLeft(self, newNode):
        if self.left != None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp
            
    def insertRight(self, newNode):
        if self.right != None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp
            
    def getRightChild(self):
        return self.right
    
    def getLeftChild(self):
        return self.left
    
    def setRootVal(self, newValue):
        self.key = newValue
        
    def getRootVal(self):
        return self.key
    
r = BinaryTree('a')
r.key
r.getRootVal()
r.insertLeft('b')
r.getLeftChild().getRootVal()
r.insertRight('c')
r.getRightChild().getRootVal()