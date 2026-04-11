class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {"]" : "[", "}" : "{", ")" : "(" }
        stack = []
        for i in s:
            if i in parenthesis:
                if stack and stack[-1] == parenthesis[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
