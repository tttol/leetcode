class Solution(object):
    class BinaryTree:
        class Node:
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
        
        def __init__(self):
            self.root = None
        
        def insert(self, val):
            if self.root is None:
                self.root = self.Node(val)
                return
            
            def _insert(node, val):
                if val < node.val:
                    if node.left is None:
                        node.left = self.Node(val)
                    else:
                        _insert(node.left, val)
                else:
                    if node.right is None:
                        node.right = self.Node(val)
                    else:
                        _insert(node.right, val)
            
            _insert(self.root, val)
            

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        binary_tree = self.BinaryTree()
        for e in nums1 + nums2:
            binary_tree.insert(e)

        

s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1,2], [3,4]))
