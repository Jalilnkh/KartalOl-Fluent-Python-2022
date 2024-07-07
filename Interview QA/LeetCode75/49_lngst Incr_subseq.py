from typing import List

class Solution:
    def length_OfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    sol = Solution()
    print(sol.length_OfLIS([10,9,2,5,3,7,101,18]))