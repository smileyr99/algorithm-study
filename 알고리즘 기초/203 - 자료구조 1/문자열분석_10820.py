import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    num = 0
    lower = 0
    upper = 0
    blank = 0
    if not s:
        break
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            num += 1
        else:
            blank += 1
    print(lower, upper, num, blank)
