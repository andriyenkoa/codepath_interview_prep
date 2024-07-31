from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                second_number = stack.pop()
                first_number = stack.pop()

                if token == '+':
                    stack.append(first_number + second_number)
                elif token == '-':
                    stack.append(first_number - second_number)
                elif token == '*':
                    stack.append(first_number * second_number)
                else:
                    stack.append(int(first_number / second_number))
            else:
                stack.append(int(token))

        return stack.pop()
