from typing import List

class Solution:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        elif n == 1:
            return cost[0]
        
        # Initialize the first two steps
        dp0 = 0
        dp1 = 0
        
        for i in range(2, n + 1):
            current = min(dp0 + cost[i - 2], dp1 + cost[i - 1])
            dp0, dp1 = dp1, current
        
        return dp1


if __name__ == "__main__":
    sol = Solution()
    print(sol.min_cost_climbing_stairs([10,15,20]))