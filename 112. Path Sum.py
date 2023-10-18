# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # while root.val + running_sum < targetSum:
        # also while root.left and root.right
        # if root.val + running_sum == targetSum return True
        # or just keep subtracting current val from targetSum. If you reach a leaf and remainder == 0 => return True
        # time O(n)
        def dfs(node, runningSum):
            if not node:
                return False
            
            runningSum += node.val

            if not node.left and not node.right:
                return runningSum == targetSum
            
            return (dfs(node.left, runningSum) or dfs(node.right, runningSum))
        return dfs(root, 0)
