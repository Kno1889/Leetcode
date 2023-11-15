# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x
        
        dummy_head = head
        next_node = head.next

        while next_node != None:
            new_node = ListNode(gcd(head.val, next_node.val), next_node)
            head.next = new_node

            head = next_node
            next_node = next_node.next

        return dummy_head      
        