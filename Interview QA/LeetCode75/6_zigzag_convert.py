class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        go_down = False
        cur_row = 0
        for char in s:
            rows[cur_row] +=char
            if cur_row == 0 or cur_row == numRows-1:
                go_down = not go_down
            cur_row +=1 if go_down else -1
        return ''.join(rows)


if __name__ == "__main__":
    s = 'ARDABILIAM'
    rows = 3
    sol = Solution()

    print(sol.convert(s,rows))