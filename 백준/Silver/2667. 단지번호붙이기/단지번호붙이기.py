n = int(input().strip())
a = [list(map(int, input().strip())) for _ in range(n)]

def dfs(x, y):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    stack = [(x, y)]
    count = 0

    while stack:
        cx, cy = stack.pop()
        if 0 <= cx < n and 0 <= cy < n and a[cx][cy] == 1:
            a[cx][cy] = -1
            count += 1
            for dx, dy in directions:
                nx, ny = cx+dx, cy+dy
                stack.append((nx, ny))
    return count

complexes = []

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            complexes.append(dfs(i, j))

print(len(complexes))

for count in sorted(complexes):
    print(count)