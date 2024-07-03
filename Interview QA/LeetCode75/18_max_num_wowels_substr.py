class Solution:
    def max_vowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_count = current_count = 0
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_count = current_count
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_count += 1
            if s[i - k] in vowels:
                current_count -= 1
            max_count = max(max_count, current_count)
        
        return max_count
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.max_vowels(s='abscded', k=2))