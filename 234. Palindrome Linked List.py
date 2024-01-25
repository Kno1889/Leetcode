# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        traversed = []

        while head:
            traversed.append(head.val)
            head = head.next
        
        j = -1
        # 2 pointers
        for i in range(len(traversed) // 2):
            if traversed[i] != traversed[j]:
                return False
            j -= 1
        
        return True
