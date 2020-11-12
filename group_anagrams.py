"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Two strings are anagrams of one another if they have the exact same character counts. In other words, “actt” and “tact” are anagrams since both strings have 1 a, 1 c and 2 t’s.

Therefore, all we care about (when making the anagram comparison) is the character counts! Therefore, we can just encode each string as a count of each character from a-z. For example, “tact” would be

1-0-1-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-0-0-0-0.

Then, we can create a hash table where the key is the character-count encoding and the values are the original strings (from the input array) that map to that encoding.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            mapping = [0 for i in range(26)]
            print('processing' + i)
            for l in i:
                print(ord(l))
                mapping[ord(l) - ord('a')] +=1
                
            mapping = "-".join([str(i) for i in mapping])
            
            if mapping in anagrams:
                anagrams[mapping].append(i)
            else:
                anagrams[mapping] = [i]
        return list(anagrams.values())
        
