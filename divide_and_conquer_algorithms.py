# divide_and_conquer_algorithms.py

import math

class DivideAndConquerAlgorithms:
    """
    ### Divide and Conquer Algorithms:
    1. Binary Search
    2. Merge Sort
    3. Quick Sort
    4. Strassen's Matrix Multiplication
    5. Closest Pair of Points
    """

    # 1. Binary Search
    @staticmethod
    def binary_search(arr, target):
        """Performs binary search on a sorted array."""
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    # 2. Merge Sort
    @staticmethod
    def merge_sort(arr):
        """Sorts an array using the merge sort algorithm."""
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            DivideAndConquerAlgorithms.merge_sort(left_half)
            DivideAndConquerAlgorithms.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    # 3. Quick Sort
    @staticmethod
    def quick_sort(arr):
        """Sorts an array using the quick sort algorithm."""
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return DivideAndConquerAlgorithms.quick_sort(left) + middle + DivideAndConquerAlgorithms.quick_sort(right)

    # 4. Strassen's Matrix Multiplication
    @staticmethod
    def strassen_matrix_multiplication(A, B):
        """Multiplies two matrices using Strassen's algorithm."""
        def add(A, B):
            return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

        def subtract(A, B):
            return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

        def split_matrix(M):
            mid = len(M) // 2
            return [[row[:mid] for row in M[:mid]], [row[mid:] for row in M[:mid]], [row[:mid] for row in M[mid:]], [row[mid:] for row in M[mid:]]]

        def strassen(A, B):
            if len(A) == 1:
                return [[A[0][0] * B[0][0]]]

            A11, A12, A21, A22 = split_matrix(A)
            B11, B12, B21, B22 = split_matrix(B)

            M1 = strassen(add(A11, A22), add(B11, B22))
            M2 = strassen(add(A21, A22), B11)
            M3 = strassen(A11, subtract(B12, B22))
            M4 = strassen(A22, subtract(B21, B11))
            M5 = strassen(add(A11, A12), B22)
            M6 = strassen(subtract(A21, A11), add(B11, B12))
            M7 = strassen(subtract(A12, A22), add(B21, B22))

            C11 = add(subtract(add(M1, M4), M5), M7)
            C12 = add(M3, M5)
            C21 = add(M2, M4)
            C22 = add(subtract(add(M1, M3), M2), M6)

            C = [[0 for _ in range(len(A))] for _ in range(len(A))]
            for i in range(len(A) // 2):
                for j in range(len(A) // 2):
                    C[i][j] = C11[i][j]
                    C[i][j + len(A) // 2] = C12[i][j]
                    C[i + len(A) // 2][j] = C21[i][j]
                    C[i + len(A) // 2][j + len(A) // 2] = C22[i][j]

            return C
        
        return strassen(A, B)

    # 5. Closest Pair of Points
    @staticmethod
    def closest_pair(points):
        """Finds the closest pair of points in a 2D plane."""
        def distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        def brute_force(points):
            min_dist = float('inf')
            pair = ()
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    dist = distance(points[i], points[j])
                    if dist < min_dist:
                        min_dist = dist
                        pair = (points[i], points[j])
            return pair, min_dist

        def closest_split_pair(px, py, delta, best_pair):
            mid_x = px[len(px) // 2][0]
            sy = [p for p in py if mid_x - delta <= p[0] <= mid_x + delta]

            best = best_pair
            best_dist = delta
            for i in range(len(sy)):
                for j in range(i + 1, len(sy)):
                    if sy[j][1] - sy[i][1] >= best_dist:
                        break
                    dist = distance(sy[i], sy[j])
                    if dist < best_dist:
                        best_dist = dist
                        best = (sy[i], sy[j])

            return best, best_dist

        def closest_pair_rec(px, py):
            if len(px) <= 3:
                return brute_force(px)

            mid = len(px) // 2
            left_px = px[:mid]
            right_px = px[mid:]
            left_py = [p for p in py if p[0] <= left_px[-1][0]]
            right_py = [p for p in py if p[0] > left_px[-1][0]]

            left_pair, left_dist = closest_pair_rec(left_px, left_py)
            right_pair, right_dist = closest_pair_rec(right_px, right_py)

            if left_dist < right_dist:
                best_pair = left_pair
                delta = left_dist
            else:
                best_pair = right_pair
                delta = right_dist

            split_pair, split_dist = closest_split_pair(px, py, delta, best_pair)
            if split_dist < delta:
                return split_pair, split_dist
            return best_pair, delta

        px = sorted(points, key=lambda p: p[0])
        py = sorted(points, key=lambda p: p[1])

        return closest_pair_rec(px, py)

    # Main function to test Divide and Conquer algorithms
    @staticmethod
    def main():
        # Test Binary Search
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 7
        print("Binary Search result:", DivideAndConquerAlgorithms.binary_search(arr, target))

        # Test Merge Sort
        arr = [38, 27, 43, 3, 9, 82, 10]
        DivideAndConquerAlgorithms.merge_sort(arr)
        print("Merge Sort result:", arr)

        # Test Quick Sort
        arr = [38, 27, 43, 3, 9, 82, 10]
        print("Quick Sort result:", DivideAndConquerAlgorithms.quick_sort(arr))

        # Test Strassen's Matrix Multiplication
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = DivideAndConquerAlgorithms.strassen_matrix_multiplication(A, B)
        print("Strassen's Matrix Multiplication result:", result)

        # Test Closest Pair of Points
        points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
        closest_pair, distance = DivideAndConquerAlgorithms.closest_pair(points)
        print(f"Closest pair: {closest_pair}, Distance: {distance}")

if __name__ == "__main__":
    DivideAndConquerAlgorithms.main()
