class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(t)
            else:
                second = stack.pop()
                stack.append(int(eval(f"{stack.pop()} {t} {second}")))
        return int(stack[-1])