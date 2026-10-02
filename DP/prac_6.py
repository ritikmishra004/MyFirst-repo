# 114. Maximum Sum of Non-Adjacent Elements

'''Given an integer array nums of size n. Return the maximum sum possible using the
elements of nums such that no two elements taken are adjacent in nums.'''

# Example 1:
# Input: nums = [1, 2, 4]
# Output: 5
# Explanation:
# [1, 2, 4], the underlined elements are taken to get the maximum sum.

class Solution:
    def maximumNonAdjacentSum(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):

            skip = dp[i - 1]

            take = dp[i - 2] + nums[i]

            dp[i] = max(skip, take)

        return dp[n - 1]