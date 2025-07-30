## Implement a Graph in Python with Edges List

from collections import deque

class GraphUsingEdgeList:
    def __init__(self):
        self.V = []
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.V:
            self.V.append(vertex)
        else:
            print(f"{vertex} already exists")
        return             

    def add_edge(self, source, destination, weight=1):
        if source in self.V and destination in self.V:
            edge = (source, destination, weight)
            self.edges.append(edge)
        else:
            print("One or both the vertices are not found")
    def display(self):
        print("Vertices")
        for vertex in self.V:
            print(f"Vertex: {vertex}")
        print("Edges:")
        for source, destination, weight in self.edges:
            print(f"{source} ---> {destination}")


## Implement a Graph in Python with Adjacency List

class GraphUsingAdjacencyList:
    
    def __init__(self):
        self.V = []
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.V:
            self.V.append(vertex)
            self.adjacency_list[vertex] = []
        else:
            print(f"{vertex} already exists")
        return
    
    def add_edge(self, source, destination, weight=1):
        if source in self.V and destination in self.V:
            # Append the destination to the source's list and vice versa for undirected graph
            self.adjacency_list[source].append((destination, weight))
            self.adjacency_list[destination].append((source, weight))  # For undirected graph
        else:
            print("One or both the vertices are not found")
    
    def display(self):
        print("Vertices")
        for vertex in self.V:
            print(f"Vertex: {vertex}")
        print("Adjacency List:")
        ## Print each vertex and its neighbours
        for vertex, neighbour in self.adjacency_list.items():
            print(f"{vertex} ---> {neighbour}")
            
            
## Implement a Graph in Python with Adjacency Matrix
class GraphUsingAdjacencyMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [None] * num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_vertex(self, index, label): # index is the position in the vertices list and label is the name of the vertex
        if index >= 0 and index < self.num_vertices: # Ensure index is within bounds
            self.vertices[index] = label
        else:
            print(f"Index {index} is out of bounds")
        return

    def add_edge(self, source, destination, weight=1):
        if 0 <= source < self.num_vertices and 0 <= destination < self.num_vertices: # Ensure indices are within bounds
            self.adjacency_matrix[source][destination] = weight
            self.adjacency_matrix[destination][source] = weight  # For undirected graph
        else:
            print("One or both the vertices are not found")
    
    def display(self):
        print("Vertices:")
        for index, label in enumerate(self.vertices):
            if label is not None:
                print(f"Vertex Index: {index}, Label: {label}")

        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)
    ## Depth First Search (DFS) Traversal
    ## This method performs a DFS traversal starting from a given vertex
    ## It uses a helper method to recursively visit each vertex
    def dfs(self, start_vertex=0):
        dfs_result = []
        visited = [False] * self.num_vertices
        print("DFS Traversal starting from vertex:", start_vertex)
        self._dfs_helper(start_vertex, dfs_result, visited)
        print("\nDFS complete!!!")
        return dfs_result

    def _dfs_helper(self, vertex, dfs_result, visited):
        print(vertex, end=' ')
        visited[vertex] = True
        dfs_result.append(vertex)
        
        for neighbor in range(self.num_vertices):
            if vertex == neighbor:
                continue
            # Check if there is an edge between vertex and neighbor
            if self.adjacency_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                self._dfs_helper(neighbor, dfs_result, visited)
                
    ## Breadth First Search (BFS) Traversal
    ## This method performs a BFS traversal starting from a given vertex
    ## It uses a queue to keep track of the vertices to visit next
    def bfs(self, start_vertex=0):
        bfs_result = []
        visited = [False] * self.num_vertices
        queue = deque([start_vertex])
        visited[start_vertex] = True

        while len(queue) > 0:
            vertex = queue.popleft()
            print(vertex, end=' ')
            bfs_result.append(vertex)

            for neighbor in range(self.num_vertices):
                if vertex == neighbor: # Skip self-loops
                    continue
                # Check if there is an edge between vertex and neighbor
                if self.adjacency_matrix[vertex][neighbor] != 0 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        print("\nBFS complete!!!")
        return bfs_result
    
    ## Kruskal's Algorithm to find Minimum Spanning Tree (MST)
    def kruskal_mst(self):
        parent = list(range(self.num_vertices)) # Initialize parent for each vertex
        rank = [0] * self.num_vertices # Initialize rank for union-find

        def find(v):
            if parent[v] != v: # Path compression
                parent[v] = find(parent[v]) 
            return parent[v]

        def union(v1, v2): # Union by rank
            root1 = find(v1) # find root of v1
            root2 = find(v2) # find root of v2
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        edges = []
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.adjacency_matrix[i][j] != 0:
                    edges.append((self.adjacency_matrix[i][j], i, j))

        edges.sort()
        
        mst = []
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))
        
        return mst
    
    
    ## A*Star Algorithm to find the shortest path from start to goal
    def a_star(self, start, goal, heuristic):
        open_set = set([start])  # Set of nodes to be evaluated
        came_from = {}  # Dictionary to track the path (from where we reached each node)

        # Initialize cost values
        g_score = [float('inf')] * self.num_vertices  # Actual cost from start to each vertex
        f_score = [float('inf')] * self.num_vertices  # Estimated total cost (g + h)

        g_score[start] = 0  # Cost from start to start is 0
        f_score[start] = heuristic[start]  # f = g + h = 0 + heuristic at start

        while open_set:
            # Select node in open_set with the lowest f_score
            current = min(open_set, key=lambda x: f_score[x])

            # If the goal is reached, reconstruct and return the path
            if current == goal:
                return self._reconstruct_path(came_from, current)

            open_set.remove(current)

            # Check all neighbors of the current node
            for neighbor in range(self.num_vertices):
                if self.adjacency_matrix[current][neighbor] == 0:
                    continue  # No edge between current and neighbor

                # Calculate tentative g score
                tentative_g = g_score[current] + self.adjacency_matrix[current][neighbor]

                # If this path to neighbor is better than any previous one
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic[neighbor]
                    open_set.add(neighbor)

        return None  # No path was found
    
    def _reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        total_path.reverse()
        return total_path