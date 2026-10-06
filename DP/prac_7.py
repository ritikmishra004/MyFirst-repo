# 125. Ninja's training

'''A ninja has planned a n-day training schedule. Each day he has to perform one of three activities
- running, stealth training, or fighting practice. The same activity cannot be done on two consecutive
days and the ninja earns a specific number of merit points, based on the activity and the given day.

Given a n x 3-sized matrix, where matrix[i][0], matrix[i][1], and matrix[i][2], represent the merit 
points associated with running, stealth and fighting practice, on the (i+1)th day respectively. 
Return the maximum possible merit points that the ninja can earn.'''

class Solution:
    def ninjaTraining(self, matrix):
        n = len(matrix)

        dp = [[0] * 3 for _ in range(n)]

        # Day 1
        dp[0][0] = matrix[0][0]
        dp[0][1] = matrix[0][1]
        dp[0][2] = matrix[0][2]

        # Remaining days
        for day in range(1, n):

            # Today = Running
            dp[day][0] = matrix[day][0] + max(
                dp[day-1][1],
                dp[day-1][2]
            )

            # Today = Stealth
            dp[day][1] = matrix[day][1] + max(
                dp[day-1][0],
                dp[day-1][2]
            )

            # Today = Fighting
            dp[day][2] = matrix[day][2] + max(
                dp[day-1][0],
                dp[day-1][1]
            )

        return max(dp[n-1])