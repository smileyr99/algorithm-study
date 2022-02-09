from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
result = [-1 for _ in range(n)]
stack = [0]
i = 1
cnt = Counter(nums)

while stack and i < n:
    while stack and cnt[nums[stack[-1]]] < cnt[nums[i]]:
        result[stack[-1]] = nums[i]
        stack.pop()

    stack.append(i)
    i += 1

print(*result)
















