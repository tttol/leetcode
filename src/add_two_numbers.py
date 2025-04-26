# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sum = self.reversed_sum(l1) + self.reversed_sum(l2)
        if sum == 0:
            return ListNode()
            
        head = None
        current = None
        while sum > 0:
            digit = sum % 10
            sum = sum // 10
            if head is None:
                head = ListNode(digit)
                current = head
            else:
                current.next = ListNode(digit)
                current = current.next
                
        return head
    
    def reversed_sum(self, node):
        sum = 0
        multiplier = 1
        while node is not None:
            sum += node.val * multiplier
            multiplier *= 10
            node = node.next
        return sum
      
        
s = Solution()
res = s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
while res is not None:
    print(res.val)
    res = res.next
# print(s.addTwoNumbers([0], [0]))
# print(s.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))