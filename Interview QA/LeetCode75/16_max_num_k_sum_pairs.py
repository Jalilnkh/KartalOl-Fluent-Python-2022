class Solution:
    def max_operations(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return count
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.max_operations(nums=[1,2,1,3,4], k=5))