import sys

n = int(sys.stdin.readline())

#스택 이용
for i in range(n):
    string = input()
    string += " "
    stack = []
    for j in string:
        if j != " ":
            stack.append(j)
        else:
            while stack:
                print(stack.pop(), end = '')
            print(' ', end = "")
    print()

'''
#리스트 이용
for i in range(n):
    string = sys.stdin.readline().split()
    for j in string:
        print(j[::-1], end=' ') #[start:end:step] :: step만큼 문자를 건너뛰면서 추출 (-1이므로 역으로)
    print()
'''

