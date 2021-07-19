class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = set(brokenLetters)
        count = 0
        
        for word in text.split(" "):
            if all(c not in s for c in word):
                count+=1
        return count
        