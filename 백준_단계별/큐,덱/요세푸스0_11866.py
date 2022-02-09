import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque(i for i in range(1, n+1))
result = []

while True:
    if not q:
        break

    for i in range(k-1):
        q.append(q.popleft())
    result.append(str(q.popleft()))

print("<", ", ".join(result), ">", sep="")




