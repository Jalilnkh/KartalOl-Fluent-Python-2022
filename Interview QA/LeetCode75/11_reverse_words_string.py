class Solution:
    def reverse_words(self, s: str) -> str:
        s= ' '.join(s.split())
        words = s.split(" ")
        words = words[::-1]
        return ' '.join(words)
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse_words(s='Jalil var yux'))