# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        prev, curr = None, head

        while curr and curr != slow:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr.next = prev
        if not fast:
            curr = curr.next

        left = curr
        while left and right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
