# Algorithms
# module to learning common computer algorithms
# Logan Richey
# 2024-11-08

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("algorithm_debug.log"),  # Logs to a file
        logging.StreamHandler()                      # Also logs to console
    ]
)

from src.sorting_algorithms import SortingAlgorithms
from src.searching_algorithms import SearchingAlgorithms
from src.graph_algorithms import GraphAlgorithms
from src.dynamic_programming import DynamicProgramming
from src.string_algorithms import StringAlgorithms
from src.data_structures import DataStructures
from src.math_algorithms import MathAlgorithms
from src.greedy_algorithms import GreedyAlgorithms
from src.backtracking_algorithms import BacktrackingAlgorithms
from src.divide_and_conquer_algorithms import DivideAndConquerAlgorithms
from src.misc_algorithms import MiscAlgorithms

class Main:
    """
    Algorithms tested:
    
    ### Sorting Algorithms:
    1. Bubble Sort
    2. Selection Sort
    3. Insertion Sort
    4. Merge Sort
    5. Quick Sort
    6. Heap Sort
    7. Radix Sort
    
    ### Searching Algorithms:
    1. Linear Search
    2. Binary Search
    3. Depth-First Search (DFS)
    4. Breadth-First Search (BFS)
    
    ### Graph Algorithms:
    1. Dijkstra's Algorithm
    2. Bellman-Ford Algorithm
    3. A* Algorithm
    4. Floyd-Warshall Algorithm
    5. Kruskal's Algorithm
    6. Prim's Algorithm
    7. Topological Sort
    8. Tarjan's Algorithm
    
    ### Dynamic Programming (DP) Algorithms:
    1. Fibonacci Sequence
    2. Longest Common Subsequence (LCS)
    3. Knapsack Problem
    4. Coin Change Problem
    5. Longest Increasing Subsequence
    6. Edit Distance
    7. Matrix Chain Multiplication
    
    ### String Algorithms:
    1. String Matching Algorithms (Knuth-Morris-Pratt (KMP))
    2. Rabin-Karp Algorithm
    3. Trie Data Structure
    4. Suffix Array/Suffix Tree
    5. Z Algorithm
    
    ### Data Structure-Based Algorithms:
    1. Binary Search Tree (BST)
    2. AVL Tree & Red-Black Tree
    3. Hashing (Chaining, Open Addressing)
    4. Fenwick Tree / Binary Indexed Tree
    5. Segment Tree
    6. Union-Find (Disjoint Set Union)
    7. Heap
    
    ### Mathematical Algorithms:
    1. Greatest Common Divisor (GCD) (Euclidean Algorithm)
    2. Sieve of Eratosthenes
    3. Fast Exponentiation
    4. Modular Arithmetic
    5. Combination & Permutation Algorithms
    6. Floyd's Cycle Detection Algorithm
    
    ### Greedy Algorithms:
    1. Activity Selection Problem
    2. Huffman Coding
    3. Interval Scheduling Maximization
    4. Fractional Knapsack
    5. Minimum Number of Platforms
    
    ### Backtracking Algorithms:
    1. N-Queens Problem
    2. Sudoku Solver
    3. Permutations & Combinations
    4. Subset Sum Problem
    5. Hamiltonian & Eulerian Paths
    
    ### Divide and Conquer Algorithms:
    1. Binary Search
    2. Merge Sort
    3. Quick Sort
    4. Strassen's Matrix Multiplication
    5. Closest Pair of Points
    
    ### Miscellaneous Algorithms:
    1. Reservoir Sampling
    2. Fisher-Yates Shuffle (Knuth Shuffle)
    3. Monte Carlo Algorithms
    4. Bloom Filter
    """
    
    @staticmethod
    def main():
        completed_all_successfully = True
        
        algorithm_classes = [
            ("SortingAlgorithms", SortingAlgorithms),
            ("SearchingAlgorithms", SearchingAlgorithms),
            ("GraphAlgorithms", GraphAlgorithms),
            ("DynamicProgramming", DynamicProgramming),
            ("StringAlgorithms", StringAlgorithms),
            ("DataStructures", DataStructures),
            ("MathAlgorithms", MathAlgorithms),
            ("GreedyAlgorithms", GreedyAlgorithms),
            ("BacktrackingAlgorithms", BacktrackingAlgorithms),
            ("DivideAndConquerAlgorithms", DivideAndConquerAlgorithms),
            ("MiscAlgorithms", MiscAlgorithms)
        ]
        
        with open("docstrings.txt","w") as file:
            for name, algorithm_class in algorithm_classes:
                
                file.write(f"{algorithm_class.__doc__}")
                
                logging.info(f"Starting {name} tests.")
                try:
                    algorithm_class.main()
                    logging.info(f"{name} tests completed successfully.")
                except Exception as e:
                    completed_all_successfully = False
                    logging.error(f"Error in {name}: {e}", exc_info=True)
                print()
                print()
            
            if completed_all_successfully:
                print()
                logging.info(f"ALL tests completed successfully!")
        
        return None


if __name__ == "__main__":
    Main.main()
