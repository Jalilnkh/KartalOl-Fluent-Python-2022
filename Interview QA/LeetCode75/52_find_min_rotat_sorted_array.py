from typing import List

class Solution:
    def find_min(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]


if __name__ == "__main__":
    sol = Solution()
    print(sol.find_min("()[]{}"))
