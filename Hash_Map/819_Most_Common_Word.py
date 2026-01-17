"""
LeetCode 819. Most Common Word

Category: Hash Map
Tags: String, Frequency Counting

Approach:
- Convert the banned words list into a set for fast lookup.
- Convert the paragraph to lowercase to handle case insensitivity.
- Replace all non-alphabetic characters with spaces to clean the text.
- Split the cleaned string into words.
- Use a hash map to count frequencies of non-banned words.
- Track the word with the maximum frequency and return it.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_set = set()
        for b in banned:
            banned_set.add(b.lower())

        paragraph = paragraph.lower()

        clean = ""
        for ch in paragraph:
            if 'a' <= ch <= 'z':
                clean += ch
            else:
                clean += " "

        words = clean.split()

        freq = {}
        maxCount = 0
        ans = ""

        for w in words:
            if w not in banned_set:
                if w in freq:
                    freq[w] += 1
                else:
                    freq[w] = 1

                if freq[w] > maxCount:
                    maxCount = freq[w]
                    ans = w

        return ans
