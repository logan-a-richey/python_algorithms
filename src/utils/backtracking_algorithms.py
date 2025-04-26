# backtracking_algorithms.py

class BacktrackingAlgorithms:
    """
    ### Backtracking Algorithms:
    1. N-Queens Problem
    2. Sudoku Solver
    3. Permutations & Combinations
    4. Subset Sum Problem
    5. Hamiltonian & Eulerian Paths
    """

    # 1. N-Queens Problem
    @staticmethod
    def solve_n_queens(n):
        """Solves the N-Queens problem using backtracking."""
        board = [-1] * n  # Board with n columns
        solutions = []
        
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or \
                   board[i] - i == col - row or \
                   board[i] + i == col + row:
                    return False
            return True
        
        def solve(board, row):
            if row == n:
                solutions.append(board[:])
                return
            
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)
                    board[row] = -1
        
        solve(board, 0)
        return solutions

    # 2. Sudoku Solver
    @staticmethod
    def solve_sudoku(board):
        """Solves the Sudoku puzzle using backtracking."""
        def is_safe(board, row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == 0:
                        for num in range(1, 10):
                            if is_safe(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = 0
                        return False
            return True
        
        solve(board)
        return board

    # 3. Permutations & Combinations
    @staticmethod
    def permutations(nums):
        """Generates all permutations of a list of numbers using backtracking."""
        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        result = []
        backtrack([], nums)
        return result
    
    @staticmethod
    def combinations(nums, k):
        """Generates all combinations of k elements from the list of numbers using backtracking."""
        def backtrack(start, path):
            if len(path) == k:
                result.append(path)
                return
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        
        result = []
        backtrack(0, [])
        return result

    # 4. Subset Sum Problem
    @staticmethod
    def subset_sum(nums, target):
        """Finds subsets of numbers that sum to a given target."""
        def backtrack(start, current_sum, path):
            if current_sum == target:
                result.append(path)
                return
            if current_sum > target:
                return
            for i in range(start, len(nums)):
                backtrack(i + 1, current_sum + nums[i], path + [nums[i]])

        result = []
        backtrack(0, 0, [])
        return result

    # 5. Hamiltonian & Eulerian Paths
    @staticmethod
    def hamiltonian_path(graph):
        """Finds a Hamiltonian path in a given graph using backtracking."""
        def is_safe(v, path, pos):
            if v in path:
                return False
            if pos > 0 and graph[path[pos - 1]][v] == 0:
                return False
            return True

        def solve(graph, path, pos):
            if pos == len(graph):
                return True

            for v in range(len(graph)):
                if is_safe(v, path, pos):
                    path[pos] = v
                    if solve(graph, path, pos + 1):
                        return True
                    path[pos] = -1
            return False

        path = [-1] * len(graph)
        if solve(graph, path, 0):
            return path
        return []

    @staticmethod
    def eulerian_path(graph):
        """Finds an Eulerian path in a given graph."""
        def is_eulerian_path(graph):
            odd_degree_nodes = 0
            for i in range(len(graph)):
                if sum(graph[i]) % 2 != 0:
                    odd_degree_nodes += 1
            return odd_degree_nodes == 0 or odd_degree_nodes == 2

        def find_path(graph, path, u):
            for v in range(len(graph)):
                if graph[u][v] == 1:
                    graph[u][v] = graph[v][u] = 0
                    find_path(graph, path, v)
            path.append(u)
        
        if not is_eulerian_path(graph):
            return []
        
        path = []
        find_path(graph, path, 0)
        return path[::-1]  # Reverse to get correct order

    # Main function to test Backtracking algorithms
    @staticmethod
    def main():
        # Test N-Queens Problem
        n = 4
        solutions = BacktrackingAlgorithms.solve_n_queens(n)
        print(f"Solutions for {n}-Queens Problem:")
        for solution in solutions:
            print(solution)

        # Test Sudoku Solver
        sudoku_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        solved_sudoku = BacktrackingAlgorithms.solve_sudoku(sudoku_board)
        print("Solved Sudoku:")
        for row in solved_sudoku:
            print(row)

        # Test Permutations & Combinations
        nums = [1, 2, 3]
        print("Permutations:", BacktrackingAlgorithms.permutations(nums))
        k = 2
        print(f"Combinations of {k} elements:", BacktrackingAlgorithms.combinations(nums, k))

        # Test Subset Sum Problem
        nums = [2, 3, 7, 8, 10]
        target = 10
        print(f"Subset sum subsets for target {target}:", BacktrackingAlgorithms.subset_sum(nums, target))

        # Test Hamiltonian Path
        graph = [
            [0, 1, 0, 1],
            [1, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 1, 1, 0]
        ]
        print("Hamiltonian Path:", BacktrackingAlgorithms.hamiltonian_path(graph))

        # Test Eulerian Path
        graph = [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ]
        print("Eulerian Path:", BacktrackingAlgorithms.eulerian_path(graph))


if __name__ == "__main__":
    BacktrackingAlgorithms.main()
