from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.depth = depth

        def helper(node, val, cur_depth):
            if not node:
                return
            if cur_depth < self.depth:
                helper(node.left, val, cur_depth + 1)
                helper(node.right, val, cur_depth + 1)
                return
            left_node = node.left if node.left else None
            right_node = node.right if node.right else None
            node.left = TreeNode(val=val, left=left_node)
            node.right = TreeNode(val=val, right=right_node)

        if depth == 1:
            return TreeNode(val, root)

        helper(root, val, 2)
        return root
