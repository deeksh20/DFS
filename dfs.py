class Graph:
    def __init__(self):
        self.graph = {}

  
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, v, visited):

        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

   
    def dfs(self, start_vertex):
        visited = set()  
        self.dfs_util(start_vertex, visited)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    print("Depth First Search starting from vertex 0:")
    g.dfs(0)