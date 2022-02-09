import sys

s = list(sys.stdin.readline().strip())
result = []

for i in range(len(s)):
    result.append("".join(s))
    del s[0]

result.sort()
print("\n".join(result))
