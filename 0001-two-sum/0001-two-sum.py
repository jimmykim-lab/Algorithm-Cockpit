#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            Approach : One-pass Hash Map
            Time complexity : O(n) - Traverse the list containing n elements ONLY ONCE
                              Each lookup in the hash map costs O(1) time
            Space complexity : O(n) - The extra space required depends on the number of items stored in the hash map (at most n elements)
                               It is trade-off with time complexity. With this space complexity, time complexity can be reduced from O(n^2) to O(n)
        """

        # A dictionary to store the value as key and its index as value
        hash_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            # Check if the 'diff' already exists in hash map
            if diff in hash_map:
                # If the diff already exists in hash map, return index of diff and index(i) of current value(n)
                return [hash_map[diff], i]
        
            # If the diff doesn't exists in hash map, store the current value(n) and its index(i) for future lookup
            hash_map[n] = i

# @lc code=end

