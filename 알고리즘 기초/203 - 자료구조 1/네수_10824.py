import sys

A, B, C, D = map(str, input().split())

intAB = int(A+B)
intCD = int(C+D)

print(intAB + intCD)

"""
nums = list(sys.stdin.readline().split())
result = []
for i in range(len(nums)):
    if i % 2 == 0:
        num = str(nums[i]) + str(nums[i+1])
        result.append(int(num))

print(sum(result))
"""
