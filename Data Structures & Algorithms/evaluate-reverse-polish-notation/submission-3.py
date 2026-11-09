class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            t = tokens[i]

            if t == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif t == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(t))

        return stack[0]