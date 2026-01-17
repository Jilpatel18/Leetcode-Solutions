"""
LeetCode 692. Top K Frequent Words

Category: Hash Map
Tags: Sorting, String

Approach:
- Use a hash map (dictionary) to count the frequency of each word.
- Convert the dictionary into a list of (word, frequency) pairs.
- Sort the list:
  - First by frequency in descending order.
  - Then by word in lexicographical (alphabetical) order.
- Return the first k words from the sorted list.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1

        items = list(freq.items())
        items.sort(key=lambda x: (-x[1], x[0]))

        return [word for word, count in items[:k]]
