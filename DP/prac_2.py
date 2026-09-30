# LeetCode 70 — Climbing Stairs

class Solution:
    def climbStairs(self, n):

        dp = [-1] * (n + 1)

        def solve(i):

            # Base cases
            if i == 0:
                return 1

            if i == 1:
                return 1

            # Agar already calculate ho chuka hai
            if dp[i] != -1:
                return dp[i]

            # Recurrence
            dp[i] = solve(i - 1) + solve(i - 2)

            return dp[i]

        return solve(n)