# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(next=head)

        slow = temp
        fast = temp.next
        while fast:
            if fast.val != val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = fast

        return temp.next
