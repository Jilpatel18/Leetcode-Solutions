"""
LeetCode 104. Maximum Depth of Binary Tree

Category: Tree
Tags: BFS, Queue, Binary Tree

Approach:
- Use Breadth-First Search (BFS) to traverse the tree level by level.
- Each level processed represents one depth increment.
- Use a queue to store nodes of the current level.
- Continue traversal until all levels are processed.
- The total number of levels traversed is the maximum depth.

Time Complexity: O(n)
Space Complexity: O(n)   (queue can hold all nodes at the widest level)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        
        q = deque([root])
        depth = 0
        
        while q:
            level_size = len(q)
            depth += 1
            
            for _ in range(level_size):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return depth
