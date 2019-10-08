class DirectedGraph:
    """Abstract base class for a directed graph.

    A functional directed graph class can be obtained by inheriting from 
    this class and overriding the methods has_edge and add_edge.  All other
    methods have default implementations, which may not be the most efficient.
    These other methods should also be overriden as appropriate to improve
    efficiency.
    """
    def __init__(self, num_vertices):
        """Constructs a directed graph with num_vertices vertices and zero edges"""
        self._num_vertices = num_vertices
    
    def has_edge(self, i, j):
        """Returns True if the graph contains the directed edge (i, j), False otherwise."""
        raise NotImplementedError
        
    def add_edge(self, i, j):
        """Adds the directed edge (i, j) to the graph."""
        raise NotImplementedError
        
    def out_edges(self, i):
        """Returns a list of directed edges outgoing from vertex i."""
        return [(i, j) for j in range(self._num_vertices) if self.has_edge(i, j)]
    
    def in_edges(self, j):
        """Returns a list of directed edges incoming to vertex j."""
        return [(i, j) for i in range(self._num_vertices) if self.has_edge(i, j)]
    
    def outdegree(self, i):
        """Returns the outdegree of vertex i."""
        return len(self.out_edges(i))
    
    def indegree(self, i):
        """Returns the indegree of vertex i."""
        return len(self.in_edges(i))
    
    def degree(self, i):
        """Returns the degree of vertex i."""
        return self.indegree(i) + self.outdegree(i)
        
    def add_edges(self, edges):
        """Adds all edges from a list to the graph."""
        for i, j in edges:
            self.add_edge(i, j)
            
    def num_vertices(self):
        """Returns the number of vertices in the graph."""
        return self._num_vertices

    def num_edges(self):
        """Returns the number of edges in the graph."""
        return len(tuple(self.edges()))
    
    def edges(self):
        """Returns an iterator over the edges of the graph."""
        for i in range(self._num_vertices):
            for edge in self.out_edges(i):
                yield edge
    
    def __str__(self):
        """Returns a string representation of the graph, so that it may be printed."""
        return "DirectedGraph with %d vertices and %d edge(s):\n%s" % (self.num_vertices(),
                                                                       self.num_edges(),
                                                                       sorted(self.edges()))
                                                            
class AdjacencyListDirectedGraph(DirectedGraph):
    def __init__(self, num_vertices):
        ### BEGIN SOLUTION
        super().__init__(num_vertices)
        self._out_lists = [[] for i in range(num_vertices)]
        self._in_lists = [[] for i in range(num_vertices)]
        ### END SOLUTION
    
    def add_edge(self, i, j):
        ### BEGIN SOLUTION
        self._out_lists[i].append(j)
        self._in_lists[j].append(i)
        ### END SOLUTION

    def remove_edge(self, i, j):
        self._out_lists[i].remove(j)
        self._in_lists[j].remove(i)
    
    def has_edge(self, i, j):
        ### BEGIN SOLUTION
        return j in self._out_lists[i]
        ### END SOLUTION
        
    def out_edges(self, i):
        ### BEGIN SOLUTION
        return [(i, j) for j in self._out_lists[i]]
        ### END SOLUTION
        
    def in_edges(self, j):
        ### BEGIN SOLUTION
        return [(i, j) for i in self._in_lists[j]]
        ### END SOLUTION
    
    def indegree(self, i):
        ### BEGIN SOLUTION
        return len(self._in_lists[i])
        ### END SOLUTION
        
    def outdegree(self, i):
        ### BEGIN SOLUTION
        return len(self._out_lists[i])
        ### END SOLUTION

    def isConnectedUtil(self, i):
        vertices_encountered = []
        vertices_encountered.append(i)

        stack = []
        stack.append(i)

        while len(stack) > 0:
            v = stack.pop()
            for t in self.out_edges(v):
                if t[1] not in vertices_encountered:
                    vertices_encountered.append(t[1])
                    stack.append(t[1])
        
        return len(vertices_encountered) == self._num_vertices

    def is_connected(self):
        for i in range(self._num_vertices):
            if self.isConnectedUtil(i) == True:
                return True
        return False

    def isCyclicUtil(self, v, visited, recStack): 
  
        # Mark current node as visited and  
        # adds to recursion stack 
        visited.append(v)
        recStack.append(v)
  
        # Recur for all neighbours 
        # if any neighbour is visited and in  
        # recStack then graph is cyclic 
        for t in self.out_edges(v):
            if t[1] not in visited:
                if self.isCyclicUtil(t[1], visited, recStack) == True: 
                    return True
            elif t[1] in recStack: 
                return True
  
        # The node needs to be poped from  
        # recursion stack before function ends 
        recStack.remove(v)
        return False

    def has_cycle(self):
        visited = []
        recStack = []

        for i in range(self._num_vertices):
            if i not in visited:
                if self.isCyclicUtil(i, visited, recStack) == True:
                    return True

        return False

if __name__ == '__main__':
    G = AdjacencyListDirectedGraph(4)
    G.add_edge(1,3)
    G.add_edge(3,2)
    G.add_edge(2,0)
    G.add_edge(3,0)
    print(G.is_connected())