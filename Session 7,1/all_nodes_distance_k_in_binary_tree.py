# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parents(node, parent):
            if not node:
                return

            parent_map[node] = parent

            add_parents(node.left, node)
            add_parents(node.right, node)

        def check_path(node, cur_distance):
            if not node or node in seen or cur_distance > k:
                return

            seen.add(node)

            if cur_distance == k:
                results.append(node.val)
                return

            check_path(node.left, cur_distance + 1)
            check_path(node.right, cur_distance + 1)
            check_path(parent_map[node], cur_distance + 1)

        results = []
        seen = set()
        parent_map = {}

        add_parents(root, 0)
        check_path(target, 0)

        return results
