class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}                   #{key=id, value=weight}
        
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
        self.verticesList = {}              #{key=Vertex(), value=id}
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
        
    def addEdge(self, fromVertex, toVertex, weight=0):
        if fromVertex not in self.verticesList:
            self.addVertex(fromVertex)
        if toVertex not in self.verticesList:
            self.addVertex(toVertex)
        self.verticesList[fromVertex].addNeighbour(self.verticesList[toVertex], weight)
        
    def getVertices(self):
        return self.verticesList.keys()
    
    def __contains__(self, n):
        return n in self.verticesList
    
    def __iter__(self):
        return iter(self.verticesList.values())

def word_ladder(word_list):
    g = Graph()
    d = {}
    for word in word_list:
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for key in d.keys():
        for i in range(1, len(d[key])):
            g.addEdge(d[key][0],d[key][i], 0)
    return g

g = word_ladder(["pope", "rope","sage","best","ripe","pipe"])
print(g.verticesList['pope'])
print(g.verticesList['rope'])