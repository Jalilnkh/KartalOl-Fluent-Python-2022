from typing import List

class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if len(strs) == "":
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
    
        return prefix

if __name__ == "__main__":
    sol = Solution()
    print(sol.longest_common_prefix(['flower', 'flight', "f"]))