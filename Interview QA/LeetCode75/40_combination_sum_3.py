from typing import List

class Solution:
    def combination_sum_3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, k, n):
            if k == 0 and n == 0:
                result.append(path)
                return
            if k == 0 or n == 0:
                return
            for i in range(start, 10):
                if i > n:  # Early stopping
                    break
                backtrack(i + 1, path + [i], k - 1, n - i)
        
        result = []
        backtrack(1, [], k, n)
        return result



if __name__ == "__main__":
    sol = Solution()
    print(sol.combination_sum_3(3, 7))