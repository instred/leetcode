from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num3 = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        print(num1, num2, num3)
        dummy = ListNode(0)
        current = dummy

        for n in num3:
            current.next = ListNode(int(n))
            current = current.next

        return dummy.next
    

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