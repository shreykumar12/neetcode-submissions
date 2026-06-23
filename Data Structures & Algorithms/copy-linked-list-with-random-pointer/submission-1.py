"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Build hashmap mapping original nodes to their copies
        # Use the hashmap to access copies of nodes and reassing 
        # Pointers to make the deep copy

        copies = { None : None}
        curr = head

        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = copies[curr]
            copy.next = copies[curr.next]
            copy.random = copies[curr.random]
            curr = curr.next
        
        return copies[head]