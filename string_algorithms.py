#string_algorithms.py

class StringAlgorithms:
    """
    ### String Algorithms:
    1. String Matching Algorithms (Knuth-Morris-Pratt (KMP))
    2. Rabin-Karp Algorithm
    3. Trie Data Structure
    4. Suffix Array/Suffix Tree
    5. Z Algorithm
    """
    
    @staticmethod
    def kmp_search(text, pattern):
        """Knuth-Morris-Pratt (KMP) algorithm for string matching."""
        def compute_lps(pattern):
            """Preprocess the pattern to create the longest prefix suffix (LPS) array."""
            lps = [0] * len(pattern)
            length = 0  # length of the previous longest prefix suffix
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = compute_lps(pattern)
        i = 0  # index for text
        j = 0  # index for pattern
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == len(pattern):
                return i - j  # pattern found
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1  # pattern not found

    @staticmethod
    def rabin_karp(text, pattern):
        """Rabin-Karp algorithm for string matching."""
        d = 256  # number of characters in the input alphabet
        q = 101  # prime number
        m = len(pattern)
        n = len(text)
        p_hash = 0  # hash value for pattern
        t_hash = 0  # hash value for text
        h = 1

        for i in range(m - 1):
            h = (h * d) % q

        for i in range(m):
            p_hash = (d * p_hash + ord(pattern[i])) % q
            t_hash = (d * t_hash + ord(text[i])) % q

        for i in range(n - m + 1):
            if p_hash == t_hash:
                if text[i:i + m] == pattern:
                    return i
            if i < n - m:
                t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
                if t_hash < 0:
                    t_hash += q
        return -1  # pattern not found
    
    
    class TrieNode:
        def __init__(self):
            """Node for the Trie data structure."""
            self.children = {}
            self.is_end_of_word = False
    
    
    class Trie:
        def __init__(self):
            """Trie data structure for efficient string matching."""
            self.root = StringAlgorithms.TrieNode()  # Correct reference to TrieNode
        
        def insert(self, word):
            """Insert a word into the Trie."""
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = StringAlgorithms.TrieNode()  # Correct reference
                node = node.children[char]
            node.is_end_of_word = True
        
        def search(self, word):
            """Search for a word in the Trie."""
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]
            return node.is_end_of_word
        
        def starts_with(self, prefix):
            """Check if there is any word in the Trie that starts with the given prefix."""
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return False
                node = node.children[char]
            return True
    
    
    @staticmethod
    def suffix_array(text):
        """Generates the suffix array of a given string."""
        suffixes = [(text[i:], i) for i in range(len(text))]
        suffixes.sort()
        return [suffix[1] for suffix in suffixes]
    
    
    @staticmethod
    def suffix_tree(text):
        """Generates a suffix tree for a given string."""
        class Node:
            def __init__(self):
                self.children = {}
                self.suffix_link = None
                self.start = -1
                self.end = -1
        
        root = Node()
        n = len(text)
        active_node = root
        active_edge = -1
        active_length = 0
        remaining_suffix_count = 0
        last_created_internal_node = None
        suffix_link = None
        
        # Add suffix to the tree one by one
        for i in range(n):
            last_created_internal_node = None
            remaining_suffix_count += 1
            while remaining_suffix_count > 0:
                if active_length == 0:
                    active_edge = i
                if text[active_edge] not in active_node.children:
                    active_node.children[text[active_edge]] = Node()
                    active_node.children[text[active_edge]].start = i
                    active_node.children[text[active_edge]].end = n
                    if last_created_internal_node is not None:
                        last_created_internal_node.suffix_link = active_node
                        last_created_internal_node = None
                else:
                    next_node = active_node.children[text[active_edge]]
                    if active_length >= next_node.end - next_node.start:
                        active_edge += 1
                        active_length -= (next_node.end - next_node.start)
                        active_node = next_node
                        continue
                    if text[next_node.start + active_length] == text[i]:
                        if last_created_internal_node is not None:
                            last_created_internal_node.suffix_link = active_node
                        active_length += 1
                        break
                    split_node = Node()
                    active_node.children[text[active_edge]] = split_node
                    split_node.children[text[i]] = Node()
                    split_node.children[text[i]].start = i
                    split_node.children[text[i]].end = n
                    next_node.start += active_length
                    split_node.children[text[next_node.start]] = next_node
                    if last_created_internal_node is not None:
                        last_created_internal_node.suffix_link = split_node
                    last_created_internal_node = split_node
                remaining_suffix_count -= 1
                if active_node == root and active_length > 0:
                    active_length -= 1
                    active_edge = i - remaining_suffix_count + 1
                elif active_node != root:
                    active_node = active_node.suffix_link
        
        return root  # Returns the root node of the suffix tree
    
    
    @staticmethod
    def z_algorithm(s):
        """Finds Z-array of a given string (Z algorithm)."""
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        z[0] = n
        return z
    
    
    @staticmethod
    def main():
        # Test Knuth-Morris-Pratt (KMP) Algorithm
        text = "ABABDABACDABABCABAB"
        pattern = "ABABCABAB"
        print(f"KMP Search Result (Pattern found at index):", StringAlgorithms.kmp_search(text, pattern))
        
        # Test Rabin-Karp Algorithm
        print(f"Rabin-Karp Search Result (Pattern found at index):", StringAlgorithms.rabin_karp(text, pattern))
        
        # Test Trie Data Structure
        trie = StringAlgorithms.Trie()
        trie.insert("apple")
        trie.insert("app")
        print("Trie Search (app):", trie.search("app"))
        print("Trie Search (apple):", trie.search("apple"))
        print("Trie Starts With (ap):", trie.starts_with("ap"))

        # Test Suffix Array
        text = "banana"
        print(f"Suffix Array of {text}:", StringAlgorithms.suffix_array(text))

        # Test Suffix Tree (This is a basic implementation and not fully optimized for large strings)
        suffix_tree = StringAlgorithms.suffix_tree(text)
        print("Suffix Tree Root:", suffix_tree)  # Returns the root node

        # Test Z Algorithm
        string = "abacabadabacaba"
        print(f"Z-Algorithm Result for {string}:", StringAlgorithms.z_algorithm(string))


# Main function to test the string algorithms
if __name__ == "__main__":
    StringAlgorithms.main()
