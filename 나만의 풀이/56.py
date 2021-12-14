#LeetCode / 208. Implement Trie (Prefix Tree)

class Trie:

    def __init__(self):
        self.END_OF_STR = 'END_OF_STR'
        self.root = {}

    def insert(self, word: str) -> None:
        current_node = self.root
        for idx in word:
            if not idx in current_node:
                current_node[idx] = {}
            current_node = current_node[idx]
        current_node[self.END_OF_STR] = self.END_OF_STR

    def search(self, word: str) -> bool:
        current_node = self.root
        for idx in word:
            if not idx in current_node:
                return False
            current_node = current_node[idx]
        
        if self.END_OF_STR in current_node:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for idx in prefix:
            if not idx in current_node:
                return False
            current_node = current_node[idx]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param_2 = obj.search('applec')
print(param_2)
param_3 = obj.startsWith('azpp')
print(param_3)