# Definition for a binary tree node.
import heapq
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.insert_to_heap(root)
        temp = 1
        while k > temp:
            heapq.heappop(self.heap)
            temp += 1
        return heapq.heappop(self.heap)

    def insert_to_heap(self, node):
        if node:
            heapq.heappush(self.heap, node.val)
            self.insert_to_heap(node.left)
            self.insert_to_heap(node.right)

    # in-order traversal solution
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node):
            nonlocal kthNode
            nonlocal k

            if not node or k < 0:
                return

            helper(node.left)

            k -= 1
            if k == 0:
                kthNode = node.val
                return

            helper(node.right)

        kthNode = 0
        helper(root)
        return kthNode
