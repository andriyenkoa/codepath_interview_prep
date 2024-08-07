# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_idx = 0
        self.inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            node_val = preorder[self.preorder_idx]
            node = TreeNode(val=node_val)
            self.preorder_idx += 1

            node.left = helper(left, self.inorder_idx_map[node_val] - 1)
            node.right = helper(self.inorder_idx_map[node_val] + 1, right)

            return node

        return helper(0, len(inorder) - 1)
