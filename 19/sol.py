from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution2:

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = self.reverse(head)

        start = reversed = prev
        counter = 1
        prev = None
        curr = reversed
        nextt = reversed.next
        removed = False

        while reversed.next:
            if counter == n:
                if not prev:
                    break
                prev.next = nextt
                removed = True
                break 
            
            prev = curr
            curr = nextt
            nextt = nextt.next
            counter += 1

        if not removed: start = start.next
        head = self.reverse(start)

        return head
    
class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head

        for _ in range(n): 
            fast = fast.next

        if not fast.next:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))  
    n = 2  
    head2 = ListNode(1)  
    n2 = 1  
    head3 = ListNode(1, ListNode(2))
    n3 = 1