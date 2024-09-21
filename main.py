class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        chars = list(s)
        for i in range(len(chars) - 1):
            score += abs(ord(chars[i]) - ord(chars[i+1]))

        return score


s = Solution()
print(s.scoreOfString("zaz"))