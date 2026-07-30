class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for v in tokens:
            if v=="+":
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)
            elif v=="-":
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            elif v=="*":
                b=stack.pop()
                a=stack.pop()
                stack.append(a*b)
            elif v=="/":
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(v))

        return stack.pop()