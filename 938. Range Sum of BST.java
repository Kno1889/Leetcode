  //Definition for a binary tree node.
  public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
 }
 }
class Solution {
    int answer;
    public int rangeSumBST(TreeNode root, int L, int R) {
        answer = 0;
        TreeNode c = root;
        addition(c, L, R);
        return answer;
    }
    
    public void addition(TreeNode n, int L, int R){ //recursively go through                                                the BST and add when appropriate
        if(n != null){
            if(n.val >= L && n.val <= R)
                answer += n.val;
            if(n.val < R)
                addition(n.right, L, R);
            if(L < n.val)
                addition(n.left, L, R);
        }
    }
}
