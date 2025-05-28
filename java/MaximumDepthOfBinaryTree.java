
public class MaximumDepthOfBinaryTree {
  public static void main(String[] args) {

  }

  static final int SEARCHED = 1000;
  public int maxDepth(TreeNode root) {
    if (root == null) return 0;
    return dfs(root, 1);
  }

  public int dfs(TreeNode node, int count) {
    if (node == null) {
      return count;
    }

    node.val = SEARCHED;
    var l = node.left;
    var r = node.right;
    
    if (isSearched(l) && isSearched(r)) {
      return count;
    } else if(isSearched(l) && !isSearched(r)) {
      return dfs(r, ++count);
    } else if (!isSearched(l) && isSearched(r)) {
      return dfs(l, ++count);
    } else {
      // 左右どちらも未探索の場合は一旦左を探索
      return dfs(l, ++count);
    }
  }

  public boolean isSearched(TreeNode node) {
    return node == null || node.val == SEARCHED;
  }

  /**
   * Definition for a binary tree node.
   */
  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
      this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
  }

}