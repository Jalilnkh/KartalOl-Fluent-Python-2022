class Solution:
    def reverse_simple(self, x: int) -> int:
        if x == 0:
            return x
        div = abs(x)
        mod = []
        rev = 0
        i = 1
        while div > 0:
            mod.append(div % 10)
            div = div // 10
        j = 1
        for i in range(len(mod)):
            rev += mod.pop() * j
            j = j*10
        if x < 0:
            return -rev
        else:
            return rev
        
    def reverse_optim(self, x: int) -> int:
        rev = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x!= 0:
            pop = x % 10
            x = x // 10
            rev = rev * 10 + pop

        return sign * rev

if __name__ == "__main__":
    nums1 = -1230
    sol = Solution()
    print(sol.reverse_optim(nums1))