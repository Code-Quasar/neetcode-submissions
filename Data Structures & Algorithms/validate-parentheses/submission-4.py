class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {"(": ")", "{" : "}", "[" : "]"}
        for char in s:
            if char in maps:
                stack.append(char)
            elif stack and char == maps[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0