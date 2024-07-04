class Solution:
    def single_number(self, nums: list[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.single_number([1,2,2,4,4]))