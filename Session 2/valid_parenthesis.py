class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        checker = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        for one_char in s:
            if one_char in checker.keys():
                stack.append(checker[one_char])
            else:
                if stack and stack[-1] == one_char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
