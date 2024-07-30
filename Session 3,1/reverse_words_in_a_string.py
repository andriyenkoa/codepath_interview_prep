class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            if not s[i].isalnum():
                i += 1
                continue
            j = i
            while j < len(s) and s[j].isalnum():
                j += 1

            res.append(s[i:j])
            i = j

        return " ".join(res[::-1])
