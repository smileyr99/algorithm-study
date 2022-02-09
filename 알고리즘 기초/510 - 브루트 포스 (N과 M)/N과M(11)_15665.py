N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(N):
        if overlap != L[i]:
            out.append(L[i])
            overlap = L[i]
            solve(depth+1, N, M)
            out.pop()

solve(0, N, M)

'''
1. 비내림차순 조건을 위해 사용했던 idx로 range 조절 방법을 뺀다.
2. 같은 수를 여러 번 골라도 되므로 visited 방법을 뺀다.
'''