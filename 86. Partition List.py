# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # thought process:
        # iterate over linked list
        # if current is less than x, add to less ll
        # greater than or equal to, add to greater ll
        # connect less ll tail to greater ll head.
        less = ListNode()
        greater = ListNode()

        l_tail = less
        g_tail = greater

        while head:
            if head.val < x:
                l_tail.next = head
                l_tail = l_tail.next
            else:
                g_tail.next = head
                g_tail = g_tail.next
            head = head.next

        l_tail.next = greater.next
        g_tail.next = None

        return less.next
