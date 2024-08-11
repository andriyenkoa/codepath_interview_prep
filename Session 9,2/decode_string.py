class Solution:
    def decodeString(self, s):
        idx, num, stack = 0, 0, [""]

        while idx < len(s):
            if s[idx].isdigit():
                num = num * 10 + int(s[idx])
            elif s[idx] == "[":
                stack.append(num)
                num = 0
                stack.append("")
            elif s[idx] == "]":
                str1 = stack.pop()
                rep = stack.pop()
                str2 = stack.pop()
                stack.append(str2 + rep * str1)
            else:
                stack[-1] += s[idx]
            idx += 1

        return stack.pop()
