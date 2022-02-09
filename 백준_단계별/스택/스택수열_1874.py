import sys
# 입력한 숫자가 top이어야 pop가능
n = int(sys.stdin.readline())

stack = []
answer = []
flag = 0
current = 1

for i in range(n):
    num = int(sys.stdin.readline())
    while current <= num:  # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(current)
        answer.append("+")
        current += 1
        # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택에 push

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)