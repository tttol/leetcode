# Binary Search Tree
### insert
```mermaid
graph TD
    A[Start Insert(root, value)] --> B{root is None?};
    B -- Yes --> C[new_node = TreeNode(value)];
    C --> D[Return new_node];
    D --> Z[End Insert];
    B -- No --> E{root.val == value?};
    E -- Yes --> F[Return root (value already exists)];
    F --> Z;
    E -- No --> G{root.val < value?};
    G -- Yes --> H[root.right = Insert(root.right, value)];
    H --> F;
    G -- No --> I[root.left = Insert(root.left, value)];
    I --> F;
```

### search
```mermaid
graph TD
    SA[Start Search(root, value)] --> SB{root.val == value? (Assuming root is not None for initial call)};
    SB -- Yes --> SC[Return root];
    SC --> SZ[End Search];
    SB -- No --> SD{root.val < value?};
    SD -- Yes --> SE{root.right is None?};
    SE -- Yes --> SF[Return None (value not found)];
    SF --> SZ;
    SE -- No --> SG[Return Search(root.right, value)];
    SG --> SZ;
    SD -- No --> SH{root.left is None? (Implies root.val > value)};
    SH -- Yes --> SI[Return None (value not found)];
    SI --> SZ;
    SH -- No --> SJ[Return Search(root.left, value)];
    SJ --> SZ;
```

### python implementation
```py
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
```
- 参考：https://www.geeksforgeeks.org/binary-search-tree-in-python/