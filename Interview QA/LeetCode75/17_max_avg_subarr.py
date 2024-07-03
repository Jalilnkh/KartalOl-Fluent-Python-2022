class Solution:
    def find_max_average(self, nums: list[int], k: int) -> float:
        # Calculate the sum of the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Slide the window over the rest of the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        return max_sum / k
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.find_max_average(nums=[1,2,1,3,4], k=5))