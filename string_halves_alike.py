class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half=len(s)//2
        countL=0
        countR=0
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for char in s[:half]:
            if char in vowels: countL+=1
        for char in s[half:]:
            if char in vowels: countR+=1
        return countL==countR