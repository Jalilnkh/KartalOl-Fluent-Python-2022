
class Solution:
    def decode_string(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ''
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_str = ''
                current_num = 0
            elif char == ']':
                last_str, num = stack.pop()
                current_str = last_str + num * current_str
            else:
                current_str += char
        
        return current_str


if __name__ == "__main__":
    sol = Solution()
    print(sol.decode_string("3[a]2[bc]"))
