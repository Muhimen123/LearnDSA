class Graph:
    def __init__(self, nodes):
        self.graph = {}
        
        # Initializing the graph
        for node in nodes:
            self.graph[node] = []

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Both are the same vertex")
        else:

            # If there is no vertex then create one
            if v1 not in self.graph:
                self.graph[v1] = []
            if v2 not in self.graph:
                self.graph[v2] = []

            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("Missing vertex", v1, "or", v2)
        else:
            self.graph[v2].remove(v1)
            self.graph[v1].remove(v2)

    def show_graph(self):
        for node in self.graph:
            print(node, '-->', self.graph[node])


# Driver code
my_graph = Graph(['A', 'B', 'D', 'E'])

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'C')
my_graph.add_edge('D', 'E')

print("Before deleting something\n\n")
my_graph.show_graph()
print()

my_graph.remove_edge('A', 'B')
my_graph.remove_edge('D', 'E')
my_graph.remove_edge('F', 'G')

print("After removing something\n\n")
my_graph.show_graph()
print()
