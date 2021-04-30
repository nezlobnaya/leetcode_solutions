class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        X, Y, output = [1], [1], []
        
        while X[-1] < bound and x!=1:
            X.append(X[-1] *x)
        while Y[-1] < bound and y!=1:
            Y.append(Y[-1] *y)
        
        print(X)
        print(Y)
        
        c = list(itertools.product(X,Y))
        for i, j in c:
            if i +j <=bound:
                output.append(i+j)
                
        return list(set(output))
        
# class Solution:
#     def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
#         output = []
#         for i in range(20):
#             for j in range(20):
#                 target = x**i + y**j
#                 if target <= bound:
#                     if target not in output:
#                         output.append(target)
#         return output