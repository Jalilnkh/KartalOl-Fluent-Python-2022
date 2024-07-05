from typing import List

class Solution:
    def find_difference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = list(set1 - set2)
        answer2 = list(set2 - set1)

        return [answer1, answer2]
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.find_difference([1,2,3,6,5,6], [1,7,3,6,5,7]))