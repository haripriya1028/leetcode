class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for b in s:
            if b=='(' or b=='[' or b=='{':
                stack.append(b)
            else:
                if not stack:
                    return False
                top=stack[-1]
                if (top=='(' and b!=')') or (top=='[' and b!=']') or (top=='{' and b!='}'):
                    return False
                stack.pop()
        return not stack
                    
