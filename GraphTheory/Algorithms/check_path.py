# This program checks is there exists any path between two nodes.
# It's using DFS to look for available paths
# Keep in mind, we are not looking for the shortest path here.
# The only thing matters is the existence of the path
# This is a one directional graph

def dfs(graph, visited, starting_node, ending_node):
    ans = False
    if starting_node not in visited:
        visited.add(starting_node)
        for neighbours in graph[starting_node]:
            dfs(graph, visited, neighbours, ending_node)
    if ending_node in visited:
        ans = True
    return ans
    
graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['I', 'J'],
        'D': [],
        'E': [],
        'F': ['J'],
        'G': ['M'],
        'H': [],
        'I': ['D'],
        'J': ['K', 'M'],
        'K': [],
        'L': [],
        'M': []
        }

visited = set()
starting_node = 'A'
ending_node = 'B'
path = dfs(graph, visited, starting_node, ending_node)
print(path)

visited = set()
starting_node = 'A'
ending_node = 'K'
path = dfs(graph, visited, starting_node, ending_node)
print(path)

visited = set()
starting_node = 'D'
ending_node = 'A'
path = dfs(graph, visited, starting_node, ending_node)
print(path)
