class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(char in it for char in s)
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.is_subsequence(s='ab', t='abc'))