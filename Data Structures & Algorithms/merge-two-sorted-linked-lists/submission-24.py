# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        trav = dummy

        while l1 and l2:
            if l1.val < l2.val:
                trav.next = l1
                l1 = l1.next
            else:
                trav.next = l2
                l2 = l2.next
            trav = trav.next
        
        if l1:
            trav.next = l1
        else:
            trav.next = l2
        
        return dummy.next