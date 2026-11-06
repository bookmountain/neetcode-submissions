class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in "({[":
                stack.append(c)
            elif not stack:
                return False
            else:
                if pairs[c] == stack[-1]:
                    stack.pop()
                else: 
                    return False
        
        return len(stack) == 0