# 198. House Robber

class Solution:
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            skip = dp[i-1]

            rob = dp[i-2] + nums[i]

            dp[i] = max(skip, rob)

        return dp[n-1]