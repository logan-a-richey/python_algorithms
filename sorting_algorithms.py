# sorting_algorithms.py

class SortingAlgorithms:
    """
    ### Sorting Algorithms:
    1. Bubble Sort
    2. Selection Sort
    3. Insertion Sort
    4. Merge Sort
    5. Quick Sort
    6. Heap Sort
    7. Radix Sort
    """
    
    @staticmethod
    def bubble_sort(arr):
        """Sorts an array using the Bubble Sort algorithm."""
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def selection_sort(arr):
        """Sorts an array using the Selection Sort algorithm."""
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def insertion_sort(arr):
        """Sorts an array using the Insertion Sort algorithm."""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    @staticmethod
    def merge_sort(arr):
        """Sorts an array using the Merge Sort algorithm."""
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            SortingAlgorithms.merge_sort(left_half)
            SortingAlgorithms.merge_sort(right_half)

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
        return arr

    @staticmethod
    def quick_sort(arr):
        """Sorts an array using the Quick Sort algorithm."""
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)

    @staticmethod
    def heap_sort(arr):
        """Sorts an array using the Heap Sort algorithm."""
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        return arr

    @staticmethod
    def radix_sort(arr):
        """Sorts an array using the Radix Sort algorithm."""
        def counting_sort(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10
            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1
            for i in range(1, 10):
                count[i] += count[i-1]
            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1
            for i in range(n):
                arr[i] = output[i]

        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            counting_sort(arr, exp)
            exp *= 10
        return arr
    
    @staticmethod
    def main():
        arr = [64, 34, 25, 12, 22, 11, 90]
        
        print("Original Array:", arr)
        
        # Test Bubble Sort
        print("\nBubble Sort:", SortingAlgorithms.bubble_sort(arr.copy()))
        
        # Test Selection Sort
        print("Selection Sort:", SortingAlgorithms.selection_sort(arr.copy()))
        
        # Test Insertion Sort
        print("Insertion Sort:", SortingAlgorithms.insertion_sort(arr.copy()))
        
        # Test Merge Sort
        print("Merge Sort:", SortingAlgorithms.merge_sort(arr.copy()))
        
        # Test Quick Sort
        print("Quick Sort:", SortingAlgorithms.quick_sort(arr.copy()))
        
        
        # Test Heap Sort
        print("Heap Sort:", SortingAlgorithms.heap_sort(arr.copy()))
        
        # Test Radix Sort
        print("Radix Sort:", SortingAlgorithms.radix_sort(arr.copy()))


# Main function to test the sorting algorithms
if __name__ == "__main__":
    SortingAlgorithms.main()
