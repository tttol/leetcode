# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        current_node = None
        if list1.val < list2.val:
            current_node = ListNode(list1.val)
            pointer1 = list1.next
            pointer2 = list2
        else:
            current_node = ListNode(list2.val)
            pointer1 = list1
            pointer2 = list2.next
        ans = current_node
        
        while pointer1 != None and pointer2 != None:
            if pointer1.val < pointer2.val:
                current_node.next = ListNode(pointer1.val)
                pointer1 = pointer1.next
            else:
                current_node.next = ListNode(pointer2.val)
                pointer2 = pointer2.next

            current_node = current_node.next

        if pointer1 != None:
            current_node.next = pointer1
        elif pointer2 != None:
            current_node.next = pointer2

        return ans