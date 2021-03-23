"""
Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.



"""
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        flatten = sum (mat, []) # expand the two-dimensional matrix into one dimension
        print(flatten)
        dic = Counter (flatten) # count all element frequencies
        print(dic)
        for num in mat [0]:
            # In the first row of elements, find if there is an element with a frequency equal to the number of mat rows
            if dic [num] == len(mat): # The element that satisfies the condition for the first time is the answer
                return num
        return -1
#         M = len(mat[0])
#         N = len(mat)
#         print(N)
#         dict = defaultdict(int)
#         for j in range(M):
#             for i in range(N):
#                 dict[mat[i][j]]+=1
#                 if dict[mat[i][j]] == N:
#                     return mat[i][j]
#         # for key, value in dict.items():
#         #     if value == len(mat):
#         #         return key
            
#         return -1