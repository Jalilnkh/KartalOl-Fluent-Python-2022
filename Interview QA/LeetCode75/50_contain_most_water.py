from typing import List

class Solution:
    def max_area(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Calculate the area
            width = right - left
            h = min(height[left], height[right])
            current_water = width * h

            # Update maximum water
            max_water = max(max_water, current_water)

            # Move the pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_area([1,8,6,2,5,4,8,3,7]))
