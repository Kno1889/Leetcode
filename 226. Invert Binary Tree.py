# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(n) time complexity
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = root

        def swap(node):
            if not node:
                return
            
            temp = node.left
            node.left = node.right
            node.right = temp
            

            swap(node.left)
            swap(node.right)
        swap(dummy)

        return root
