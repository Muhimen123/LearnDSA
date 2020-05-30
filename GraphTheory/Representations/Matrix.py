class Graph:
    # Initializing the graph
    def __init__(self, size):
        self.Matrix = []
        for _ in range(size):
            self.tmp = [0] * size
            self.Matrix.append(self.tmp)
    # Adding vertex into the graph
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Both of them are the same")
        else:
            v1 -= 1
            v2 -= 1
            self.Matrix[v2][v1] = 1
            self.Matrix[v1][v2] = 1
    # Deleting vertex from the graph
    def delete_edge(self, v1, v2):
        if self.Matrix[v2-1][v1-1] == 0:
            print("The is no vertex to delete")
        else:
            v1 -= 1
            v2 -= 1
            self.Matrix[v2][v1] = 0
            self.Matrix[v1][v2] = 0
    # Printing out the vertex
    def show_graph(self):
        for self.row in self.Matrix:
            print(self.row)

#Driver code
my_graph = Graph(10)
my_graph.add_edge(5, 6)
my_graph.add_edge(1, 8)
my_graph.add_edge(1, 9)
my_graph.add_edge(1, 7)
my_graph.add_edge(9, 8)

print("Before deleting something\n")
my_graph.show_graph()

my_graph.delete_edge(2, 8)
my_graph.delete_edge(5, 6)
my_graph.delete_edge(1, 7)

print("After deleting something\n")
my_graph.show_graph()
