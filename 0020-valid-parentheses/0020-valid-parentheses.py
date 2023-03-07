class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            elif p == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif p == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif p == "}" and stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return len(stack) == 0
