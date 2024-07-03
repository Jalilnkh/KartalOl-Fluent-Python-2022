class Solution:
    def increasing_triplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.increasing_triplet([1,2,3,4]))