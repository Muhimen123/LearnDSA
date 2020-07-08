import collections

# Graph traversal using BFS(breadth first search)

graph = {
    'A' : ['B', 'C', 'F'],
    'B' : ['D', 'E', 'I', 'J'],
    'C' : ['D', 'F'],
    'D' : ['G', 'I'],
    'E' : ['B', 'F'],
    'F' : ['H', 'J'],
    'G' : ['D', 'H'],
    'H' : [],
    'I' : ['J'],
    'J' : ['A']
}

def bfs(graph, starting_node):
    visited = set()
    queue = collections.deque([starting_node])

    visited.add(starting_node)
    
    while queue:
        vertex = queue.popleft()
        print(f"Vsisited node {vertex}")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
bfs(graph, 'A')
