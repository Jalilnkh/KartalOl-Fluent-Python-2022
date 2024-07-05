class Solution:
    def remove_stars(self, s: str) -> str:
        stack = []
    
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.remove_stars("leet**cod*e"))
