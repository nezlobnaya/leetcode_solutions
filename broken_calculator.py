import unittest
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

class TestSum(unittest.TestCase):

    def test_sum_1(self):
        self.assertEqual(Solution().brokenCalc(2,3),2, "should be 2")
    
    def test_sum_2(self):
        self.assertEqual(Solution().brokenCalc(5,8),2, "should be 2")
    
    def test_sum_3(self):
        self.assertEqual(Solution().brokenCalc(3,10),3, "should be 3")
    
    def test_sum_4(self):
        self.assertEqual(Solution().brokenCalc(1024,1),1023, "should be 1023")

if __name__ == '__main__':
    unittest.main()



