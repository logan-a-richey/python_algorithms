# graphing_algorithms.py

import heapq
from collections import defaultdict, deque

class GraphAlgorithms:
    """
    ### Graph Algorithms:
    1. Dijkstra's Algorithm
    2. Bellman-Ford Algorithm
    3. A* Algorithm
    4. Floyd-Warshall Algorithm
    5. Kruskal's Algorithm
    6. Prim's Algorithm
    7. Topological Sort
    8. Tarjan's Algorithm
    """

    @staticmethod
    def dijkstra(graph, start):
        """Performs Dijkstra's Algorithm to find the shortest paths from the start node."""
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

    @staticmethod
    def bellman_ford(graph, start):
        """Performs Bellman-Ford Algorithm to find the shortest paths from the start node."""
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        for _ in range(len(graph) - 1):
            for node in graph:
                for neighbor, weight in graph[node]:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight
        return distances

    @staticmethod
    def a_star(graph, start, goal, heuristic):
        """Performs A* Algorithm for pathfinding from start to goal node using heuristic."""
        open_list = []
        heapq.heappush(open_list, (0 + heuristic[start], 0, start))
        g_costs = {start: 0}
        f_costs = {start: heuristic[start]}
        came_from = {}
        
        while open_list:
            _, g, current = heapq.heappop(open_list)
            
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]  # reverse path
            
            for neighbor, weight in graph[current]:
                tentative_g = g + weight
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    f_costs[neighbor] = tentative_g + heuristic.get(neighbor, 0)
                    came_from[neighbor] = current
                    heapq.heappush(open_list, (f_costs[neighbor], tentative_g, neighbor))
        
        return []  # return empty list if no path found

    @staticmethod
    def floyd_warshall(graph):
        """Performs Floyd-Warshall Algorithm to find the shortest paths between all pairs of nodes."""
        nodes = list(graph.keys())
        dist = {node: {neighbor: float('inf') for neighbor in nodes} for node in nodes}

        for node in nodes:
            dist[node][node] = 0

        for node in graph:
            for neighbor, weight in graph[node]:
                dist[node][neighbor] = weight

        for k in nodes:
            for i in nodes:
                for j in nodes:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist

    @staticmethod
    def kruskal(graph):
        """Performs Kruskal's Algorithm to find the Minimum Spanning Tree."""
        edges = []
        for node in graph:
            for neighbor, weight in graph[node]:
                edges.append((weight, node, neighbor))
        edges.sort()  # Sort edges by weight

        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        for node in graph:
            parent[node] = node
            rank[node] = 0

        mst = []
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))

        return mst

    @staticmethod
    def prim(graph, start):
        """Performs Prim's Algorithm to find the Minimum Spanning Tree."""
        mst = []
        visited = set([start])
        edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
        heapq.heapify(edges)

        while edges:
            weight, u, v = heapq.heappop(edges)
            if v not in visited:
                visited.add(v)
                mst.append((u, v, weight))
                for neighbor, weight in graph[v]:
                    if neighbor not in visited:
                        heapq.heappush(edges, (weight, v, neighbor))

        return mst

    @staticmethod
    def topological_sort(graph):
        """Performs Topological Sort on a Directed Acyclic Graph (DAG)."""
        in_degree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1
        
        queue = deque([node for node in graph if in_degree[node] == 0])
        sorted_list = []

        while queue:
            node = queue.popleft()
            sorted_list.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_list

    @staticmethod
    def tarjan(graph):
        """Performs Tarjan's Algorithm to find Strongly Connected Components (SCCs)."""
        index = 0
        stack = []
        indices = {}
        lowlink = {}
        on_stack = set()
        sccs = []

        def strongconnect(v):
            nonlocal index
            indices[v] = lowlink[v] = index
            index += 1
            stack.append(v)
            on_stack.add(v)

            for w in graph[v]:
                if w not in indices:
                    strongconnect(w)
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif w in on_stack:
                    lowlink[v] = min(lowlink[v], indices[w])

            if lowlink[v] == indices[v]:
                scc = []
                while True:
                    w = stack.pop()
                    on_stack.remove(w)
                    scc.append(w)
                    if w == v:
                        break
                sccs.append(scc)

        for node in graph:
            if node not in indices:
                strongconnect(node)

        return sccs
    
    @staticmethod
    def main():
        # Graph for testing
        graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 5)],
            'C': [('A', 4), ('B', 2), ('D', 1)],
            'D': [('B', 5), ('C', 1)],
        }

        # Test Dijkstra's Algorithm
        print("Dijkstra's Algorithm:", GraphAlgorithms.dijkstra(graph, 'A'))

        # Test Bellman-Ford Algorithm
        print("Bellman-Ford Algorithm:", GraphAlgorithms.bellman_ford(graph, 'A'))

        # Test A* Algorithm
        heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 1}
        print("A* Algorithm:", GraphAlgorithms.a_star(graph, 'A', 'D', heuristic))

        # Test Floyd-Warshall Algorithm
        print("Floyd-Warshall Algorithm:", GraphAlgorithms.floyd_warshall(graph))

        # Test Kruskal's Algorithm
        print("Kruskal's Algorithm:", GraphAlgorithms.kruskal(graph))

        # Test Prim's Algorithm
        print("Prim's Algorithm:", GraphAlgorithms.prim(graph, 'A'))

        # Test Topological Sort
        dag = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D'],
            'D': [],
        }
        print("Topological Sort:", GraphAlgorithms.topological_sort(dag))

        # Test Tarjan's Algorithm (SCCs)
        graph_scc = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A', 'D'],
            'D': ['E'],
            'E': ['D']
        }
        print("Tarjan's Algorithm (SCCs):", GraphAlgorithms.tarjan(graph_scc))


# Main function to test the graph algorithms
if __name__ == "__main__":
    GraphAlgorithms.main()

