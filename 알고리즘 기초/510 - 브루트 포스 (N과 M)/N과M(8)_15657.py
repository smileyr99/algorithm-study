N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(L[i])
        solve(depth+1, i, N, M)
        out.pop()

solve(0, 0, N, M)

'''
N과 M(7)에서 오름차순 조건이 추가된 문제이다.
idx를 적용한 range 조건을 추가하면 된다.
같은 수를 골라도 되므로 idx로 i을 넘겨주어 자기 자신도 포함할 수 있게 한다.
'''