class Solution(object):
    def decodeString(self, s):
        stack = []
        num = 0
        current = ""

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append((current, num))
                current = ""
                num = 0

            elif ch == ']':
                old_string, repeat = stack.pop()
                current = old_string + current * repeat

            else:
                current += ch

        return current