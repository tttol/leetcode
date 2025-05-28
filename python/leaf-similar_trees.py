# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.leaves1 = []
        self.leaves2 = []

    def get_leaf(self, node: TreeNode, leaves: List):
        if node == None:
            return
        
        if node.left == None and node.right == None:
            leaves.append(node.val)
        self.get_leaf(node.left, leaves)
        self.get_leaf(node.right, leaves)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.get_leaf(root1, self.leaves1)
        self.get_leaf(root2, self.leaves2)
        return self.leaves1 == self.leaves2