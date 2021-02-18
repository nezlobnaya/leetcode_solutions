from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        
    def transpose(self,matrix):
        n = len(matrix)
        for i in range(n):
            j=i
            for j in range(j, n):
                temp = matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]= temp
            
            
    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j]= matrix[i][n-1-j]
                matrix[i][n-1-j]=temp
  
        