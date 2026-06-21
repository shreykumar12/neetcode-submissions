# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get middle of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # Reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Merge the 2 in place
        second = prev # prev is head of reversed half
        first = head
        while second: # len(second) guaranteed to be <= len(first))
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
