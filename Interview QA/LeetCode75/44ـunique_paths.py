class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
    
        # Fill the dp array using the transition relation
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The result is the value at the bottom-right corner of the grid
        return dp[m-1][n-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.unique_paths(3, 7))