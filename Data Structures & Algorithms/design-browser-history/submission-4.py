class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = Node("")
        self.right = Node("")
        home = Node(homepage)
        self.left.next = self.right.prev = home
        home.prev = self.left
        home.next = self.right
        self.current = home
    
    # insert next to current page
    def insert(self, node):
        prv = self.current
        prv.next = node
        node.next = self.right
        node.prev = prv
        self.right.prev = node

    def visit(self, url: str) -> None:
        node = Node(url)
        self.insert(node)
        self.current = node

    def back(self, steps: int) -> str:
        curr = self.current
        while curr.prev != self.left and steps > 0:
            curr = curr.prev
            steps -= 1
        self.current = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.current
        while curr.next != self.right and steps > 0:
            curr = curr.next
            steps -= 1
        self.current = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)