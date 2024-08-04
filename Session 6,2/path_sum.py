# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pre_order_traversal(node, cur_sum):
            if not node:
                return False

            if not node.left and not node.right:
                return cur_sum + node.val == targetSum

            return pre_order_traversal(node.left, cur_sum + node.val) or \
                pre_order_traversal(node.right, cur_sum + node.val)

        return pre_order_traversal(root, 0)
