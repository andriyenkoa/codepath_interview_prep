# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(node, cur_path):
            if not node:
                return None

            cur_path.append(str(node.val))

            if not node.left and not node.right:
                all_paths.append("->".join(cur_path))

            helper(node.left, cur_path)
            helper(node.right, cur_path)

            cur_path.pop()

        all_paths = []
        helper(root, [])

        return all_paths
