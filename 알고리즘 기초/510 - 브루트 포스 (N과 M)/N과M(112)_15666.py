def dfs(depth):
    if depth == M:
        s = ' '.join(map(str, lst))
        if s not in d:
            d[s] = 1
            print(s)
        return

    for i in range(N):
        if depth == 0 or lst[-1] <= nums[i]:
            lst.append(nums[i])
            dfs(depth+1)
            lst.pop()


N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
d = {}
lst = []
dfs(0)


'''
문제 해석 : 
N개의 자연수 중에서 M개를 선택하여 수열을 생성한다. 
이때 N에는 중복된 수가 들어 있을 수 있으며 수열은 서로 중복되서는 안되고,
수열 속에서 같은 수가 중복 되어도 된다. 
'''