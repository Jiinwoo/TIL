n, k = map(int, input().split())

# Please write your code here.
from collections import deque

arr = [ i + 1 for i in range(n)]

q = deque()

for v in arr:
    q.append(v)

result = []
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())
print(*result)

