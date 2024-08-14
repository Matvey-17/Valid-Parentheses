def valid(s: str) -> bool:
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif char == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif char == '}' and stack and stack[-1] == '{':
            stack.pop()
        else:
            return False
    return len(stack) == 0


s = input("Введите строку со скобками: ")
res = valid(s)
print(res)