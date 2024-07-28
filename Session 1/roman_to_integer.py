class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        output = 0
        idx = 0
        while idx < len(s):
            if idx + 1 < len(s) and converter[s[idx + 1]] > converter[s[idx]]:
                output += (converter[s[idx + 1]] - converter[s[idx]])
                idx += 2
            else:
                output += converter[s[idx]]
                idx += 1

        return output
