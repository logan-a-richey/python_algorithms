# greedy_algorithms.py

import heapq
from collections import defaultdict

class GreedyAlgorithms:
    """
    ### Greedy Algorithms:
    1. Activity Selection Problem
    2. Huffman Coding
    3. Interval Scheduling Maximization
    4. Fractional Knapsack
    5. Minimum Number of Platforms
    """

    # 1. Activity Selection Problem (Greedy Algorithm)
    @staticmethod
    def activity_selection(start_times, end_times):
        """Selects the maximum number of activities that don't overlap."""
        n = len(start_times)
        activities = sorted(zip(start_times, end_times), key=lambda x: x[1])
        
        selected_activities = []
        last_end_time = -1
        for start, end in activities:
            if start >= last_end_time:
                selected_activities.append((start, end))
                last_end_time = end
        return selected_activities

    # 2. Huffman Coding (Greedy Algorithm)
    class HuffmanNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    @staticmethod
    def huffman_coding(char_freq):
        """Generates the Huffman code for a given set of characters and frequencies."""
        # Create a priority queue (min-heap)
        heap = [GreedyAlgorithms.HuffmanNode(char, freq) for char, freq in char_freq.items()]
        heapq.heapify(heap)
        
        # Build the Huffman tree
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = GreedyAlgorithms.HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)
        
        # Generate the Huffman codes
        huffman_codes = {}

        def generate_codes(node, current_code):
            if node is None:
                return
            if node.char is not None:
                huffman_codes[node.char] = current_code
            generate_codes(node.left, current_code + '0')
            generate_codes(node.right, current_code + '1')
        
        generate_codes(heap[0], "")
        return huffman_codes

    # 3. Interval Scheduling Maximization (Greedy Algorithm)
    @staticmethod
    def interval_scheduling(intervals):
        """Schedules the maximum number of non-overlapping intervals."""
        intervals.sort(key=lambda x: x[1])  # Sort intervals by finish time
        selected_intervals = []
        last_end_time = -1
        for interval in intervals:
            if interval[0] >= last_end_time:
                selected_intervals.append(interval)
                last_end_time = interval[1]
        return selected_intervals

    # 4. Fractional Knapsack (Greedy Algorithm)
    @staticmethod
    def fractional_knapsack(capacity, weights, values):
        """Solves the Fractional Knapsack Problem."""
        n = len(values)
        items = [(values[i], weights[i], values[i] / weights[i]) for i in range(n)]
        items.sort(key=lambda x: x[2], reverse=True)  # Sort items by value/weight ratio
        
        total_value = 0
        for value, weight, ratio in items:
            if capacity == 0:
                break
            if weight <= capacity:
                total_value += value
                capacity -= weight
            else:
                total_value += value * (capacity / weight)
                capacity = 0
        return total_value

    # 5. Minimum Number of Platforms (Greedy Algorithm)
    @staticmethod
    def minimum_platforms(arrivals, departures):
        """Finds the minimum number of platforms required for trains at the station."""
        arrivals.sort()
        departures.sort()
        
        platforms_needed = 0
        max_platforms = 0
        i = 0
        j = 0
        n = len(arrivals)

        while i < n and j < n:
            if arrivals[i] <= departures[j]:
                platforms_needed += 1
                i += 1
            else:
                platforms_needed -= 1
                j += 1
            max_platforms = max(max_platforms, platforms_needed)
        
        return max_platforms

    # Main function to test the Greedy algorithms
    @staticmethod
    def main():
        # Test Activity Selection Problem
        start_times = [1, 3, 0, 5, 8, 5]
        end_times = [2, 4, 6, 7, 9, 9]
        selected_activities = GreedyAlgorithms.activity_selection(start_times, end_times)
        print("Selected Activities:", selected_activities)
        
        # Test Huffman Coding
        char_freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
        huffman_codes = GreedyAlgorithms.huffman_coding(char_freq)
        print("Huffman Codes:", huffman_codes)
        
        # Test Interval Scheduling Maximization
        intervals = [(1, 4), (2, 6), (5, 8), (7, 9)]
        selected_intervals = GreedyAlgorithms.interval_scheduling(intervals)
        print("Selected Intervals:", selected_intervals)

        # Test Fractional Knapsack
        capacity = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        max_value = GreedyAlgorithms.fractional_knapsack(capacity, weights, values)
        print("Maximum value in Knapsack:", max_value)
        
        # Test Minimum Number of Platforms
        arrivals = [900, 940, 950, 1100, 1500, 1800]
        departures = [910, 1200, 1120, 1130, 1900, 2000]
        platforms = GreedyAlgorithms.minimum_platforms(arrivals, departures)
        print("Minimum number of platforms required:", platforms)

if __name__ == "__main__":
    GreedyAlgorithms.main()
