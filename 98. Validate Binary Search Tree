# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive DFS O(2n)
        # update range boundaries and check that each node's val is within range
        def validateSubtree(node, left, right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            return (validateSubtree(node.left, left, node.val) and validateSubtree(node.right, node.val, right))
        
        return validateSubtree(root, float("-inf"), float("inf"))
