# math_algorithms.py

class MathAlgorithms:
    """
    ### Mathematical Algorithms:
    1. Greatest Common Divisor (GCD) (Euclidean Algorithm)
    2. Sieve of Eratosthenes
    3. Fast Exponentiation
    4. Modular Arithmetic
    5. Combination & Permutation Algorithms
    6. Floyd's Cycle Detection Algorithm
    """

    # Greatest Common Divisor (GCD) using Euclidean Algorithm
    @staticmethod
    def gcd(a, b):
        """Returns the GCD of a and b using the Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return a

    # Sieve of Eratosthenes
    @staticmethod
    def sieve_of_eratosthenes(limit):
        """Returns all primes up to a given limit using the Sieve of Eratosthenes."""
        sieve = [True] * (limit + 1)
        sieve[0], sieve[1] = False, False
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        primes = [i for i in range(limit + 1) if sieve[i]]
        return primes

    # Fast Exponentiation (Exponentiation by Squaring)
    @staticmethod
    def fast_exponentiation(base, exp):
        """Calculates base raised to the power exp in logarithmic time."""
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2
        return result

    # Modular Arithmetic (Modular Exponentiation)
    @staticmethod
    def modular_exponentiation(base, exp, mod):
        """Calculates (base^exp) % mod using modular exponentiation."""
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result

    # Combination & Permutation Algorithms
    @staticmethod
    def factorial(n):
        """Calculates the factorial of a number n."""
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def combination(n, k):
        """Calculates the number of combinations (n choose k)."""
        return MathAlgorithms.factorial(n) // (MathAlgorithms.factorial(k) * MathAlgorithms.factorial(n - k))

    @staticmethod
    def permutation(n, k):
        """Calculates the number of permutations (n permute k)."""
        return MathAlgorithms.factorial(n) // MathAlgorithms.factorial(n - k)

    # Floyd's Cycle Detection Algorithm (Tortoise and Hare)
    @staticmethod
    def floyd_cycle_detection(f):
        """Floyd's cycle detection algorithm (Tortoise and Hare) to detect cycles in a function f."""
        tortoise = f(0)
        hare = f(f(0))
        while tortoise != hare:
            tortoise = f(tortoise)
            hare = f(f(hare))
        return tortoise  # returns the meeting point of the cycle

    # Main function to test the mathematical algorithms
    @staticmethod
    def main():
        # Test GCD using Euclidean Algorithm
        print("GCD of 56 and 98:", MathAlgorithms.gcd(56, 98))  # Expected output: 14
        print()

        # Test Sieve of Eratosthenes
        limit = 50
        primes = MathAlgorithms.sieve_of_eratosthenes(limit)
        print(f"Primes up to {limit}:", primes)  # Expected output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        print()

        # Test Fast Exponentiation
        base, exp = 2, 10
        print(f"Fast Exponentiation of {base}^{exp}:", MathAlgorithms.fast_exponentiation(base, exp))  # Expected output: 1024
        print()

        # Test Modular Exponentiation
        base, exp, mod = 3, 200, 100
        print(f"Modular Exponentiation ({base}^{exp} mod {mod}):", MathAlgorithms.modular_exponentiation(base, exp, mod))  # Expected output: 49
        print()

        # Test Combination and Permutation Algorithms
        n, k = 5, 3
        print(f"Combination of {n} choose {k}:", MathAlgorithms.combination(n, k))  # Expected output: 10
        print(f"Permutation of {n} permute {k}:", MathAlgorithms.permutation(n, k))  # Expected output: 60
        print()

        # Test Floyd's Cycle Detection Algorithm
        # Example: Using a simple cycle function
        def f(x):
            return (x * x + 1) % 6

        cycle_start = MathAlgorithms.floyd_cycle_detection(f)
        print("Floyd's Cycle Detection - Cycle starts at:", cycle_start)  # Expected output: 1


if __name__ == "__main__":
    MathAlgorithms.main()
