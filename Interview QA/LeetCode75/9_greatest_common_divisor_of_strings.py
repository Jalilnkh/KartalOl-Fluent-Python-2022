class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]



if __name__ == "__main__":
    sol = Solution()
    print(sol.gcd_of_strings(str1='Jalil', str2='Kartal'))