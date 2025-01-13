from typing import Optional
from collections import defaultdict

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        start = head
        copies = defaultdict(lambda: Node(0))
        copies[None] = None

        while start:
            copies[start].val = start.val
            copies[start].next = copies[start.next]
            copies[start].random = copies[start.random]
            start = start.next

        return copies[head]