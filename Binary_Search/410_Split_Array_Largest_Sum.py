"""
LeetCode 410. Split Array Largest Sum

Category: Binary Search
Tags: Greedy, Prefix Sum

Approach:
- The answer lies between max(nums) and sum(nums).
- Use Binary Search on the possible maximum subarray sum.
- For a guessed value `mid`, check how many subarrays are needed
  if no subarray sum exceeds `mid`.
- If required subarrays <= k, try a smaller maximum (move left).
- Otherwise, increase the limit (move right).
- The smallest valid maximum sum is the answer.

Time Complexity: O(n log(sum(nums)))
Space Complexity: O(1)
"""

class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = max(nums), sum(nums)

        while l < r:
            mid = (l + r) // 2
            subarray = 1
            cur_sum = 0

            for num in nums:
                if cur_sum + num > mid:
                    subarray += 1
                    cur_sum = num
                else:
                    cur_sum += num

            if subarray <= k:
                r = mid
            else:
                l = mid + 1

        return l
