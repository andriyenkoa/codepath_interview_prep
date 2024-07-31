from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_to_stack(self, node):
        stack = []

        while node:
            stack.append(node.val)
            node = node.next

        return stack

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = self.add_to_stack(l1)
        stack2 = self.add_to_stack(l2)

        carry = 0
        result = None
        while stack1 or stack2 or carry:
            digit1 = stack1.pop() if stack1 else 0
            digit2 = stack2.pop() if stack2 else 0
            summ = digit1 + digit2 + carry

            carry = summ // 10
            summ = summ % 10

            node = ListNode(val=summ)
            node.next = result
            result = node

        return result
