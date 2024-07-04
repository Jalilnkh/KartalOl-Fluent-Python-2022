class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return result
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1,2,2,4,5]))