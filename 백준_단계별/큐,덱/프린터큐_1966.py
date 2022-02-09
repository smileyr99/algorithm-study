import sys
from collections import deque

tn = int(sys.stdin.readline())

for _ in range(tn):
    n, m = map(int, sys.stdin.readline().split())
    priority = deque(map(int, sys.stdin.readline().split()))
    index = deque(range(n)) # 위치
    cnt = 0

    while True:
        if priority[0] == max(priority):
            cnt += 1
            if index[0] == m:
                print(cnt)
                break
            priority.popleft()
            index.popleft()
        else:
            priority.append(priority.popleft())
            index.append(index.popleft())




