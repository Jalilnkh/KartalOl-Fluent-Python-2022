from typing import List

class Solution:
    def max_score(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Pair the elements from nums1 and nums2 and sort by the elements in nums2 in descending order
        paired = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        
        min_heap = []
        sum_nums1 = 0
        max_score = 0
        
        # Function to push an element into the heap
        def heap_push(heap, value):
            heap.append(value)
            heap.sort()  # Sorting after each insertion to maintain heap property
        
        # Function to pop the smallest element from the heap
        def heap_pop(heap):
            return heap.pop(0)
        
        # Iterate through the paired list
        for num1, num2 in paired:
            heap_push(min_heap, num1)
            sum_nums1 += num1
            
            if len(min_heap) > k:
                sum_nums1 -= heap_pop(min_heap)
            
            if len(min_heap) == k:
                max_score = max(max_score, sum_nums1 * num2)
        
        return max_score


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_score([1,3,3,2], [2,1,3,4], 3))
