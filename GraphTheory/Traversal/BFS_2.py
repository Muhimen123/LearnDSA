# Graph traversal with BFS.
# Graph representation: Adjacency Matrix

graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]

def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(f"Visited node: {node}")
        visited.add(node)

        for i in range(len(graph)):
            if graph[i][node] == 1 and i not in visited:
                queue.append(i)

bfs(graph, 0)
