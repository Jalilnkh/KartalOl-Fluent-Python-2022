from typing import List

class Solution:
    def dominant_index(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        max_val = max(nums)
        temp = []

        for i in range(len(nums)):
            if nums[i] != max_val:
                temp.append(nums[i])
        if (max(temp)*2) <= max_val:
            return nums.index(max_val)

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.dominant_index([3,9,1,0]))