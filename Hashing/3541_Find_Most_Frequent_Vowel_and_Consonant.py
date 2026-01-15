"""
LeetCode 3541. Find Most Frequent Vowel and Consonant

Approach:
- Use a dictionary to count frequency of each character.
- Find the maximum frequency among vowels (a, e, i, o, u).
- Find the maximum frequency among consonants.
- Return (max vowel frequency + max consonant frequency).

Time Complexity: O(n)
Space Complexity: O(1)   (since only lowercase English letters are possible)
"""


class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        vowels = "aeiou"
        max_vowel = 0
        max_consonant = 0

        for ch, count in freq.items():
            if ch in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_consonant = max(max_consonant, count)

        return max_vowel + max_consonant
