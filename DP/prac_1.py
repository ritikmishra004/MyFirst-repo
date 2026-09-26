# LeetCode 70 — Climbing Stairs
class Solution:
    def climbStairs(self, n):

        if n == 1:
            return 1

        prev2 = 1   # ways(0)
        prev1 = 1   # ways(1)

        for i in range(2, n + 1):
            current = prev1 + prev2

            prev2 = prev1
            prev1 = current

        return prev1