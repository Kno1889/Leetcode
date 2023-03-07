# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        set_A = set()
        a = headA

        while a:
            set_A.add(a)
            a = a.next

        a = headB
        while a:
            if a in set_A:
                return a
            a = a.next

        return None
