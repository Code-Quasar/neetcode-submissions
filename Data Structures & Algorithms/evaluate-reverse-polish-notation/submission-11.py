class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(t)
            else:
                second = stack.pop()
                print(type(second))
                stack.append(int(eval(str(stack.pop()) + t + str(second))))
        return int(stack[-1])