class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        
    def addNeighbour(self, neighbour, weight):
        self.connectedTo[neighbour] = weight
        
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getWeight(self, n):
        return self.connectedTo[n]
    
    def __str__(self):
        return str(self.id) + "connected to " + str([x.id for x in self.connectedTo.keys()])
    
class Graph:
    
    def __init__(self):
        self.verticesList = {}
        self.noOfVertices = 0
        
    def addVertex(self,key):
        self.noOfVertices += 1
        self.verticesList[key] = Vertex(key)
        return self.verticesList[key]
    
    def getVertex(self, n):
        if n in self.verticesList:
            return self.verticesList[n]
        else:
            return None
        
    def addEdge(self, fromVertex, toVertex, weight):
        if fromVertex not in self.verticesList:
            self.addVertex(fromVertex)
        if toVertex not in self.verticesList:
            self.verticesList(toVertex)
        self.verticesList[fromVertex].addNeighbour(self.verticesList[toVertex], weight)
        
    def getVertices(self):
        return self.verticesList.keys()
    
    def __contains__(self, n):
        return n in self.verticesList
    
    def __iter__(self):
        return iter(self.verticesList.values())
    
g = Graph()
for i in range(6):
    g.addVertex(i)
    
g.getVertices()
g.addEdge(0,1,5)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())