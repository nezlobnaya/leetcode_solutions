"""
9. Palindrome Number
"""

import unittest
class Solution:
    def isPalindrome(self, x:int) -> bool:
        if x < 0: 
            return False
        rev = 0
        pal = x
        while pal > 0:
            char = pal % 10
            pal = pal //10
            rev = rev * 10 + char
            
        return rev == x 






class TestPalindrome(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(Solution().isPalindrome(121),True, "should be True")
    
    def test_case_2(self):
        self.assertEqual(Solution().isPalindrome(-121),False, "should be False")
    
    def test_case_3(self):
        self.assertEqual(Solution().isPalindrome(10),False, "should be False")
    
    def test_case_4(self):
        self.assertEqual(Solution().isPalindrome(101101),True, "should be True")

if __name__ == '__main__':
    unittest.main()
