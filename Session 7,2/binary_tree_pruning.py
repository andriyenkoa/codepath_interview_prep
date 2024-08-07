# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return False
            left = helper(node.left)
            right = helper(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return node.val == 1 or left or right
        res = helper(root)
        if not res:
            return None
        return root
