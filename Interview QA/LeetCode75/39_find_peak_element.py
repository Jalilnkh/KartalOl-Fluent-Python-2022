from typing import List

class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # If the middle element is greater than the next element,
                # then the peak element must be in the left half.
                right = mid
            else:
                # If the middle element is less than or equal to the next element,
                # then the peak element must be in the right half.
                left = mid + 1
        
        # At the end, left will be pointing to the peak element.
        return left


if __name__ == "__main__":
    sol = Solution()
    print(sol.find_peak_element([1,2,3,1]))