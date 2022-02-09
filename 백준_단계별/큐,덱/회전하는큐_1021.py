import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, input().split()))
q = deque(range(1, n + 1))

cnt = 0
for i in range(m):
    index = q.index(num[i])
    if index < len(q) - index:
        while True:
            if num[i] == q[0]:
                q.popleft()
                break
            cnt += 1
            q.append(q.popleft())
    else:
        while True:
            if num[i] == q[0]:
                q.popleft()
                break
            cnt += 1
            q.insert(0, q.pop())

print(cnt)
