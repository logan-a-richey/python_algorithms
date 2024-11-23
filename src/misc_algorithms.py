import random
import hashlib
import math

class MiscAlgorithms:
    """
    ### Miscellaneous Algorithms:
    1. Reservoir Sampling
    2. Fisher-Yates Shuffle (Knuth Shuffle)
    3. Monte Carlo Algorithms
    4. Bloom Filter
    """

    # 1. Reservoir Sampling
    @staticmethod
    def reservoir_sampling(stream, k):
        """Selects k random elements from a stream using reservoir sampling."""
        reservoir = []
        for i, item in enumerate(stream):
            if i < k:
                reservoir.append(item)
            else:
                j = random.randint(0, i)
                if j < k:
                    reservoir[j] = item
        return reservoir

    # 2. Fisher-Yates Shuffle (Knuth Shuffle)
    @staticmethod
    def fisher_yates_shuffle(arr):
        """Shuffles an array using the Fisher-Yates (Knuth) algorithm."""
        n = len(arr)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    # 3. Monte Carlo Algorithms
    @staticmethod
    def monte_carlo_pi(num_samples):
        """Estimates the value of Pi using the Monte Carlo method."""
        inside_circle = 0
        for _ in range(num_samples):
            x, y = random.random(), random.random()
            if x ** 2 + y ** 2 <= 1:
                inside_circle += 1
        return 4 * inside_circle / num_samples

    # 4. Bloom Filter
    @staticmethod
    def bloom_filter(size, hash_functions, elements):
        """Implements a Bloom filter to test membership of elements in a set."""
        bit_array = [0] * size

        # Hash each element and mark the corresponding bits
        for element in elements:
            for hash_func in hash_functions:
                # Convert hash hex string to an integer before applying modulo
                hash_value = int(hash_func(element), 16) % size
                bit_array[hash_value] = 1

        def contains(element):
            """Checks if an element is probably in the set."""
            return all(bit_array[int(hash_func(element), 16) % size] for hash_func in hash_functions)

        return contains

    # Main function to test Miscellaneous algorithms
    @staticmethod
    def main():
        # Test Reservoir Sampling
        stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3
        print("Reservoir Sampling result:", MiscAlgorithms.reservoir_sampling(stream, k))
        
        # Test Fisher-Yates Shuffle (Knuth Shuffle)
        arr = [1, 2, 3, 4, 5]
        print("Fisher-Yates Shuffle result:", MiscAlgorithms.fisher_yates_shuffle(arr))
        
        # Test Monte Carlo Algorithm to estimate Pi
        num_samples = 100000
        print("Monte Carlo Pi estimate:", MiscAlgorithms.monte_carlo_pi(num_samples))
        
        # Test Bloom Filter
        size = 1000
        hash_functions = [
            lambda x: hashlib.md5(x.encode('utf-8')).hexdigest(),
            lambda x: hashlib.sha1(x.encode('utf-8')).hexdigest()
        ]
        elements = ['apple', 'banana', 'orange']
        bloom = MiscAlgorithms.bloom_filter(size, hash_functions, elements)
        
        # Test if an element is in the Bloom Filter
        print("Is 'apple' in Bloom Filter?", bloom('apple'))
        print("Is 'grape' in Bloom Filter?", bloom('grape'))


if __name__ == "__main__":
    MiscAlgorithms.main()
