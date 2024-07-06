class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # Initialize the first three Tribonacci numbers
        T0, T1, T2 = 0, 1, 1
        
        # Compute the N-th Tribonacci number iteratively
        for i in range(3, n + 1):
            Tn = T0 + T1 + T2
            T0, T1, T2 = T1, T2, Tn
        
        return Tn
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.tribonacci(3))