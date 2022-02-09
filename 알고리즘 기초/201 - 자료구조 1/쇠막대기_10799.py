import sys

string = list(sys.stdin.readline().strip())

stick = []
sum = 0

for i in range(len(string)):
    if string[i] == '(':
        stick.append('(')
    else:
        if string[i-1] == '(':
            stick.pop()    # 레이저 하나 뺴주기
            sum += len(stick)    # 스택의 개수만큼
        else:
            stick.pop()
            sum += 1     # 쇠막대기

print(sum)



