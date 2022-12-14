class graph:
    def __init__(self):
        self.al = {}

    def add_vertex(self, vertex):
        self.al[vertex] = set()

    def connect(self, v1, v2):
        self.al[v1].add(v2)
        self.al[v2].add(v1)

    def addAdjacencyList(self, _al):
        for i in range(len(_al)):
            self.add_vertex(i)
            for j in _al[i] :
                if i != j:
                    self.al[i].add(j)

    def addAdjacencyMatrix(self, _am):
        for i in range(len(_am)):
            self.add_vertex(i)
            for j in range(len(_am[i])):
                if(_am[i][j] == 1 ):
                    self.al[i].add(j)

    def isConneted(self, v1, v2):
        if (v2 in self.al[v1] or v1 in self.al[v2]):
            print("is Connected")
        else:
            print("not Connected")
                

    def bfs(self,start):
        visited = []
        visited.append(start)
        for i in sorted(self.al[start]):
            visited.append(i)
        for i in visited:
            for j in sorted(self.al[i]):
                if j not in visited:
                    visited.append(j)
        print(visited)

    def dfs(self, start, visited = None):
        if visited == None:
            visited = []
        visited.append(start)
        for i in sorted(self.al[start]):
            if i not in visited:
                self.dfs(i,visited)
        return visited


    def printGraph(self):
        print(self.al)

_graph = graph()
_graph.add_vertex("a")
_graph.add_vertex("b")
_graph.add_vertex("c")
_graph.add_vertex("d")
_graph.connect("a","b")
_graph.connect("b","c")
_graph.connect("c", "a")
_graph.connect("d","b")

# _list = [
#     [1,2],  #0
#     [0,3],    #1
#     [0,3],   #2
#     [4,1,2],   #3
#     [3,5],   #4
#     [4]   #5
# ]

# _graph.addAdjacencyList(_list)

# _matrix = [
#     [0,1,1,0,1],
#     [1,0,0,0,1],
#     [1,0,1,0,0],
#     [0,0,0,1,0],
#     [0,0,0,0,1],
# ]

# _graph.addAdjacencyMatrix(_matrix)

_graph.bfs("b")
print(_graph.dfs("b"))

# _graph.printGraph()

# DFS algorithm in Python

            
