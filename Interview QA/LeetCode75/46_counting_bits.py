from typing import List

class Solution:
    def count_bits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        offset = 1
    
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            res[i] = 1 + res[i - offset]
        
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_bits(5))