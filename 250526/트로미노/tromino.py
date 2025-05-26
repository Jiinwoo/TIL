n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
l_block = [[[0, 0], [1, 0],[1, 1]], [[0, 0], [1, 0], [0, 1]], [[0, 0], [0, 1], [1, 1]], [[0, 1], [1, 1], [1, 0]]]
r_block = [[[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 0], [2, 0]]]

# l_block
result = -1
for i in range(n):
    for j in range(m):
        
        for rotated in range(4):
            s = 0
            for pos in l_block[rotated]:
                x, y = pos[0], pos[1]
                if i + x >= n or y + j >= m:
                    s = -1
                    break;
                s += grid[i+x][j+y]
            result = max(result, s)

for i in range(n):
    for j in range(m):
        for rotated in range(2):
            s = 0
            for pos in r_block[rotated]:
                x, y = pos[0], pos[1]
                if i + x >= n or y + j >= m:
                    s = -1
                    break;
                s += grid[i+x][j+y]
            result = max(result, s)
print(result) 