from typing import List

class Solution:
    def longest_subarray(self, nums: List[int]) -> int:
        left = 0
        zeros_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            max_length = max(max_length, right - left)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.longest_subarray([1,1,1,0,0,0,1,1,1,0]))