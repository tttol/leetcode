# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 模範回答
# https://leetcode.com/problems/reverse-linked-list/solutions/2682085/java-0ms-100-easy-understanding/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev = None
        while current_node != None:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
        return prev

if __name__ == "__main__":
    s = Solution()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(s.reverseList(node))