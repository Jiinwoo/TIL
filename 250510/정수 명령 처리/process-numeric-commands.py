N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.

a = []

for i in range(N):
    cmd, v = command[i], value[i]
    if cmd == "push":
        a.append(v)
    elif cmd == "size":
        print(len(a))
    elif cmd == "empty":
        print(1 if not a else 0)
    elif cmd == "top":
        print(a[-1])
    else:
        p = a.pop()
        print(p)
