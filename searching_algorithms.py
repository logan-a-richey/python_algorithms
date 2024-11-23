#searching_algorithms.py

from collections import deque

class SearchingAlgorithms:
    """
    ### Searching Algorithms:
    1. Linear Search
    2. Binary Search
    3. Depth-First Search (DFS)
    4. Breadth-First Search (BFS)
    """
    
    @staticmethod
    def linear_search(arr, target):
        """Performs linear search to find the target element in the array."""
        for i in range(len(arr)):
            if arr[i] == target:
                return i  # return index of target
        return -1  # return -1 if target is not found

    @staticmethod
    def binary_search(arr, target):
        """Performs binary search on a sorted array to find the target element."""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # return -1 if target is not found

    @staticmethod
    def dfs(graph, start):
        """Performs Depth-First Search (DFS) on a graph starting from a given node."""
        visited = set()
        result = []

        def dfs_helper(node):
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result

    @staticmethod
    def bfs(graph, start):
        """Performs Breadth-First Search (BFS) on a graph starting from a given node."""
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(graph[node] - visited)
        return result
    
    @staticmethod
    def main():
        # Testing Linear Search
        arr = [10, 20, 30, 40, 50, 60]
        target = 30
        print("Linear Search:", SearchingAlgorithms.linear_search(arr, target))

        # Testing Binary Search (Array must be sorted)
        sorted_arr = [10, 20, 30, 40, 50, 60]
        print("Binary Search:", SearchingAlgorithms.binary_search(sorted_arr, target))

        # Testing Depth-First Search (DFS)
        graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B', 'F'},
            'F': {'C', 'E'}
        }
        print("DFS:", SearchingAlgorithms.dfs(graph, 'A'))

        # Testing Breadth-First Search (BFS)
        print("BFS:", SearchingAlgorithms.bfs(graph, 'A'))


# Main function to test the searching and graph traversal algorithms
if __name__ == "__main__":
    SearchingAlgorithms.main()
