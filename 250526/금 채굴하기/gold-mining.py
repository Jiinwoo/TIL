n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, k):
    visited = [[-1] * n for _ in range(n) ]
    visited[x][y] = 0
    gold = grid[x][y]
    q = deque()
    q.append((x, y, 0))
    while q:
        cx, cy, ck = q.popleft()
        for d in range(4):
            nx, ny, nk = cx + dx[d], cy + dy[d], ck + 1
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and nk <= k:
                visited[nx][ny] = visited[cx][cy] + 1
                gold += grid[nx][ny]
                q.append((nx, ny, nk))
    return gold

result = -1

for i in range(n): 
    for j in range(n):
        for k in range(1, (n // 2) + 1):
            g = bfs(i, j, k)
            # if i == 2 and j == 2:
            #     print(g, k)
            # if i == 1 and j == 1:
            if g * m > (k) ** 2 + (k + 1) ** 2:
                result = max(result, g)
print(result) 
            

