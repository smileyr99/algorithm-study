import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    # command만 있을 경우
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    # command와 target 모두 있을 경우
    else:
        command, target = temp[0], temp[1]
        target = int(target)

        if command == "add":
            S.add(target)
        elif command == "remove":
            S.discard(target)
        elif command == "check":
            if target in S:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if target in S:
                S.discard(target)
            else:
                S.add(target)