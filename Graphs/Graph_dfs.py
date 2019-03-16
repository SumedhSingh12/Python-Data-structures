graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs_iter(graph, start):
    stack = [start]
    visited = set()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
print(dfs_iter(graph, 'A'))

def dfs_recursive(graph,start, visited=None):
    if visited is None:
        visited = set()
    for nxt in graph[start] - visited:
        visited.add(nxt)
        dfs_recursive(graph, nxt, visited)
    return visited
print(dfs_recursive(graph, 'A'))

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal :
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))
list(dfs_path(graph,'A','F'))