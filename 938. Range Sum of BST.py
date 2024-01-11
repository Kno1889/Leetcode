# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.range_sum = 0
        
        def traverse(node):
            if node:
                if node.val >= low and node.val <= high:
                    self.range_sum += node.val
                
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
            else:
                return
        
        traverse(root)
        return self.range_sum