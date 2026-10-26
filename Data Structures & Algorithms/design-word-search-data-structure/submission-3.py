class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.start = Node(None)

    def addWord(self, word: str) -> None:
        curr = self.start
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]   
            return curr.isEnd
        
        return dfs(0, self.start)
        
                
