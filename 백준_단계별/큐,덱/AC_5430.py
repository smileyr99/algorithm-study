import sys
from collections import deque

T = int(sys.stdin.readline())
for i in range(T):
    flag = False
    cnt = 0
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    q = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if n == 0:
        q = []

    for j in p:
        if j == 'R':
            cnt += 1
        elif j == 'D':
            if q:
                if cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                flag = True
                print("error")
                break
    if not flag:
        if cnt % 2 == 0:
            print("[", ",".join(q), "]", sep="")
        else:
            q.reverse()
            print("[", ",".join(q), "]", sep="")

