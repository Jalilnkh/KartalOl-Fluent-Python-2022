from typing import List

class Solution:
    def count_bits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
    
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_bits(5))