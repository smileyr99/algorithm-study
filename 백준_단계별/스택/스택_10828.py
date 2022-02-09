import sys

class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return not self.items


n = int(sys.stdin.readline())
stk = stack()

for i in range(n):
    str = sys.stdin.readline().split()

    if str[0] == 'push':
        stk.push(str[1])
    elif str[0] == 'pop':
        if stk.isEmpty():
            print(-1)
        else:
            print(stk.pop())
    elif str[0] == 'size':
        print(stk.size())
    elif str[0] == 'empty':
        if stk.isEmpty():
            print(1)
        else:
            print(0)
    elif str[0] == 'top':
        if stk.size() == 0:
            print(-1)
        else:
            print(stk.top())
