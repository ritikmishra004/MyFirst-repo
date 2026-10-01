# 714. Frog jump with K distances

class Solution:
    def frogJump(self, heights, k):
        n = len(heights)

        dp = [0] * n

        for i in range(1, n):

            dp[i] = float('inf')

            for j in range(max(0, i-k), i):

                energy = dp[j] + abs(heights[i] - heights[j])

                dp[i] = min(dp[i], energy)

        return dp[n-1]