class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        # Calculate left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Calculate right products and multiply with the corresponding left product
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.product_except_self([1,2,3]))