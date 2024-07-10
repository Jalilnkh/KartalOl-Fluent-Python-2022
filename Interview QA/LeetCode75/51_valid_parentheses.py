class Solution:
    def is_valid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                # Pop the top element if available, else use a dummy value
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_valid("(()[]{})"))