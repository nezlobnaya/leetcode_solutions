"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counts = Counter(p)
        s_counts = Counter(s[0:len(p)])
        for i in range(0, len(s)-len(p)+1):
            if i > 0:
                start, end = s[i-1], s[i+len(p)-1]
                s_counts[start] -=1
                s_counts[end] +=1
                if s_counts[start] <=0:
                    s_counts.pop(start)
            if s_counts == p_counts:
                result.append(i)
        return result

#Time complexity O(n) where n === len(s)
# Space O(1)
#        