class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.start = Node(None)

    def insert(self, word: str) -> None:
        curr = self.start
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = Node(word[i])
            if i == len(word) - 1:
                curr.children[word[i]].isEnd = True
            curr = curr.children[word[i]]


    def search(self, word: str) -> bool:
        curr = self.start
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.start
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        
        