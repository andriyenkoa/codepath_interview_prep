# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.num_of_paths = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.dfs(root, targetSum)
        return self.num_of_paths

    def dfs(self, root, target):
        if not root:
            return

        self.test_result(root, target)
        self.pathSum(root.left, target)
        self.pathSum(root.right, target)

    def test_result(self, node, target):
        if not node:
            return
        if node.val == target:
            self.num_of_paths += 1

        self.test_result(node.left, target - node.val)
        self.test_result(node.right, target - node.val)
