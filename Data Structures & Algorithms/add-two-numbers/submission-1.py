# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        trav = dummy
        carry = 0

        while l1 or l2:
            if l1 and l2:
                v1, v2 = l1.val, l2.val
                l1, l2 = l1.next, l2.next
            elif l1:
                v1, v2 = l1.val, 0
                l1 = l1.next
            elif l2:
                v1, v2 = 0, l2.val
                l2 = l2.next
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            trav.next = ListNode(val)
            trav = trav.next
        
        if carry:
            trav.next = ListNode(carry)
            trav = trav.next
        
        return dummy.next

            