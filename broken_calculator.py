class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        operations = 0
        while X != Y:
            if Y < X:
                operations += (X-Y)
                X=Y
            else:
                if Y %2 == 0:
                    Y//=2
                else:
                    Y+=1
                operations+=1
        return operations 

if __name__ == '__main__':
    X = 1024
    Y = 1
    print(f'number of steps required:{Solution().brokenCalc(X,Y)}')
