# 321. Frog Jump

class Solution:
    def frogJump(self, heights):
        n = len(heights)

        dp = [0] * n

        dp[0] = 0

        for i in range(1, n):
            one_jump = dp[i-1] + abs(heights[i] - heights[i-1])

            two_jump = float('inf')

            if i > 1:
                two_jump = dp[i-2] + abs(heights[i] - heights[i-2])

            dp[i] = min(one_jump, two_jump)

        return dp[n-1]