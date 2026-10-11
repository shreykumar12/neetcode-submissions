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

        def reverse(head):
            prev = None
            curr = head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry

            carry = val // 10
            val %= 10
            trav.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            trav = trav.next
        
        res = reverse(dummy.next)
        return res

