"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

"""

class Solution:
    def isPalindrome(self, s: str) -> bool: #The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator.
        c = ''.join(x.lower() for x in s if x.isalnum()) #The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
        return c == c[::-1]