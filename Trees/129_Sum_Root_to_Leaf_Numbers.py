"""
LeetCode 129. Sum Root to Leaf Numbers

Category: Tree
Tags: DFS, Stack, Binary Tree

Approach:
- Each root-to-leaf path represents a number formed by concatenating node values.
- Use Depth-First Search (DFS) with a stack to traverse the tree.
- Maintain the current number formed so far while traversing.
- When a leaf node is reached, add the formed number to the total sum.
- Continue until all root-to-leaf paths are processed.

Time Complexity: O(n)
Space Complexity: O(n)   (stack space in the worst case)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        stack = [(root, 0)]
        total = 0

        while stack:
            node, num = stack.pop()
            num = num * 10 + node.val

            if not node.left and not node.right:
                total += num

            if node.right:
                stack.append((node.right, num))
            if node.left:
                stack.append((node.left, num))

        return total
