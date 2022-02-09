import sys

rE, rS, rM = map(int, sys.stdin.readline().split())
E, S, M, cnt = 1, 1, 1, 1

while True:
    if E == rE and S == rS and M == rM:
        break
    E += 1; S += 1; M += 1; cnt += 1
    if E >= 16:
        E = 1
    if S >= 29:
        S = 1
    if M >= 20:
        M = 1

print(cnt)