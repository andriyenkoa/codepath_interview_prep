class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        startIdx = 0

        for one_char in t:
            if one_char == s[startIdx]:
                startIdx += 1
                if startIdx == len(s):
                    return True

        return False
