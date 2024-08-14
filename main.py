s = input()

def valid(s):
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char == ')' and stack[-1] == '(':
            stack.pop()
        elif char == ']' and stack[-1] == '[':
            stack.pop()
        elif char == '}' and stack[-1] == '{':
            stack.pop()
    if len(stack) == 0:
        return True
    return False

res = valid(s)
print(res)