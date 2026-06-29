# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Seperate the list, advence pointers so that
        # left ptr is right before node we want to remove
        # i.e left.next = removed node

        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1
        
        # Now r is n steps ahead of left.next
        # So we advance both ptrs together until we reach 
        # End of list bc then left.next will be the node we 
        # Want to remove

        while l and r:
            r = r.next
            l = l.next
        
        node = l.next
        l.next = node.next
        

        return dummy.next