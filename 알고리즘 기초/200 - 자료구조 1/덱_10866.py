import sys
import collections

n = int(sys.stdin.readline())

queue = collections.deque()

for i in range(n):
    string = sys.stdin.readline().split()

    if string[0] == 'push_back':
        queue.appendleft(string[1])

    elif string[0] == 'push_front':
        queue.append(string[1])

    elif string[0] == 'pop_front':
        if queue:
            print(queue.pop())
        else:
            print(-1)

    elif string[0] == 'pop_back':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif string[0] == 'size':
        print(len(queue))

    elif string[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif string[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[len(queue)-1])

    elif string[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[0])
