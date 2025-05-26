n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

result = -1

for i in range(n - 2):
    for j in range(n - 2):
        s = 0
        for k in range(3):
            for l in range(3):
                s += grid[i + k][j + l]
        result = max(result, s)
print(result)