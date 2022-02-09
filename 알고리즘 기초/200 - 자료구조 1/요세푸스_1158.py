import sys
import collections

num = sys.stdin.readline().split()
n = int(num[0])
k = int(num[1])

deque = collections.deque([i for i in range(1, n+1)])
answer = []

while len(deque) != 0:
    for i in range(k):
        x = deque.popleft()
        deque.append(x)
    answer.append(deque.pop())

print('<' + ', '.join(map(str, answer)) + '>')

