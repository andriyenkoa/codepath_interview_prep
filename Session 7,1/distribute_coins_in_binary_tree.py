# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(node, parent):
            if not node:
                return 0

            moves = helper(node.left, node) + helper(node.right, node)
            x = node.val - 1
            if parent:
                parent.val += x
            moves += abs(x)
            return moves

        return helper(root, 0)
