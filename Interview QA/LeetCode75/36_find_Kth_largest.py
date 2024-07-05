from typing import List

class Solution:
    def find_Kth_largest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        def quickselect(left, right, k):
            if left == right:
                return nums[left]

            pivot_index = partition(left, right)

            if k == pivot_index:
                return nums[k]
            elif k < pivot_index:
                return quickselect(left, pivot_index - 1, k)
            else:
                return quickselect(pivot_index + 1, right, k)

        # Start the quickselect process to find the k-1 largest element
        return quickselect(0, len(nums) - 1, k - 1)



if __name__ == "__main__":
    sol = Solution()
    print(sol.find_Kth_largest([3,2,1,5,6,4], 2))
