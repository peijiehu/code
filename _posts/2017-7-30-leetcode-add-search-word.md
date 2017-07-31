## [LeetCode]Add and Search Word - Data structure design

```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.is_word = True
        
    def search(self, word):
        return self._find(self.root, word)
        
    def _find(self, node, word):
        if word == '':
            return node.is_word
        if word == '.':
            for c in node.children:
                if self.find(node.children[c], word[1:]):
                    return True
        else:
            child = node.children.get(w[0])
            if child:
                return self.find(child, w[1:])
        return False
```
