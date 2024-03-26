# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traversed = []
        prev = None
        dummy = head
        
        while head:
            if head.val not in traversed:
                traversed.append(head.val)
                prev = head
                head = head.next
            else:
                prev.next = head.next
                head = head.next
        
        return dummy
        