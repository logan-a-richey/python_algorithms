#dynamic_programming.py

class DynamicProgramming:
    """
    ### Dynamic Programming (DP) Algorithms:
    1. Fibonacci Sequence
    2. Longest Common Subsequence (LCS)
    3. Knapsack Problem
    4. Coin Change Problem
    5. Longest Increasing Subsequence
    6. Edit Distance
    7. Matrix Chain Multiplication
    """

    @staticmethod
    def fibonacci(n):
        """Returns the nth Fibonacci number using dynamic programming."""
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    @staticmethod
    def lcs(X, Y):
        """Finds the Longest Common Subsequence (LCS) between two strings."""
        m, n = len(X), len(Y)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    @staticmethod
    def knapsack(weights, values, capacity):
        """Solves the 0/1 Knapsack Problem."""
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for w in range(capacity + 1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif weights[i - 1] <= w:
                    dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][capacity]

    @staticmethod
    def coin_change(coins, amount):
        """Solves the Coin Change problem (minimum number of coins required)."""
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    @staticmethod
    def longest_increasing_subsequence(arr):
        """Finds the length of the Longest Increasing Subsequence (LIS)."""
        n = len(arr)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    @staticmethod
    def edit_distance(str1, str2):
        """Finds the Edit Distance (Levenshtein Distance) between two strings."""
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    @staticmethod
    def matrix_chain_multiplication(dimensions):
        """Solves the Matrix Chain Multiplication problem."""
        n = len(dimensions)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    q = dp[i][k] + dp[k][j] + dimensions[i] * dimensions[k] * dimensions[j]
                    dp[i][j] = min(dp[i][j], q)

        return dp[0][n - 1]
    
    @staticmethod
    def main():
        # Test Fibonacci Sequence
        n = 10
        print(f"Fibonacci of {n}:", DynamicProgramming.fibonacci(n))

        # Test Longest Common Subsequence (LCS)
        X = "AGGTAB"
        Y = "GXTXAYB"
        print(f"LCS of {X} and {Y}:", DynamicProgramming.lcs(X, Y))

        # Test Knapsack Problem
        weights = [1, 2, 3]
        values = [60, 100, 120]
        capacity = 5
        print(f"Knapsack Result:", DynamicProgramming.knapsack(weights, values, capacity))

        # Test Coin Change Problem
        coins = [1, 2, 5]
        amount = 11
        print(f"Coin Change Result:", DynamicProgramming.coin_change(coins, amount))

        # Test Longest Increasing Subsequence (LIS)
        arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        print(f"Longest Increasing Subsequence Length:", DynamicProgramming.longest_increasing_subsequence(arr))

        # Test Edit Distance
        str1 = "sitting"
        str2 = "kitten"
        print(f"Edit Distance between {str1} and {str2}:", DynamicProgramming.edit_distance(str1, str2))

        # Test Matrix Chain Multiplication
        dimensions = [1, 2, 3, 4]
        print(f"Minimum number of multiplications:", DynamicProgramming.matrix_chain_multiplication(dimensions))


# Main function to test the dynamic programming algorithms
if __name__ == "__main__":
    DynamicProgramming.main()