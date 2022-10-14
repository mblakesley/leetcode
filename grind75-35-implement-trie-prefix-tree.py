# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:
    # Yeah, I could've/should've done it with Node objects, but I kept it a bit simpler for this scenario
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        branch = self.trie
        for char in word:
            branch = branch.setdefault(char, {})
        branch['.'] = True

    def search(self, word: str) -> bool:
        return self._search(word)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix, terminal=False)

    def _search(self, string: str, terminal: bool = True) -> bool:
        branch = self.trie
        for char in string:
            branch = branch.get(char)
            if branch is None:
                return False
        if terminal:
            return branch.get('.', False)
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
