# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            if not list2:
                return 
            else:
                return list2 

        next_sorted_node = ListNode()

        new_head = next_sorted_node
        
        while list1 and list2:
            if list1.val < list2.val:
                next_sorted_node.next = list1
                list1 = list1.next
            else:
                next_sorted_node.next = list2
                list2 = list2.next
            next_sorted_node = next_sorted_node.next
        
        if list1:
            next_sorted_node.next = list1
        if list2:
            next_sorted_node.next = list2
        
        return new_head.next