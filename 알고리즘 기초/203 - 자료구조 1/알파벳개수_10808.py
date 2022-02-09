import sys

s = sys.stdin.readline().strip()
alph = 'abcdefghijklmnopqrstuvwxyz'
answer = [0 for _ in range(26)]

for i in s:
    idx = alph.find(i)
    answer[idx] += 1

answer = [str(j) for j in answer]
print(" ".join(answer))