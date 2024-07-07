from typing import List

class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        current_sum = 0
        max_sum = nums[0]
        
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))