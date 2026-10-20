class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        self.current.next = node
        node.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        curr = self.current
        while curr.prev and steps > 0:
            curr = curr.prev
            steps -= 1
        self.current = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.current
        while curr.next and steps > 0:
            curr = curr.next
            steps -= 1
        self.current = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)