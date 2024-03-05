# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:
    def __init__(self):
        self.root = {}
        self.delimiter = '.'

    def insert(self, word: str) -> None:
        word += self.delimiter
        parent = self.root
        for char in word:
            parent = parent.setdefault(char, {})

    def search(self, word: str) -> bool:
        return self.startsWith(word + self.delimiter)

    def startsWith(self, prefix: str) -> bool:
        parent = self.root
        for char in prefix:
            parent = parent.get(char)
            if parent is None:
                return False
        return True
