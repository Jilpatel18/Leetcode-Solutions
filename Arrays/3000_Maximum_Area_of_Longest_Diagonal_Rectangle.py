
"""
LeetCode 3000. Maximum Area of Longest Diagonal Rectangle

Approach:
- For each rectangle, compute diagonal^2 = l*l + w*w (no need of sqrt).
- Track the maximum diagonal length.
- If multiple rectangles have same diagonal, choose the one with maximum area.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def areaOfMaxDiagonal(self, dimensions):
        max_diag = 0
        max_area = 0

        for l, w in dimensions:
            diag_sq = l * l + w * w
            area = l * w

            if diag_sq > max_diag:
                max_diag = diag_sq
                max_area = area
            elif diag_sq == max_diag:
                max_area = max(max_area, area)

        return max_area
