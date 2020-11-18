"""

Suppose we have a string we have to return the longest possible substring that has exactly k number of unique characters, if there are more than one substring of longest possible length, return any of them.

So, if the input is like s = "ppqprqtqtqt", k = 3, then the output will be rqtqtqt as that has length 7.

"""

# Time:  O(n)
# Space: O(1)

# class Solution(object):
#     def lengthOfLongestSubstringKDistinct(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         longest, start, distinct_count, visited = 0, 0, 0, [0 for _ in xrange(256)]
#         for i, char in enumerate(s):
#             if visited[ord(char)] == 0:
#                 distinct_count += 1
#             visited[ord(char)] += 1
#             while distinct_count > k:
#                 visited[ord(s[start])] -= 1
#                 if visited[ord(s[start])] == 0:
#                     distinct_count -= 1
#                 start += 1
#             longest = max(longest, i - start + 1)
#         return longest


# Time:  O(n)
# Space: O(1)
from collections import Counter


class Solution2(object):
    # def longest_substring_with_k_distinct(self, s, k):
    #     """
    #     :type s: str
    #     :type k: int
    #     :rtype: int
    #     """
    #     counter = Counter() #initiate a counter
    #     left, max_length = 0, 0 # left pointer
    #     for right, char in enumerate(s): #right pointer
    #         counter[char] += 1
    #         while len(counter) > k: #if len of counter > k 
    #             counter[s[left]] -= 1 #we move left counter and decrement the counter 
    #             if counter[s[left]] == 0: #if a count of a char is zero, 
    #                 del counter[s[left]] #we remove it from counter dic
    #             left += 1
    #         max_length = max(max_length, right-left+1)
    #     return max_length
    
    def longest_substring_with_k_distinct(self, str1, k):
        window_start, max_length = 0,0
        char_frequency = {}
  # in the following loop we'll try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1
    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
            while len(char_frequency) > k:
                left_char = str1[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1  # shrink the window
    # remember the maximum length so far
            max_length = max(max_length, window_end-window_start + 1)
        return max_length



s = Solution2()
def main():
  print("Length of the longest substr1ing: " + str(s.longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substr1ing: " + str(s.longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substr1ing: " + str(s.longest_substring_with_k_distinct("cbbebi", 3)))


main()
