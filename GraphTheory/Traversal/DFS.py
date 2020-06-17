def dfs(graph, visited, node): #Implementation of DFS using recursion
    if node not in visited:
        print("Visited node:", node)
        visited.add(node)
        for neighbours in graph[node]:
            dfs(graph, visited, neighbours)
# Just a simple directional graph
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
visited = set()
first_node = 'D'
dfs(graph, visited, first_node)
