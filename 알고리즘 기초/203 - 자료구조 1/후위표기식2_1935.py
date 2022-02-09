import sys

def cal(oper2, oper1, c):
    if c == '+':
        return oper1 + oper2
    elif c == '-':
        return oper1 - oper2
    elif c == '*':
        return oper1 * oper2
    elif c == '/':
        return oper1 / oper2


n = int(sys.stdin.readline())
string = list(sys.stdin.readline().strip())
num_lst = [0]*n
for i in range(n):
    num_lst[i] = int(input())

for i in range(len(string)):
    if string[i].isalpha():
        string[i] = str(num_lst[ord(string[i])-ord('A')])

stack = []
result = 0

for i in range(len(string)):
    if string[i].isdigit():
        stack.append(string[i])
    else:
        result = cal(float(stack.pop()), float(stack.pop()), string[i])
        stack.append(result)

print('%.2f' %stack[0])
