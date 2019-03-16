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