import sys

string = list(sys.stdin.readline().strip())
answer = []
n = int(sys.stdin.readline())
current = len(string)

for i in range(n):
    inst = sys.stdin.readline().strip()
    if inst[0] == 'L' and string != []:
        answer.append(string.pop())
    if inst[0] == 'D' and answer != []:
        string.append(answer.pop())
    if inst[0] == 'B' and string != []:
        string.pop()
    if inst[0] == 'P':
        string.append(inst[2])

print("".join(string + list(reversed(answer))))
'''
시간복잡도 
 O(1)
 '''

'''
#시간초과
for i in range(n):
    inst = sys.stdin.readline().split()
    if inst[0] == 'L':
        if current != 0:
            current -= 1
    if inst[0] == 'D':
        if current != len(string):
            current += 1
    if inst[0] == 'B':
        if current != 0:
            del string[current-1]
            current -= 1
    if inst[0] == 'P':
        string.insert(current, inst[1])
        current += 1

print("".join(string))
'''

'''
시간복잡도 
 O(n)
 '''




