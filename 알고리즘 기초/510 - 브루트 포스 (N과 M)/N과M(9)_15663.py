N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != L[i]:
            visited[i] = True
            out.append(L[i])
            overlap = L[i]
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()

solve(0, N, M)



'''
overlap이란 변수를 만들어서 전에 쓰인 변수 값과 비교하는 것이다. (초기값 0, 자연수가 아니므로)
위치는 탈출문 바로 아래쪽에 위치하게 했는데, 이유는 깊이가 다를 때마다 변수를 초기화해야하기 때문이다.
그리고 방문 여부를 확인과 동시에 값도 이전에 쓰인 변수 값과 같은지 확인해주고
DFS를 진행하기 직전에 지금의 변수 값을 넘주었다. 
'''