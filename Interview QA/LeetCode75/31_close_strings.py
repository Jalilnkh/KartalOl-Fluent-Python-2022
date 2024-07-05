
class Solution:
    def close_strings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # Count frequency of each character in both words
        count1 = {}
        count2 = {}
        for ch in word1:
            count1[ch] = count1.get(ch, 0) + 1
        for ch in word2:
            count2[ch] = count2.get(ch, 0) + 1

        # Check if both words have the same set of unique characters
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Check if both words have the same frequency counts
        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.close_strings(word1="abc", word2="bca"))