# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:

# Input: s = "a"
# Output: 1

# Example 3:

# Input: s = "bb"
# Output: 2

 

# Constraints:

#     1 <= s.length <= 2000
#     s consits of lower-case and/or upper-case English letters only.

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         odds = sum(v & 1 for v in collections.Counter(s).values())
#         return len(s) - odds + bool(odds)

# class Solution: #count odds
#     def longestPalindrome(self, s: str) -> int:
#         return len(s) - max(sum(v & 1 for v in collections.Counter(s).values()) - 1, 0)
    
# class Solution: #count evens
#     def longestPalindrome(self, s):
#         return min(sum(v & ~1 for v in collections.Counter(s).values()) + 1, len(s))

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         """
#         :type s: str
#         :rtype: int
#         """
#         output = odd = 0
#         count = collections.Counter(s)
#         for c in count:
#             output += count[c]
#             if count[c] % 2 == 1:
#                 output -= 1
#                 odd += 1
#         return output + bool(odd)
import collections

def longestPalindrome(s):
    output = 0
    for v in collections.Counter(s).values():
        output += v // 2 * 2
            
    return min(output + 1, len(s))
    
# class Solution:
#     def longestPalindrome(self, s):
#         return len(s) - max(sum(v & 1 for v in collections.Counter(s).values()) - 1, 0)


if __name__ == '__main__':
    # Use the main function here to test out the implementation
    s = "abccccdd"

    print(f"The longest palindrome is: {longestPalindrome(s)}")
    # Output: 7
    