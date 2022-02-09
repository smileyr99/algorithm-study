N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            out.append(L[i])
            solve(depth+1, i+1, N, M)
            out.pop()
            visited[i] = False

solve(0, 0, N, M)

'''
N과 M(5)에서 오름차순 방식 추가.
idx 적용한 range 조절만 해주면 끝이다. 
'''