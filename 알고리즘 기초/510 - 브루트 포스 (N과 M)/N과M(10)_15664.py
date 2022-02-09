N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(idx, N):
        if not visited[i] and overlap != L[i]:
            out.append(L[i])
            visited[i] = True
            overlap = L[i]
            solve(depth+1, i+1, N, M)
            out.pop()
            visited[i] = False

solve(0, 0, N, M)

'''
N과 M(9)에서 비내림차순 조건이 붙은 문제.
N과 M(9)와 같은 방법에서 idx로 i+1을 넘겨주어 range를 조정해주면 해결.
'''