class Solution:
    def search_insert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left


if __name__ == "__main__":
    sol = Solution()
    print(sol.search_insert([1,2,2,4,5],2))