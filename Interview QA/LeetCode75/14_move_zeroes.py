class Solution:
    def move_zeroes(self, nums: list[int]) -> list:
        n = len(nums)
        last_non_zero_found_at = 0

        # Move all the non-zero elements to the beginning of the array
        for i in range(n):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1

        # Fill the remaining array with zeros
        for i in range(last_non_zero_found_at, n):
            nums[i] = 0
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.move_zeroes([1,0,3,4]))