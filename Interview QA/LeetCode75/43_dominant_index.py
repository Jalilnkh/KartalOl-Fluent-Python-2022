from typing import List

class Solution:
    def dominant_index(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        max_index = 0
        max_value = nums[0]

        # Find the index of the largest element
        for i in range(1, len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
                max_index = i

        # Check if the largest element is at least twice as large as all other elements
        for i in range(len(nums)):
            if i != max_index and nums[i] * 2 > max_value:
                return -1

        return max_index


if __name__ == "__main__":
    sol = Solution()
    print(sol.dominant_index([3,6,1,0]))