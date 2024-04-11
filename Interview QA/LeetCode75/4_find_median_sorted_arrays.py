class Solution:
    def find_median_sorted_arrays_simple(self, nums1: list[int], nums2: list[int]) -> float:
        total = nums1 + nums2
        total = sorted(total)
        if int(len(total) % 2) == 0:
            return ((total[int(len(total)/2)-1] + total[(int(len(total)/2))])) / 2
        else:
            return total[int(len(total)/2)]
    
    def find_median_sorted_arrays_optimize(self, nums1, nums2):
        # Ensure nums1 is the shorter array to minimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        
        # Binary search on the shorter array
        left, right = 0, m
        while left < right:
            i = (left + right) // 2
            j = half_len - i
            if nums1[i] < nums2[j-1]:
                left = i + 1
            else:
                right = i
                
        i = left
        j = half_len - i
        
        # Handle edge cases where the partition falls at the beginning or end of an array
        max_of_left = max(nums1[i-1] if i > 0 else float('-infinity'),
                        nums2[j-1] if j > 0 else float('-infinity'))
        
        if (m + n) % 2 == 1:
            return max_of_left
        
        min_of_right = min(nums1[i] if i < m else float('infinity'),
                        nums2[j] if j < n else float('infinity'))
        
        return (max_of_left + min_of_right) / 2.0

        

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    sol = Solution()
    print(sol.find_median_sorted_arrays_simple(nums1, nums2))
    print(sol.find_median_sorted_arrays_optimize(nums1, nums2))