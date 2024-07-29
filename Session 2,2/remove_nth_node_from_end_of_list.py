# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = slow = fast = ListNode(next=head)
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return temp.next
