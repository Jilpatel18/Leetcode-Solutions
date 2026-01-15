"""
LeetCode 9. Palindrome Number

Approach:
- Convert the integer into a string.
- Reverse the string using slicing.
- If the original string and reversed string are same, it is a palindrome.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def isPalindrome(self, x):
        s1 = str(x)
        s2 = s1[::-1]

        if s1 == s2:
            return True
        return False
