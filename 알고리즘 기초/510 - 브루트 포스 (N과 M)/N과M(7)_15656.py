N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(L[i])
        solve(depth+1, N, M)
        out.pop()

solve(0, N, M)

'''
N과 M(6)와 비슷한데, 같은 수열을 여러번 골라도 되며 오름차순이 없는 문제
visited를 쓰지 않고, idx를 적용한 range도 쓰지 않으면 끝이다.
'''