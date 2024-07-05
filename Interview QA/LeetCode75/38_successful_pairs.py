from typing import List

class Solution:
    def successful_pairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
    
        def binary_search(spell):
            # Binary search to find the first potion that forms a successful pair with the spell
            left, right = 0, len(potions)
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1
            return len(potions) - left

        # For each spell, use binary search to count the successful pairs
        result = [binary_search(spell) for spell in spells]
        return result


if __name__ == "__main__":
    sol = Solution()
    spells = [5,1,3]
    potions = [1,2,3,4,5]
    success = 7
    print(sol.successful_pairs(spells, potions, success))