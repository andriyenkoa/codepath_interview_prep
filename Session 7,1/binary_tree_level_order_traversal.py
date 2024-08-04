# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.depth = []

        def traverse(node, cur_depth):
            if not node:
                return
            if cur_depth < len(self.depth):
                self.depth[cur_depth].append(node.val)
            else:
                self.depth.append([node.val])

            traverse(node.left, cur_depth + 1)
            traverse(node.right, cur_depth + 1)

        traverse(root, 0)
        return self.depth
