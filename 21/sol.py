from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        ans = head
        while list1 and list2:

            if list1.val <= list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next

            elif list1.val > list2.val:
                head.next = ListNode(list2.val)
                list2 = list2.next
                
            head = head.next

        head.next = list1 or list2

        return ans.next

if __name__ == "__main__":
    sol = Solution()
    lis = ListNode(1, ListNode(2, ListNode(4)))
    lis2 = ListNode(1, ListNode(3, ListNode(4)))
    a = (sol.mergeTwoLists(lis, lis2))
    while a:
        print(a.val)
        a = a.next