from typing import List

class Solution:
    def pivot_index(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num

        return -1
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.pivot_index([1,7,3,6,5,6]))