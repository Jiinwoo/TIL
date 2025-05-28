n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


result = 0

for i in range(n):
    for j in range(n):
        # 해당 좌표 아래
    
        for a in range(1, n-1):
            for b in range(1, n-1):
                cx, cy = i + 1, j
                if cx >= n: 
                    break
                max_s = 0  
                possible = True
                for _ in range(a):
                    cx, cy = cx - 1, cy + 1
                    if 0 <= cx < n and 0 <= cy < n:
                        max_s += grid[cx][cy]
                    else:
                        possible = False
                    
                for _ in range(b):
                    cx, cy = cx - 1, cy - 1
                    if 0 <= cx < n and 0 <= cy < n:
                        max_s += grid[cx][cy]
                    else:
                        possible = False

                for _ in range(a):
                    cx, cy = cx + 1, cy - 1

                    if 0 <= cx < n and 0 <= cy < n:
                        max_s += grid[cx][cy]
                    else:
                        possible = False

                for _ in range(b):
                    cx, cy = cx + 1, cy + 1
                    if 0 <= cx < n and 0 <= cy < n:
                        max_s += grid[cx][cy]
                    else:
                        possible = False
                if possible:
                    # print(a, b, i, j, max_s)
                    result = max(result, max_s)
print(result) 

                    
                


                
        