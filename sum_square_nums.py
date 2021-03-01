"""
633. Sum of Square Numbers

https://leetcode.com/problems/sum-of-square-numbers/

"""
import unittest
from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        maxA = sqrt(c)
     
        for i in range(int(maxA)+1):
 
            if sqrt(c - i**2).is_integer():
                return True
        return False

class TestSum(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Solution().judgeSquareSum(5),True, "should be True")

    def test_case_2(self):
        self.assertEqual(Solution().judgeSquareSum(3), False, "should be False")

    def test_case_3(self):
        self.assertEqual(Solution().judgeSquareSum(4), True, "should be True")

    def test_case_4(self):
        self.assertEqual(Solution().judgeSquareSum(2), True, "should be True")

    def test_case_5(self):
        self.assertEqual(Solution().judgeSquareSum(1), True, "should be True")

def main():
    unittest.main()
main()