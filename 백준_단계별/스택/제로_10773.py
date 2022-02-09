import sys

k = int(input())
stack = []

for i in range(k):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))