class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        temp_chars = []
        main_chars = []
        for char in s:
            temp_chars.append(char)
            if len(set(temp_chars)) != len(temp_chars):
                if len(main_chars) < len(temp_chars):
                    main_chars = temp_chars[:-1]
                temp_chars = [temp_chars[-1]]
        return len(main_chars)
    

if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    print(sol.length_of_longest_substring(s))