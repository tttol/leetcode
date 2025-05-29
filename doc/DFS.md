# DFS: Depth First Search
[1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)
<br>
![alt text](image-3.png)
```py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node: TreeNode, count: int, max_node: int) -> int:
        if node == None:
            return count
        
        if max_node <= node.val:
            count += 1
        
        max_node = max(max_node, node.val)
        count = self.dfs(node.left, count, max_node)
        count = self.dfs(node.right, count, max_node)

        return count
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, 0, root.val)

if __name__ == "__main__":
    sample1 = TreeNode(3, TreeNode(1, TreeNode(3), None), TreeNode(4, TreeNode(1), TreeNode(5)))
    sample2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)), None)
    sample3 = TreeNode(1)
    s = Solution()
    print(s.goodNodes(sample1))
    print(s.goodNodes(sample2))
    print(s.goodNodes(sample3))
```

### def goodNodes
```mermaid
graph TD
    A[Start goodNodes] --> B{Is root None?};
    B -- Yes --> C[Return 0];
    B -- No --> D[Call dfs on root];
    D --> E[Return dfs result];
    E --> F[End goodNodes];
```

### def dfs
```mermaid
graph TD
    A[Start dfs] --> B{Is node None?};
    B -- Yes --> C[Return count];
    B -- No --> D{Is current node good?};
    D -- Yes --> E[Increment count];
    D -- No --> F[No change to count];
    E --> G[Update max_node];
    F --> G;
    G --> H[Recurse left child];
    H --> I[Recurse right child];
    I --> J[Return count];
    J --> K[End dfs];
```