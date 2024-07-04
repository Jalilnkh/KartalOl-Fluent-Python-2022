class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
    
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
        
        return matrix


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))