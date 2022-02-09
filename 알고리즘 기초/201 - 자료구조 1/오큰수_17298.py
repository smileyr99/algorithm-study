n = int(input())
nums = list(map(int, input().split()))
stack = []
result = [-1 for _ in range(n)]         #오큰수 못찾은 곳 -1 출력

stack.append(0)
i = 1

while stack and i < n:
    while stack and nums[stack[-1]] < nums[i]:
        result[stack[-1]] = nums[i]
        stack.pop()
    stack.append(i)
    i += 1

print(*result)



'''
#시간초과
NGE = 0
result = []
for i in range(0, n):
    j = 1
    flag = False
    while j+i < n:
        if nums[i] < nums[i+j]:
            NGE = nums[i+j]
            result.append(NGE)
            flag = True
            break
        j += 1

    if not flag:
        NGE = -1
        result.append(NGE)

print(*result)
'''









