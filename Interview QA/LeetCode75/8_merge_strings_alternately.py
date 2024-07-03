class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        merged_string = []
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)

        # Add characters in alternating order
        for i in range(min_len):
            merged_string.append(word1[i])
            merged_string.append(word2[i])

        # Append remaining characters from the longer string
        if len1 > len2:
            merged_string.extend(word1[min_len:])
        else:
            merged_string.extend(word2[min_len:])

        return ''.join(merged_string)
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge_alternately(word1='Jalil', word2='Kartal'))