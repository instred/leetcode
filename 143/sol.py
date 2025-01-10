from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        t, h = head, head.next
        while h and h.next:
            t = t.next
            h = h.next.next
        
        l2 = t.next
        prev = t.next = None
        
        while l2:
            tmp = l2.next
            l2.next = prev
            prev = l2 
            l2 = tmp

        
        l1, l2 = head, prev
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2

        return head


        

if __name__ == "__main__":
    sol = Solution()
    lis = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    a = sol.reorderList(lis)
    while a:
        print(a.val)
        a = a.next