class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = Node("")
        self.right = Node("")
        page = Node(homepage)
        self.left.next = page
        page.prev = self.left
        page.next = self.right
        self.right.prev = page
        self.current = page

    #insert node next to current
    def insert(self, node):
        prv = self.current
        prv.next = node
        node.prev = self.current
        node.next = self.right
        self.right.prev = node
        
    def visit(self, url: str) -> None:
        node = Node(url)
        self.insert(node)
        self.current = node
        

    def back(self, steps: int) -> str:
        curr = self.current
        while curr.prev is not self.left and steps > 0:
            curr = curr.prev
            steps -= 1
        self.current = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.current
        while curr.next is not self.right and steps > 0:
            curr = curr.next
            steps -= 1
        self.current = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)