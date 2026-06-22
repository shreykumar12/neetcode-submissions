# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Displace right n nodes from left.next
        # Setting up left.next to be the deleted node 
        # By maintaining this pivot
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Move left and right together util right reaches the end
        # At this point left.next is the node we need to delete
        while right:
            right = right.next
            left = left.next

        # Break and build the new link
        node = left.next
        left.next = node.next

        return dummy.next