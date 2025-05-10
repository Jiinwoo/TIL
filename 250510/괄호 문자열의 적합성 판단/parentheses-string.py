str = input()

# Please write your code here.
s = []

for c in str:
    if c == "(":
        s.append(c)
    else:
        if not s:
            print("No")
            exit(0)
        if s[-1] == "(":
            s.pop()
if s:
    print("No")
else:
    print("Yes")