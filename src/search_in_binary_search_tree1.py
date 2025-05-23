# https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert(self, root: TreeNode, value: int):
        if root == None:
            return TreeNode(value)
        
        if root.val == value:
            return root
        
        if root.val < value:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)
        return root
      
    def search(self, root: TreeNode, value: int) -> TreeNode:
        if root.val == value:
            return root
        
        if root.val < value:
            if root.right is None:
                return None
            
            return self.search(root.right, value)
        else:
            if root.left is None:
                return None
            
            return self.search(root.left, value)
            
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        root_node = TreeNode(root[0])
        for i in range(1, len(root)):
            root_node = self.insert(root_node, root[i])
        
        node = self.search(root_node, val)

        if node is None: 
            return []
        
        ans = [node.val]
        if node.left is not None: 
            ans.append(node.left.val)
        if node.right is not None:
            ans.append(node.right.val)

        return ans


s = Solution()
print(s.searchBST(root = [4,2,7,1,3], val = 2))
print(s.searchBST(root = [4,2,7,1,3], val = 5))