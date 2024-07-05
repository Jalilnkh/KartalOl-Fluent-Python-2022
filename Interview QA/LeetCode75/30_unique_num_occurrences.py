from typing import List

class Solution:
    def unique_occurrences(self, arr: List[int]) -> bool:
        occurrence_count = {}
        for num in arr:
            if num in occurrence_count:
                occurrence_count[num] += 1
            else:
                occurrence_count[num] = 1

        # Create a set to store the occurrences
        occurrences = set()
        for count in occurrence_count.values():
            if count in occurrences:
                return False
            occurrences.add(count)

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.unique_occurrences([1,2,2,1,1,3]))