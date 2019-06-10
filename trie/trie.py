import collections


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add a word to the trie
        """
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]
            current_node.is_word = True

    def exists(self, word):
        """
        Check whether a given word exists in our trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word


def run_tests():
    # Add words
    valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
    word_trie = Trie()
    for valid_word in valid_words:
        word_trie.add(valid_word)

    # Tests
    assert word_trie.exists('the')
    assert word_trie.exists('any')
    assert not word_trie.exists('these')
    assert not word_trie.exists('zzz')
    print('All tests passed!')


if __name__ == "__main__":
    run_tests()
