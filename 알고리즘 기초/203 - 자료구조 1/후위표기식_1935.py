import sys


def priority(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0


s = sys.stdin.readline()
stack = []
result = ''

for i in s:
    if i.isalpha():
        result += i
        continue

    if i == '(':
        stack.append(i)
    elif i == ')':
        while True:
            if stack and stack[-1] != '(':
                result += stack.pop()
            else:
                stack.pop() # '('를 빼주고 탈출
                break
    else:
        while True:
            if stack and (priority(stack[-1]) >= priority(i)):
                result += stack.pop()
            else:
                stack.append(i)
                break

while stack:
    result += stack.pop()
print(result)



