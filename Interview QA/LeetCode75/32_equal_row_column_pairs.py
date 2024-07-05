from typing import List

class Solution:
    def equal_pairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        
        # Create a list of columns
        columns = [[grid[i][j] for i in range(n)] for j in range(n)]
        
        # Compare each row with each column
        for row in grid:
            for col in columns:
                if row == col:
                    count += 1
        
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.equal_pairs([[3,2,1],[1,7,6],[2,7,7]]))
