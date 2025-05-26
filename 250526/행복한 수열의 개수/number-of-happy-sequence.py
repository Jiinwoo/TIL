n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

result = 0
for i in range(n):
    v = grid[i][0]
    c = 1
    for j in range(1, n):
        if v == grid[i][j]:
            c += 1
        else:
            v = grid[i][j]
            c = 1
        if c >= m:
            result += 1
            break;
    if c >= m:
        result += 1
        break;

for i in range(n):
    v = grid[0][i]
    c = 1
    for j in range(1, n):
        if v == grid[j][i]:
            c += 1
        else:
            v = grid[j][i]
            c = 1
        if c >= m:
            result += 1
            break;
    if c >= m:
        result += 1
        break;
print(result)