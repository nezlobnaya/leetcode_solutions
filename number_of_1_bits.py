from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = Counter(bin(n)[2:])
        return c["1"]
        


def main():
    print(Solution().hammingWeight(n=11111111111111111111111111111101))

main()