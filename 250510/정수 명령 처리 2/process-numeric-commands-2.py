N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.

from collections import deque

q = deque()

for i in range(N):
    cmd, v = command[i], A[i]
    if cmd == "push":
        q.append(v)
    elif cmd == "pop":
        print(q.popleft())
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        print(1 if not q else 0)
    elif cmd == "front":
        print(q[0])


