def dfs(depth, idx):
    if depth == 6:
        print(*out)
        return

    for i in range(idx, k):
        out.append(S[i])
        dfs(depth + 1, i + 1)
        out.pop()


while True:
    arrs = list(map(int, input().split()))
    k = arrs[0]
    S = arrs[1:]
    out = []
    dfs(0, 0)
    if k == 0:
        exit()
    print()




# 라이브러리 이용

'''
import itertools

while True:

    array = list(map(int, input().split()))

    k = array[0]
    S = array[1:]

    for i in itertools.combinations(S, 6):
        print(*i)

    if k == 0:
        exit()
    print()
'''