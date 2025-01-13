from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = '', ''
        while l1:
            n1 = str(l1.val) + n1
            l1 = l1.next

        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next

        n3 = (str(int(n1)+int(n2)))[::-1]
        ans = newhead = ListNode()

        for ch in n3:
            newhead.next = ListNode(int(ch))
            newhead = newhead.next

        return ans.next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ans = l3 = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            digit, carry = carry % 10, carry // 10
            l3.next = ListNode(digit)
            l3 = l3.next

        return ans.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(9)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.next.next.next = ListNode(9)
    print(s.addTwoNumbers(l1,l2))