from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        a = None

        while head:
            tmp = ListNode(head.val)
            tmp.next = a
            a = tmp
            head = head.next

        return a

if __name__ == "__main__":
    sol = Solution()
    lis = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    a = (sol.reverseList(lis))
    while a:
        print(a.val)
        a = a.next
