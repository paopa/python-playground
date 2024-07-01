class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
                continue

            if not stack:
                return False

            if c == ")" and stack[-1] == "(":
                stack.pop()
                continue

            if c == "]" and stack[-1] == "[":
                stack.pop()
                continue

            if c == "}" and stack[-1] == "{":
                stack.pop()
                continue

            return False

        return not stack

print(Solution().isValid("()"))  # True
