# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = slow = head
        fast = slow.next

        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
            slow.next = fast
            slow = slow.next

        return temp
