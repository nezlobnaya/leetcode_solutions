class Solution:
    def toGoatLatin(self, S: str) -> str:
        letters = "aeiouAEIOU"
        s = S.split()
        new_str =''
        for i, word in enumerate(s, 1):
            if word[0] not in letters:
                word = word[1:] + word[0] + 'ma' + i*"a"
            else: word = word +'ma'+ i*"a"
            new_str = new_str + word + ' '
        return new_str[:-1]

def main():
    S = "The quick brown fox jumped over the lazy dog"
    print(Solution().toGoatLatin(S))

main()
# "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
