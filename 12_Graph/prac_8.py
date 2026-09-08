# rotten orange leetcode 994
# we will do this question using bfs traversal
# because we have to do level wise work for this

# Rotten Oranges Problem (LeetCode 994)
# -------------------------------------
# 0 -> empty cell
# 1 -> fresh orange
# 2 -> rotten orange
# Task: Find minimum time (minutes) required so that no fresh orange remains
# If impossible -> return -1

from collections import deque   # queue for BFS

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])   # grid dimensions
    q = deque()   # BFS queue to hold rotten oranges
    fresh = 0     # count of fresh oranges

    # Step 1: Traverse the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))   # push rotten orange into queue
            elif grid[r][c] == 1:
                fresh += 1         # count fresh orange

    # If there are no fresh oranges -> answer is 0
    if fresh == 0:
        return 0

    # Directions for 4-neighbours (up, down, left, right)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    minutes = 0   # time counter

    # Step 2: BFS traversal (multi-source)
    while q:
        # Process all rotten oranges of current minute
        for _ in range(len(q)):
            r, c = q.popleft()

            # Explore 4-directional neighbours
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if neighbour is valid and fresh
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2     # make fresh -> rotten
                    q.append((nr, nc))   # add to queue for next round
                    fresh -= 1           # one fresh orange less

        minutes += 1   # after finishing one level = 1 minute passed

    # Step 3: Result
    return minutes - 1 if fresh == 0 else -1


# -----------------------------
# Driver Code for VS Code
# -----------------------------
if __name__ == "__main__":
    # Example input
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]

    result = orangesRotting(grid)
    print("Minimum minutes required:", result)
