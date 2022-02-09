import sys

n = 9
high = [int(input()) for i in range(9)]
temp1, temp2 = 0, 0

for i in range(n):
    for j in range(i+1, n):
        if sum(high) - (high[i] + high[j]) == 100:
            temp1 = high[i]
            temp2 = high[j]

high.remove(temp1)
high.remove(temp2)

print('\n'.join(map(str, sorted(high))))


