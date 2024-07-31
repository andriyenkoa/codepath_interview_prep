class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.recursion(s, 0, len(s) - 1, 1)

    def recursion(self, s: str, i: int, j: int, skip=1):

        while i < j:
            if s[i] != s[j]:
                if skip == 1:
                    return self.recursion(s, i + 1, j, 0) or self.recursion(s, i, j - 1, 0)
                else:
                    return False
            else:
                i += 1
                j -= 1

        return True
